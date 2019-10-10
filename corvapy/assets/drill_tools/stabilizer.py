"""Module containing the Stabilizer class

"""
from .tool import Tool

class Stabilizer(Tool):
    """A class for drilling stabilizers
    
    """
    def __init__(self, params):
        """Initializes a Stabilizer instance.
        
        """
        super().__init__(params)
        self.blade_width = params['blade_width']
        self.number_of_blades = params['no_of_blades']
        self.barrel_od = params['gauge_od']
        self.barrel_length = params['gauge_length']
        self.material = params['material']
