# -*- coding: utf-8 -*-
import time
from novaclient.v2.servers import Server

from auth import get_nova_client

def main():
    runner = RunKeeper()
    while True:
        time.sleep(5.0)
        runner.run()

class RunKeeper:
    def __init__(self):
        self.client = get_nova_client()

    def keep_running_servers(self,filename='/etc/nova/keep_running_servers'):
        result = []
        for line in open(filename, 'r'):
            try:
                result.append(client.get(line))
            except Exception:
                pass
        return result

    def is_server_down(self,server):
        return server.status == "STOPPED"

    def run():
        map((lambda server:server.start),
            filter(self.is_server_down,self.keep_running_servers))

if __name__ == '__main__':
    main()
