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
import traceback
import time
import math

# this is being done so that the resources accounting doesn't interfere with logging
from repyportability import *
_context = locals()
add_dy_support(_context)

advertise = dy_import_module("advertise.r2py")
tcp = dy_import_module("tcp_time.r2py")
ntp = dy_import_module("ntp_time.r2py")
time_interface = dy_import_module("time_interface.r2py")

def checkTimeServersStatus():
  servers = advertise.advertise_lookup("time_server")
  if len(servers) != 0:
    print "Running timeservers:", servers
    return True
  print "No timeservers are running."
  return False

def testTCP():
  notify_str = ''
  connected_server = ''

  # Whenever we fail to do tcp_time_updatetime, we add the exception string
  exception_string_list = []
  
  # get the time 5 times and make sure they are reasonably close
  test_start = getruntime()
  print test_start
  times = []

  time_interface.time_settime(getruntime())

  local_start_time = time.localtime()
 
  # Keep a list of servers we connected to or tried to connect to for time.
  server_list = []

  # Connect to 5 servers and retrieve the time.
  for i in range (5):
    try:
      connected_server = tcp.tcp_time_updatetime(12345)
      current_time = time_interface.time_gettime()
      times.append(current_time)
      server_list.append(connected_server)
      print "Calling time_gettime(). Retrieved time: ", current_time
    except Exception,e:
      exception_string_list.append({'Server' : connected_server, 'Exception' : str(e), 'Traceback' : str(traceback.format_exc())})
      pass

  # Get the stop time 
  test_stop1 = getruntime()
  # Make sure that we don't fail too many times
  if len(times) < 4:  # more than one attempt failed
    notify_str += "failed to get ntp time via tcp at least twice in 5 attempts\n\n"
    notify_str += "Appending a list of all the exceptions returned and servers we attempted to connect to:\n\n"
    notify_str += str(exception_string_list)

  fail_test_str = ''

  # Find out the difference in time between the start time and end time of the test.
  #I get a case when times array is null
  if len(times) != 0:
    diff = max(times) - min(times)
    test_diff = test_stop1 - test_start

  # If the time difference was more then 10 seconds then there is a problem.
    if math.fabs(diff - test_diff) > 10:  
      fail_test_str += ' WARNING large descrepancy between tcp times. \nThe difference between tcp_time diff and the actual test diff is:    '+str(diff - test_diff)
      fail_test_str += "\n\nThe start time of test was: " + str(test_start) + ". The end time of test was: " + str(test_stop1)
      fail_test_str += "\n\nThe list of times returned by the tcp_server were: " + str(times)
      fail_test_str += "\n\nThe max time was: " + str(max(times)) + ". The min time was: " + str(min(times))
      fail_test_str += ". \n\nThe tcp diff time was: " + str(diff) + ". This time should have been less then: " + str(test_diff)
      fail_test_str += "\n\nThe servers we connected to are: " + str(server_list) 
      notify_str += fail_test_str
      print fail_test_str
    local_end_time = time.localtime()
    local_time_diff = time.mktime(local_end_time) - time.mktime(local_start_time)
    print "Local time diff: ", local_time_diff

  # Now do an ntp time test
  try:
    ntp.ntp_time_updatetime(12345)
    ntp_t = time_interface.time_gettime()
  except Exception,e:
    print "Failed to call ntp_time_updatetime(). Returned with exception: ", str(e)
    notify_str += "\nFailed to call ntp_time_updatetime(). Returned with exception: " + str(e)
  
  test_stop2 = getruntime()
  if len(times) !=0:
    diff = ntp_t - max(times)
    if diff > (8 + test_stop2 - test_stop1):
      exceedby = diff - (test_stop2-test_stop1)
      print "WARING large descrepancy between ntp and tcp times"
      notify_str += "WARNING large descrepancy between ntp and tcp time: " + str(exceedby)

  if notify_str != '':
    print notify_str, "time_monitor.py test failed"
    return True
  else:
    print "Finished running time_monitor.py..... Passed"
    return True


if __name__ == "__main__":
  checkTimeServersStatus()
  testTCP()



