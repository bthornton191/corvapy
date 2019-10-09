import requests

API_ENDPOINT = 'https://api.corva.ai/v1'
PROVIDER = 'corva'

class Corva():    

    # def __init__(self, email, password, api_key):
    def __init__(self, api_key):
        
        self.session = requests.Session()
        self.api_key = api_key
    
    def get_drillstrings(self, well_name):
        well = self.get_well(well_name)
        asset_id = well['id']
        response = self._get('/data', params={'provider': PROVIDER, 'collection': 'data.drillstring', 'query': '{asset_id#eq#' + str(asset_id) + '}', 'limit': 0})
        return response.json()
    
    def get_assets(self, types='all', search=''):
        response = self._get('/assets', params={'types': types, 'search': search})
        return response.json()
        
    def get_all_rigs(self):
        return self.get_assets(types='Rig')
    
    def get_rig(self, rig_name):
        return self.get_assets(types='Rig', search=rig_name)[0] 
       
    def get_all_wells(self):
        return self.get_assets(types='Well')
    
    def get_well(self, well_name):
        return self.get_assets(types='Well', search=well_name)[0] 
    
    def _get(self, url, headers=None, **kwargs):
        # Add to the headers
        headers = {} if headers is None else headers.copy()
        headers['Authorization'] = f'API {self.api_key}'

        return self.session.get(API_ENDPOINT + f'/{url}', headers=headers, **kwargs)
    
    def _post(self, url, headers=dict, **kwargs):
        headers = {} if headers is None else headers.copy()
        headers['Authorization'] = f'Bearer {self.api_key}' 
        return self.session.get(API_ENDPOINT + f'/{url}', headers=headers, **kwargs)


class LoginError(Exception):
    pass




        
