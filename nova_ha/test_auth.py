from unittest import TestCase
from nose.tools import ok_, eq_
from auth import get_nova_client

class AuthTestCase(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_auth(self):
        get_nova_client
        pass
