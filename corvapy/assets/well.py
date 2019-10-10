"""Module containing the Well class

"""
class Well():
    """Class containing data about a corva well

    """
    def __init__(self, params, corva):
        self.name = params['name']
        self.rig = params['parent_asset_name']
        self.casings = self._get_casing(corva)
        self.surveys = self._get_survey(corva)
        self.drillstrings = corva.get_drillstrings(self.name)
        self.params = params

    def _get_survey(self, corva):     
        """Returns a list of the :obj:`Survey` objects associated with this well.
        
        Parameters
        ----------
        corva : Corva
            :obj:`Corva` session
        
        Returns
        -------
        list
            list of :obj:`Survey` objects associated with this well

        Note
        ----
        This method only returns actual surveys.

        """   
        surveys = corva.get_surveys(self.name)
        return surveys

    def _get_casing(self, corva):
        """Returns a list of the :obj:`Casing` objects associated with this well.
        
        Parameters
        ----------
        corva : Corva
            :obj:`Corva` session
        
        Returns
        -------
        list
            list of :obj:`Casing` objects associated with this well

        """
        casings = corva.get_casings(self.name)
        return casings

class Casing():
    def __init__(self, params):
        self.bottom_depth = params['data']['bottom_depth']
        self.top_depth = params['data']['top_depth']
        self.outer_diameter = params['data']['outer_diameter']
        self.inner_diameter = params['data']['inner_diameter']
        self.length = params['data']['length']
        self.grade = params['data']['grade']
        self.params = params

class Survey():
    def __init__(self, params):
        self.x = [station['easting'] for station in params['data']['stations']]
        self.y = [station['northing'] for station in params['data']['stations']]
        self.tvd = [station['tvd'] for station in params['data']['stations']]
        self.md = [station['measured_depth'] for station in params['data']['stations']]
        self.azimuth = [station['azimuth'] for station in params['data']['stations']]
        self.inclination = [station['inclination'] for station in params['data']['stations']]
        self.dls = [station['dls'] for station in params['data']['stations']]
        self.timestamp = params['timestamp']
        self.params = params
