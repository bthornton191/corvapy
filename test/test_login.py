"""Initial test module

"""
import unittest

from corvapy.corva import Corva

from corva_credentials import API_KEY

class Test_BasicMethods(unittest.TestCase):
    """Tests some of the first few basic methods
    
    """
    def setUp(self):
        self.corva = Corva(API_KEY)

    def test_get_assets(self):
        """Tests that Corva can get a list of assets

        """
        assets = self.corva.get_assets()
        self.assertTrue('asset_type' in assets[0])
    
    def test_get_hp_604(self):
        """Tests that Corva can get the H&P 604 asset info

        """
        rig_name = 'H&P 604'
        rig = self.corva.get_rig(rig_name)
        self.assertEqual(rig['name'], rig_name)

    def test_get_drillstrings(self):
        """Tests that Corva can get the drillstrings for a well

        """
        drillstrings = self.corva.get_drillstrings('University 7-43 115H')
        self.assertEqual(drillstrings[0]['data']['start_depth'], 15735)

    def tearDown(self):
        return
