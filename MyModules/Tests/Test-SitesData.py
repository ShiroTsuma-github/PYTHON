import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from MyModules.SitesData import SitesInformation as SI
    
class TestWorking(unittest.TestCase):
    print('yes')