# -*- coding: utf-8 -*-
import time
from novaclient.v2.servers import Server
Server.hostname = (lambda self: getattr(self,'OS-EXT-SRV-ATTR:host'))

from auth import get_nova_client

def main():
    runner = AutoEvacuate()
    while True:
        time.sleep(5.0)
        runner.run()

class AutoEvacuate(object):
    def __init__(self):
        self.client = get_nova_client()

    def run(self):
        map(self.treat_failed, self.failed_hosts())

    def failover(self,vm):
        print "Server %s on Host %s is to evacuate..." % (vm.name,vm.hostname())
        try:
            vm.evacuate()
        except Exception as e:
            print "Error({0}): {1}".format(e.errno, e.strerror)

    def treat_failed(self,host):
        map(self.failover,
            self.client.servers.list(search_opts={'all_tenants':1,
                                                  'host':host.hypervisor_hostname}))

    def failed_hosts(self):
        return filter((lambda host: host.state == "down" and host.status == "enabled"),
                      self.client.hypervisors.list())

if __name__ == '__main__':
    main()
