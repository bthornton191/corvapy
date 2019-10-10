"""Module containing the base class for all drilling tools

"""
class Tool():
    """Base class for all drilling tools

    """
    def __init__(self, params : dict):
        """Initializes the drilling tool by extracting the parameters from the parameters dictionary.  In the corva api these dictionaries are located at drillstring.data.components.
        
        """
        self.length = params['component_length'] if 'component_length' in params and params['component_length'] is not None else params['length']
        self.outer_diameter = params['outer_diameter']
        self.inner_diameter = params['inner_diameter']
        self.tool_type = params['family']
        self.weight = params['weight']
        self.params = params
