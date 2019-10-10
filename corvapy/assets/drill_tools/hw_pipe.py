"""Module containing the HwPipe class

"""
from .drill_pipe import DrillPipe

class HwPipe(DrillPipe):
    """A class for heavy weight pipe
    
    """
    def __init__(self, params):
        """Initializes HwPipe instance.
        
        """
        super().__init__(params)
