"""Module containing the Motor class

"""
from .tool import Tool
from .stabilizer import Stabilizer

class Motor(Tool):
    """A class for mud motors

    """
    def __init__(self, params):
        """Initializes a Motor instance.
        
        """
        params['connection_type'] = None
        super().__init__(params)
        self.make = params['make']
        self.serial_number = params['serial_number']
        
        self.max_diff_pressure = params['max_operating_differential_pressure']
        self.max_torque = params['torque_at_max_operating_differential_pressure']        
        
        self.min_flow = params['min_standard_flowrate']
        self.max_flow = params['max_standard_flowrate']

        self.number_rotor_lobes = params['number_rotor_lobes']
        self.number_stator_lobes = params['number_stator_lobes']

        self.bend = params['bend_range']

        self.rpg = params['rpg']
        self.stages = params['stages']
        
        self.stabilizer = MotorStabilizer(params['stabilizer']) if params['has_stabilizer'] is True else None

class MotorStabilizer(Stabilizer):
    """A special class of Stabilizer specifically for motor stabilizers
    
    """
    def __init__(self, params):
        """Initializes a MotorStabilizer instance.
        
        """
        params['family'] = 'stabilizer'
        super().__init__(params)
        self.center_to_bit = params['stab_centerpoint_to_bit']
