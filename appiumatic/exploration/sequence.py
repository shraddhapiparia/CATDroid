import time
import collections
import logging
import random
from abstraction import create_launch_event, create_home_event, create_back_event, synthesize, make_event_serializable
from ui_analysis import get_available_events, get_current_state
from hashing import generate_sequence_hash, generate_event_hash
from exploration.utils import remove_termination_events, write_sequence_to_file, explored_beyond_boundaries
from framework.utils import adb
from allpairspy import AllPairs

logger = logging.getLogger(__name__)


class SequenceGenerator:
    def __init__(self,
                 database,
                 termination_criterion,
                 event_selection_strategy,
                 setup_strategy,
                 tear_down_strategy,
                 executor_factory):
        self.database = database
        self.termination_criterion = termination_criterion
        self.event_selection_strategy = event_selection_strategy
        self.setup_strategy = setup_strategy
        self.tear_down_strategy = tear_down_strategy
        self.executor_factory = executor_factory

    def generate(self, sequence_info, app_package_name, suite_id, adbpath):
        current_state = sequence_info.start_state
        executor = self.executor_factory(driver=sequence_info.driver)
        # Reset all context variables
        executor.executeContext("CHANGE_LANDSCAPE")
        executor.executeContext("BATTERY_HIGH")
        executor.executeContext("POWER_ON")
        executor.executeContext("INTERNET_CONNECTED")
        # Below line uses variables for conext aware testing
        # randlist = ["CHANGE_LANDSCAPE","CHANGE_PORTRAIT","POWER_ON","POWER_OFF","BATTERY_HIGH","BATTERY_LOW","INTERNET_CONNECTED","INTERNET_DISCONNECTED"]
        # Added below lines for Rand-Start Context events -- comment if not doing  rand-start context aware testing
        # event = random.choice(randlist)
        # executor.executeContext(event)
        # End of Rand-Start
        # Iterative-Start Context -- comment if not using iterative start context aware testing
        # executed_events, idx = [], 0
        # if len(executed_events) <= len(randlist):
        #    event = randlist[idx]
        #    executor.executeContext(event)
        #    idx += 1
        #    executed_events.append(event)
        # else:
        #    idx = 0
        #    executed_events = []
        # End of Iterative Start
        context_events = []
        cevents = [["CHANGE_LANDSCAPE","CHANGE_PORTRAIT"],["POWER_ON","POWER_OFF"],["BATTERY_HIGH","BATTERY_LOW"],["INTERNET_CONNECTED","INTERNET_DISCONNECTED"]]
        executed_list = {}
        for val in AllPairs(cevents):
            context_events.append(val)
        while not self.termination_criterion(database=self.database,
                                             sequence_hash=generate_sequence_hash(sequence_info.events),
                                             suite_id=suite_id,
                                             event_count=len(sequence_info.events)):
            # Uncomment below lines for pairwise context algorithm --added by SP
            # if not context_events:
            #     for val in AllPairs(cevents):
            #         context_events.append(val)
            # combination = context_events[0]
            # context_events.remove(combination)
            # for context_event in combination:
            #     context_event = str(context_event)
            #     executor.executeContext(context_event)
            # End of pairwise context algorithm --added by SP
            
            # for val in AllPairs(cevents):
            # 	context_events.append(val)
            logger.debug("-------------called process next event---------")
            next_event_info = self.process_next_event(sequence_info, suite_id, executor, executed_list, context_events)
            # logger.debug("-------------context events are {}".format(context_events))
            # next_event_info = self.process_next_event(sequence_info, suite_id, executor)
            current_state = next_event_info.resulting_state
            self.update_knowledge_base(suite_id, next_event_info, sequence_info)
            sequence_info.events.append(next_event_info.event)

            # end the sequence if event explores beyond boundary of the application
            if explored_beyond_boundaries(sequence_info.driver.current_package, app_package_name):
                self.database.add_termination_event(next_event_info.event_hash, suite_id)
                logger.debug("Identified termination event: {}".format(next_event_info.event_hash))
                break

        # always end sequences by clicking the home event, but do not add the event to the test case
        home_event = create_home_event(current_state)
        executor.execute(home_event)

        return int(time.time() - sequence_info.start_time)

    def initialize(self):
        logger.debug("-------------INSIDE INITIALIZED----------.")
        start_time = int(time.time())
        logger.debug("-------------START TIME----------.")
        driver = self.setup_strategy()
        logger.debug("-------------SET UP STRATEGY----------.")
        launch_event = create_launch_event()
        logger.debug("-------------LAUNCH EVENT CREATED----------.")
        start_state = get_current_state(driver)
        logger.debug("-------------CURRENT STATE----------.")
        complete_event = synthesize(launch_event, start_state)
        logger.debug("-------------EVENT SYNTHESIZED----------.")
        events = [complete_event]
        logger.debug("-------------TC INITIALIZATION COMPLETE----------.")

        SequenceInfo = collections.namedtuple("SequenceInfo", ["driver", "events", "start_time", "start_state"])
        return SequenceInfo(driver, events, start_time, start_state)
        

    def process_next_event(self, sequence_info, suite_id, executor, executed_list, context_events):
        selected_event = self.choose_event(sequence_info, suite_id)
        sel_event_code = generate_event_hash(selected_event)
        # logger.debug("selected event and type {} {}".format(selected_event,sel_event_code))
        if sel_event_code in executed_list:
            # logger.debug("---------------------1 {}".format(executed_list[sel_event_code]))
            diff =  [i for i in context_events if i not in executed_list[sel_event_code]]
            # logger.debug("diff is {}".format(diff))
            if diff:
                # logger.debug("2")
                executed_list[sel_event_code].append(diff[0])
                for cevent in diff[0]:
                    cevent = str(cevent)
                    executor.executeContext(cevent)
        else:
            # logger.debug("3")
            executed_list[sel_event_code] = [context_events[0]]
            for cevent in context_events[0]:
                # logger.debug("4")
                cevent = str(cevent)
                executor.executeContext(cevent)
        			
        logger.debug("SEQUENCE--------------PROCESS NEXT EVENT--------------")
        executor.execute(selected_event)
        resulting_state = get_current_state(sequence_info.driver)
        complete_event = synthesize(selected_event, resulting_state)
        event_hash = generate_event_hash(complete_event)
        NextEventInfo = collections.namedtuple("NextEventInfo", ["event", "event_hash", "resulting_state"])
        # logger.debug("^^^^^^^^^^^^^^^^^^^^^^^^^ executed events {}".format(executed_list))

        return NextEventInfo(complete_event, event_hash, resulting_state)


    def choose_event(self, sequence_info, suite_id):
        logger.debug("SEQUENCE--------------CHOOSE EVENT--------------")
        partial_events = get_available_events(sequence_info.driver)
        non_termination_events = remove_termination_events(self.database, suite_id, partial_events)
        logger.debug("++++++++++++++++++++++++++NON TERMINATION EVENTS: {}".format(non_termination_events))
        if non_termination_events:
            selected_event = self.event_selection_strategy(events=non_termination_events,
                                                           database=self.database,
                                                           suite_id=suite_id)
        else:
            logger.warning("No events available for selection. All events in the current state are marked as "
                           "termination events.")
            current_state = partial_events[0]["precondition"]
            selected_event = create_back_event(current_state)

        return selected_event

    def update_knowledge_base(self, suite_id, next_event_info, sequence_info):
        self.database.update_event_frequency(suite_id, next_event_info.event_hash)

    def finalize(self, sequence_count, suite_id, sequence_info, output_paths):
        end_time = time.time()
        sequence_duration = int(end_time - sequence_info.start_time)
        self.database.add_sequence(generate_sequence_hash(sequence_info.events),
                                   suite_id,
                                   sequence_info.start_time,
                                   sequence_duration)
        sequence_path = write_sequence_to_file(output_paths.sequences,
                                               sequence_info.events,
                                               sequence_count,
                                               sequence_duration)
        logger.debug("Sequence {} written to {}.".format(sequence_count, sequence_path))

        logger.debug("Beginning test case teardown.")
        self.tear_down_strategy(sequence_info.driver)
