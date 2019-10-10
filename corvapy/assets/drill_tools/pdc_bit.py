"""Module containing the PdcBit class

"""
from .tool import Tool
from . import ToolCompatibilityError

class PdcBit(Tool):
    def __init__(self, params):
        params['connection_type'] = None
        super().__init__(params)
        self.make = params['make']
        self.model = params['model']
        self.serial_number = params['serial_number']
        self.outer_diameter = params['size']
        self.stub_od = params['shank_od']
        self.nozzel_sizes = params['nozzle_sizes']
        self.blade_count = None

        # Raise an error if the bit type isn't pdc
        if params['bit_type'] != 'pdc':
            raise ToolCompatibilityError('This library does not support {} as a bit type'.format(params['bit_type']))
