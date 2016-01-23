from unittest import TestCase
from nose.tools import ok_, eq_
from novaclient import client
from mock import Mock

from auto_evacuate import AutoEvacuate

class AutoEvacuateTestCase(TestCase):
    def setUp(self):
        self.subject = AutoEvacuate()
        self.subject.client.hypervisors = Mock()
        self.subject.client.hypervisors.list.return_value = []
        self.subject.client.servers = Mock()
        self.subject.client.servers.list.return_value = []

    def tearDown(self):
        pass

    def test_failover(self):
        vm = Mock()
        self.subject.failover(vm)
        vm.evacuate.assert_called_with()

        # with exception
        vm.evacuate.side_effect = Exception
        self.subject.failover(vm)


    def test_treat_failed(self):
        host = Mock()
        host.hypervisor_hostname = "test-host"
        self.subject.failover = Mock()


        self.subject.client.servers.list.return_value = ["a","b","c"]

        self.subject.treat_failed(host)
        self.subject.failover.assert_called_with("c")
        self.subject.client.servers.list.assert_called_with(search_opts={'all_tenants':1,
                                                                         'host':host.hypervisor_hostname})

    def test_failed_hosts(self):
        hosts = range(0,4)
        for i in range(0,4):
            hosts[i] = Mock()

        hosts[0].state = "up"
        hosts[0].status = "enabled"
        hosts[1].state = "down"
        hosts[1].status = "enabled"
        hosts[2].state = "up"
        hosts[2].status = "disabled"
        hosts[3].state = "down"
        hosts[3].status = "disabled"
        self.subject.client.hypervisors.list.return_value = hosts

        failes = self.subject.failed_hosts()
        self.assertEqual(failes, [hosts[1]])
