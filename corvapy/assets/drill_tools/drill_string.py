"""Module containing the DrillString class

"""
from .hw_pipe import HwPipe as _HwPipe
from .drill_pipe import DrillPipe as _DrillPipe
from .agitator import Agitator as _Agitator
from .drill_collar import DrillCollar as _DrillCollar
from .jar import Jar as _Jar
from .mwd_tool import MwdTool as _MwdTool
from .pdc_bit import PdcBit as _PdcBit
from .motor import Motor as _Motor
from .instrumentation_sub import InstrumentationSub as _InstrumentationSub
from .stabilizer import Stabilizer as _Stabilizer

FAMILY_MAP = {
    'dp': _DrillPipe,
    'hwdp': _HwPipe,
    'agitator': _Agitator,
    'dc': _DrillCollar,
    'jar': _Jar,
    'mwd': _MwdTool,
    'sub': _InstrumentationSub,
    'stabilizer': _Stabilizer,
    'pdm': _Motor,
    'bit': _PdcBit    
}

class DrillString():
    """Contains data about a corva drill string

    Instance Attributes
    -------------------
    start_depth : int
        Depth at which use of this drill string began
    start_time : int
        Unix time at which use of this drill string began
    tools : list
        A list of tool objects that make up this drill string
    params : dict
        Nested dictionary of all the parameters stored for this drill string in corva

    """
    def __init__(self, params):
        """Initializes the DrillString instance.

        Parameters
        ----------
        params : dict
            Nested dictionary of all the parameters stored for this drill string in corva
        
        """
        self.start_depth = params['data']['start_depth']
        
        self.tools = []
        """A list of all the tools in the DrillString

        """
        for component_params in params['data']['components']:
            component_family = component_params['family']
            tool = FAMILY_MAP[component_family](component_params)
            self.tools.append(tool)

        self.params = params
