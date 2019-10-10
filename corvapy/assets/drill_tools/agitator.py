"""Module containing the Agitator class

"""
from .tool import Tool

class Agitator(Tool):
    """A class for agitators
    
    """
    def __init__(self, params):
        """Initializes Agitator instance.
        
        """
        super().__init__(params)
