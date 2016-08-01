'''

Author: 
  Hieu Do 

Start Date: 
  June 6, 2016

Description: 
  Check that multiples nodes' IP addresses are registered to a single hostname

Credits:
  This monitoring script uses part of the code from `zenodotus_alive.py`
  https://github.com/SeattleTestbed/integrationtests/blob/master/zenodotus/zenodotus_alive.py

Usage: 
  python zenodotus_monitor.py

'''
import os
import sys

# this is being done so that the resources accounting doesn't interfere with logging
from repyportability import *
_context = locals()
add_dy_support(_context)

advertise = dy_import_module("advertise.r2py")
random = dy_import_module("random.r2py")
rsa = dy_import_module('rsa.r2py')
sha = dy_import_module('sha.r2py')


zenodotus_servername = "zenodotus.poly.edu"
zenodotus_ipaddr = '128.238.63.50'


def _dns_mapping_exists(name, ip_address):
  for line in os.popen('dig @8.8.8.8 ' + name, 'r').readlines():
    # Can't do direct comparison between dig's output and hardcoded string
    # TTL value changes on each call.  Instead, check if any of the lines
    # contain the entry for blackbox.
    if name + '.' in line.split() and ip_address in line.split():
      return True
  return False


def _generate_random_ip_address():
  octets = []
  for octet in xrange(4):
    octets.append(str(random.random_int_below(256)))
  return '.'.join(octets)


def _generate_random_dns_entry():
  random_publickey = rsa.rsa_gen_pubpriv_keys(1024)[0]
  random_publickey_string = rsa.rsa_publickey_to_string(random_publickey)
  random_subdomain = "test-" + sha.sha_hexhash(random_publickey_string)
  random_dns_entry = random_subdomain + '.' + zenodotus_servername  
  return random_dns_entry

def testZenodotus():
  print "Beginning query."
  success = True

  try:
    # Query zenodotus
    if not _dns_mapping_exists(zenodotus_servername, zenodotus_ipaddr):
      print "Zenodotus failed to respond properly!"
      # Query is invalid!
      success = False

    # Check that advertised values work
    # Map an entirely random IP to a random DNS name. The mapped IP does
    # not have to actually exist (but should still be valid).
    random_ip_address = _generate_random_ip_address()
    r2andom_ip_address = _generate_random_ip_address()

    random_dns_entry = _generate_random_dns_entry()

    random_ip_address = _generate_random_ip_address()
    print "Announcing", random_dns_entry, random_ip_address, r2andom_ip_address
    advertise.advertise_announce(random_dns_entry, random_ip_address, 60)
    advertise.advertise_announce(random_dns_entry, r2andom_ip_address, 60)

    print "Looking up", random_dns_entry, advertise.advertise_lookup(random_dns_entry)

    if not _dns_mapping_exists(random_dns_entry, random_ip_address) and _dns_mapping_exists(random_dns_entry, r2andom_ip_address):
      print "Zenodotus failed to respond properly to advertised subdomain!"
      # Query is invalid!
      success = False

  except Exception, e:
    print "Unknown error!"
    print str(e)
    success = False

  if success:
    print "Query was successful."
    return success

  return success

if __name__ == "__main__":
  testZenodotus()