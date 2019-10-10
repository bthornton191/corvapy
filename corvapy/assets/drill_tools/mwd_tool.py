"""Module containing the MwdTool class

"""
from .tool import Tool

class MwdTool(Tool):
    """A class for mwd tools
    
    """
    def __init__(self, params):
        """Initializes an MwdTool instance.
        
        """
        super().__init__(params)
        self.bit_to_survey = params['bit_to_survey_distance']
