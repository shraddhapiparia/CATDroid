import logging
logger = logging.getLogger(__name__)

class ContextSequence:

    def __init__(self, context_covering_array, covering_array_index):
        self.context_covering_array = context_covering_array
        self.covering_array_index = covering_array_index


    def iterate_covering_array(self, covering_array_index):
        return covering_array_index + 1 if covering_array_index < len(self.context_covering_array) else 0
