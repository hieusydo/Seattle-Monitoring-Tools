'''
Author: 
Hieu Do 
hieu.do@nyu.edu

Start Date: July 1, 2016

Description: 
Check the status of the UDP advertise server

Usage: 
python udpadvertise_monitor.py

'''

import os
import sys
import socket
import subprocess
# import send_gmail
# import irc_seattlebot
# import integrationtestlib

def main():
  servername = "udpadvertiseserver.poly.edu"
  portrange = "20-30"
  command = "nc -v -u -z -w 3 " + servername + " " + portrange
  # print(command)
  try:
    relevant_processes, command_error = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate() 
  except:
    integrationtestlib.handle_exception("Failed to run command: "+command)
    sys.exit(1)  
  print(relevant_processes)
  print(command_error)

if __name__ == '__main__':
  main()