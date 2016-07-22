'''

Author: Hieu Do 

Start Date: June 6, 2016

Description: 
Check the status of the Zenodotus server
Check that multiples nodes' IP addresses are registered to a single hostname

Usage: 


'''

# this is being done so that the resources accounting doesn't interfere with logging
from repyportability import *
_context = locals()
add_dy_support(_context)

serverstatus = dy_import_module('serverstatus.r2py')

zenodotus_servername = "zenodotus.poly.edu"
zenodotus_serverport = 10102

def testZenodotus():
  # first, check the status of the server
  serverstatus.checkServerStatus(zenodotus_servername, zenodotus_serverport)

  # then, check if the Zenodotus is functioning 

if __name__ == '__main__':
  testZenodotus()