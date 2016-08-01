'''

Author:
  Hieu Do 

Start Date: 
  June 6, 2016

Description: 
  Check if time servers are running and if ntp and tcp time work

Credits:
  This monitoring script uses part of the code from `test_time_servers_running.py` and `test_time_tcp.py` 
  https://github.com/SeattleTestbed/integrationtests/tree/master/time

Usage: 
  python time_monitor.py

'''
import os
import sys

# this is being done so that the resources accounting doesn't interfere with logging
from repyportability import *
_context = locals()
add_dy_support(_context)

advertise = dy_import_module("advertise.r2py")

def checkTimeServersStatus():
  servers = advertise.advertise_lookup("time_server")
  if len(servers) != 0:
    print "Running timeservers:", servers
    return True
  print "No timeservers are running."
  return False


if __name__ == "__main__":
  checkTimeServersStatus()