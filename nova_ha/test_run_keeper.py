from unittest import TestCase
from nose.tools import ok_, eq_
from novaclient import client
from mock import mock_open, patch, Mock

from sys import version_info
if version_info.major == 2:
    import __builtin__ as builtins
else:
    import builtins

from run_keeper import RunKeeper

class RunKeeperTestCase(TestCase):
    def setUp(self):
        self.subject = RunKeeper()
        self.subject.client.servers = Mock()

    def test_run(self):
        self.subject.run()

    @patch('__builtin__.open')
    def test_keep_running_servers(self):
        servers = range(2)
        for i in range(2):
            servers[i] = Mock()
        servers[0].status = 'ACTIVE'
        servers[1].status = 'STOPPED'

        self.subject.client.servers.list.return_value = servers


        builtins.open.return_value = ["1111","2222","3333"]
        with patch('{}.open'.format(__name__), mock_open(), create=True):
            self.assertEqual(self.subject.keep_running_servers(),["1111","2222","3333"])


    def test_is_server_down(self):
        server = Mock(side_effect=Exception)
        self.subject.is_server_down(server)

        server = Mock()
        self.subject.is_server_down(server)
