"""Module containing the InstrumentationSub class

"""
from .tool import Tool

class InstrumentationSub(Tool):
    """A class for instrumentation subs
    
    """
    def __init__(self, params):
        """Initializes an InstrumentationSub instance.
        
        """
        super().__init__(params)
        self.name = params['name']

        # Determine the sub vendor
        if 'lodestar' in self.name.lower():
            self.make = 'Lodestart'
        elif 'gyrodata' in self.name.lower():
            self.make = 'Gyrodata'
        elif 'nov' in self.name.lower():
            self.make = 'NOV'
        else:
            self.make = None
