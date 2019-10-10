import requests

from .assets.drill_tools.drill_string import DrillString
from .assets.well import Well, Casing, Survey

API_ENDPOINT = 'https://api.corva.ai/v1'
PROVIDER = 'corva'

class Corva():    

    # def __init__(self, email, password, api_key):
    def __init__(self, api_key):
        
        self.session = requests.Session()
        self.api_key = api_key
    
    def get_drillstrings(self, well_name):
        """Returns a list of :obj:`DrillString` objects used in `well_name`
        
        Parameters
        ----------
        well_name : str
            Name of a well in corva (case sensitive)
        
        Returns
        -------
        list
            List of :obj:`DrillString` objects

        """
        # Get the well's asset id
        well_asset_id = self.get_asset_data('Well', well_name)['id']
        
        # Call the corva api
        response = self._get('/data', params={'provider': PROVIDER, 'collection': 'data.drillstring', 'query': '{asset_id#eq#' + str(well_asset_id) + '}', 'limit': 0})
        
        # Retrieve the drillstrings from the response
        drill_strings = [DrillString(param_set) for param_set in response.json()]
        
        # Return the drill strings
        return drill_strings 
    
    def get_casings(self, well_name):    
        """Gets a list of :obj:`Casing` objects for the well `well_name`.
        
        Parameters
        ----------
        well_name : str
            Corva well name. Case sensitivie.
        
        Returns
        -------
        list
            list of :obj:`Casing` objects
            
        """
        # Get the well's asset id
        well_asset_id = self.get_asset_data('Well', well_name)['id']

        # Call the corva api
        response = self._get('/data', params={'provider': PROVIDER, 'collection': 'data.casing', 'query': '{asset_id#eq#' + str(well_asset_id) + '}', 'limit': 0})
        
        # Retrieve the casings from the response
        casings = [Casing(param_set) for param_set in response.json()]
        
        # Return the casings list
        return casings
    
    def get_surveys(self, well_name):    
        """Gets a list of :obj:`Survey` objects for the well `well_name`.
        
        Parameters
        ----------
        well_name : str
            Corva well name. Case sensitivie.
        
        Returns
        -------
        list
            list of :obj:`Survey` objects
            
        """
        # Get the well's asset id
        well_asset_id = self.get_asset_data('Well', well_name)['id']

        # Call the corva api
        response = self._get('/data', params={'provider': PROVIDER, 'collection': 'data.actual_survey', 'query': '{asset_id#eq#' + str(well_asset_id) + '}', 'limit': 0})
        
        # Retrieve the casing from the response
        surveys = [Survey(param_set) for param_set in response.json()]
        
        # Return the casing list
        return surveys
    
    def get_well(self, well_name):
        """Returns the :obj:`Well` object for the well `well_name`
        
        Parameters
        ----------
        well_name : str
            Corva well name.  Case sensitive.
        
        Returns
        -------
        Well
            :obj:`Well` object for the well `well_name`
            
        """
        params = self.get_asset_data('Well', well_name)
        return Well(params, self)
    
    def get_asset_data(self, asset_type, asset_name):
        """Returns the json data in a dictionary for the asset sepcified by `asset_type` and `asset_name`
        
        Parameters
        ----------
        asset_type : str
            Corva asset type. Options are 'Well', 'Rig', etc.
        asset_name : str
            Corva asset name.  Case sensitive.
        
        Returns
        -------
        dict
            Dictionary of the json data from corva
        
        Raise
        CorvaError
            Raised if the number of assets found is not exactly 1

        """
        # Retrieve the asset data
        assets_data = self.get_all_assets_data(asset_type, asset_name)

        # Confirm that exactly 1 asset was found
        if assets_data == []:
            # If nothing returned, raise an error
            raise CorvaError(f'Asset of name {asset_name} and type {asset_type} not found!')
        
        elif len(assets_data) > 1:
            # If multiple assets are found, raise an error
            raise CorvaError(f'Multiple assets of name {asset_name} and type {asset_type} were found!')
        
        # Return the first asset found
        return assets_data[0]
        
    def get_all_assets_data(self, types='all', search=''):
        response = self._get('/assets', params={'types': types, 'search': search})
        return response.json()
    
    def _get(self, url, headers=None, **kwargs):
        # Add to the headers
        headers = {} if headers is None else headers.copy()
        headers['Authorization'] = f'API {self.api_key}'

        return self.session.get(API_ENDPOINT + f'/{url}', headers=headers, **kwargs)
    
    def _post(self, url, headers=dict, **kwargs):
        headers = {} if headers is None else headers.copy()
        headers['Authorization'] = f'Bearer {self.api_key}' 
        return self.session.get(API_ENDPOINT + f'/{url}', headers=headers, **kwargs)

class CorvaError(Exception):
    pass


        
