__author__ = 'Florian Lier'

'''

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
'''

    More info on LUA and NMAP requirements, try URL
    https://gist.github.com/bonsaiviking/10402038

'''

import os
import sys
import subprocess
import ConfigParser


class Check:
    def __init__(self):

        self.hosts = dict()
        self.serious = dict()

        if os.path.isfile('hosts.cfg'):
            try:
                config = ConfigParser.ConfigParser()
                config.read('hosts.cfg')
                host_items = config.items('hosts')
                print "  >> Info: Reading your config file now"

                for i, n in host_items:
                    self.hosts[i] = n
                print "  >> Info: Found the following hosts in *.cfg"

                for key, value in self.hosts.items():
                    print "  >> # " + key + " " + value
            except Exception, e:
                print " >> Error: Reading your *.cfg file %s" % str(e)
                sys.exit(1)
        else:
            print " Error: No hosts.cfg file next to this script"
            sys.exit(1)

    def check(self):
        for i in self.hosts.keys():
            current_host = self.hosts[i]
            print "  >> Now checking %s" % current_host
            try:
                out = subprocess.check_output(["nmap", "-sV",
                                               "--script=ssl-heartbleed.nse",
                                               "--script-args=vulns.showall",
                                               current_host])
                print "  >> Result: %s\n" % out

                if not "NOT VULNERABLE" in out:
                    print "  >> UPS, %s is VULNERABLE" % current_host
                    self.serious[current_host] = str(out)
            except Exception, e:
                print " >> Error: Something went wrong while invoking nmap %s" \
                      % str(e)
                sys.exit(1)


if __name__ == '__main__':
    c = Check()
    c.check()
    if len(c.serious) > 0:
        print "  >> The following hosts are insecure"
        for i in c.serious.keys():
            print "  >> %s" % i

