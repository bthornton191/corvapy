"""Module containing the DrillPipe class

"""
from .tool import Tool

class DrillPipe(Tool):
    """A class for drill pipe
    
    """
    def __init__(self, params):
        """Initializes DrillPipe instance.
        
        """
        super().__init__(params)
        self.grade = params['grade']
        
        # Check if this is the first section of drill pipe
        if params['order'] == 0:
            # If this is the first section of drill pipe...
            # TODO: Can't assume 10
            self.joints = 10
        else:
            # If this is not the first section of drill pipe, get the number of joints
            self.joints = params['number_of_joints']

        self.total_length = params['length']
