"""Initial test module

"""
import unittest

from corvapy.corva import Corva

from credentials import API_KEY

class Test_BasicMethods(unittest.TestCase):
    """Tests some of the first few basic methods
    
    """
    def setUp(self):
        self.corva = Corva(API_KEY)

        self.well_name = 'University 7-43 115H'

    def test_get_assets(self):
        """Tests that Corva can get a list of assets

        """
        assets = self.corva.get_all_assets_data()
        self.assertTrue('asset_type' in assets[0])
    
    def test_get_hp_604(self):
        """Tests that Corva can get the H&P 604 asset info

        """
        rig_name = 'H&P 604'
        rig = self.corva.get_asset_data('Rig', rig_name)
        self.assertEqual(rig['name'], rig_name)

    def test_get_drillstrings(self):
        """Tests that Corva can get the drillstrings for a well

        """
        drillstrings = self.corva.get_drillstrings(self.well_name)
        self.assertListEqual([drillstring.start_depth for drillstring in drillstrings], [15735, 9404, 8399, 6314, 1])
    
    def test_get_casing(self):
        """Tests that Corva can get the casings for a well

        """
        casings = self.corva.get_casings(self.well_name)
        self.assertListEqual([casing.bottom_depth for casing in casings], [6314, 1981, 19112])
    
    def test_get_survey(self):
        """Tests that Corva can get the casings for a well

        """
        surveys = self.corva.get_surveys(self.well_name)
        self.assertListEqual([survey.md[:5] for survey in surveys], [[0.0, 114.0, 149.84, 184.91, 214.26]])

    def test_get_well_casings(self):
        well = self.corva.get_well(self.well_name)
        self.assertListEqual([casing.bottom_depth for casing in well.casings], [6314, 1981, 19112])
    
    def test_get_well_surveys(self):
        well = self.corva.get_well(self.well_name)
        self.assertListEqual([survey.md[:5] for survey in well.surveys], [[0.0, 114.0, 149.84, 184.91, 214.26]])
    
    def test_get_well_drillstrings(self):
        well = self.corva.get_well(self.well_name)
        self.assertListEqual([drillstring.start_depth for drillstring in well.drillstrings], [15735, 9404, 8399, 6314, 1])
    
    def tearDown(self):
        return
