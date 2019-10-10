"""Module containing the DrillCollar class

"""
from .tool import Tool

class DrillCollar(Tool):
    """A class for drill collars
    
    """
    def __init__(self, params):
        """Initializes DrillCollar instance.
        
        """
        super().__init__(params)
