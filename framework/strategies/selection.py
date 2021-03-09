import random
import logging
from framework.utils import selection as selection_utils


logger = logging.getLogger(__name__)


def uniform_random(events, database=None, suite_id=None):
    assert events is not None
    logger.debug("SELECTION--------------uniform random algo--------------")
    selected_event = random.choice(events)

    return selected_event


def min_frequency_random(events, database, suite_id):
    assert events is not None and suite_id is not None and database is not None

    logger.info("Making min_frequency_random selection from {} available events.".format(len(events)))

    hash_to_events_map = selection_utils.create_hash_to_events_map(events)
    event_hashes = hash_to_events_map.keys()
    event_frequencies = database.get_event_frequencies(event_hashes, suite_id)
    min_frequency_event_hashes = selection_utils.get_min_frequency_event_hashes(event_frequencies)
    selected_event_hash = random.choice(min_frequency_event_hashes)

    return hash_to_events_map[selected_event_hash]


def min_frequency_deterministic(events, database, suite_id):
    assert events is not None and suite_id is not None and database is not None

    logger.info("Making min_frequency_deterministic selection from {}".format(len(events)))

    hash_to_events_map = selection_utils.create_hash_to_events_map(events)
    event_hashes = hash_to_events_map.keys()
    event_frequencies = database.get_event_frequencies(event_hashes, suite_id)
    min_frequency_event_hashes = selection_utils.get_min_frequency_event_hashes(event_frequencies)

    selected_event_hash = min_frequency_event_hashes[0]

    return hash_to_events_map[selected_event_hash]


def frequency_weighted(events, database, suite_id):
    assert events is not None and suite_id is not None and database is not None

    logger.info("Making frequency_weighted selection from {} available events.".format(len(events)))

    hash_to_events_map = selection_utils.create_hash_to_events_map(events)
    event_hashes = hash_to_events_map.keys()
    event_frequencies = database.get_event_frequencies(event_hashes, suite_id)

    event_weights = selection_utils.get_frequency_weights(event_frequencies)
    total_weight = sum(event_weights.values())
    goal_weight = random.uniform(0.0, 1.0) * total_weight
    selected_event = selection_utils.make_weighted_selection(hash_to_events_map, event_weights, goal_weight)

    return selected_event


## Added by kk

def q_learning(events, database, suite_id):
    assert events is not None and suite_id is not None and database is not None

    logger.info("Making q_learning based selection from {} available events.".format(len(events)))

    home_btn_prob = 0.5
    hash_to_events_map = selection_utils.create_hash_to_events_map(events)
    event_hashes = hash_to_events_map.keys()
    event_frequencies = database.get_event_frequencies(event_hashes, suite_id)
    event_qvalues = database.get_event_values(event_hashes, suite_id)

    if random.random() >= home_btn_prob:
        for event_hash, event_frequency in event_frequencies.items():
            if event_frequency == 0:
                event_qvalues[event_hash] = 500
                database.update_event_qvalue(suite_id, event_hash, 500)

        selected_event = selection_utils.get_max_value_event(hash_to_events_map, event_qvalues) # Todo
    return selected_event

# context algorithms added by Shraddha Piparia
def random_start_context(events, database, suite_id):
    assert events is not None and suite_id is not None and database is not None

    logger.info("Making random GUI selection and random context from {} available events.".format(len(events)))

    selected_event = random.choice(events)
    c_event = "dnfjkdh"

    return [selected_event,c_event]

def iterative_start_context(events, database, suite_id):
    assert events is not None and suite_id is not None and database is not None

    return selected_event

def pairs_context(events, database, suite_id):
    assert events is not None and suite_id is not None and database is not None
    # pairwise only context
    return selected_event

def pairs_interleaved(events, database, suite_id):
    assert events is not None and suite_id is not None and database is not None
    # pairwise combinations of context and GUI
    return selected_event

    # Code for EXECUTE Selected event
    # Update Test suite
    # if selected event exits appiumatic
        # update reward to 0
        # set_Qvalue to 0
    # Calculate and set q_value
