# Distributed Monitoring Tools

### Design and Implementation Questions

#### Target to monitor
- Seattle infrastructure server (which?)
  * Advertising Service: check for free (unassigned) nodes' IP addresses
  * Software Updating Site: check if the update server is still up; if the version on the local machine is up-to-date
  * Zenodotus: check if the domain name registerd by a user is still up 
- Seattle node
  * Custom Installer Builder: check vesselinfo
  * all vessels within a node
- Seattle services: 
  * Integration Test Framework: sends notifications (gmail and irc) in case of critical failure
  * check disk space
  * check critical processes that should be running:
    * on Seattle server: advertiseserver.py
    * on Seattle ClearingHouse: transition\_donation\_to\_canonical.py, transition\_onepercentmanyevents\_to\_canonical.py, transition\_canonical\_to\_twopercent.py, transition\_twopercent\_to\_twopercent.py, check\_active\_db\_nodes.py', apache2, /usr/sbin/mysqld, backend\_daemon.py, lockserver\_daemon.py

#### What metrics
- Availability
  * how many nodes are available
- Performance: 
  * metrics: _ping_ to measure latency (what other metrics can also be used?)
  * implementation example: use _wget_ or _curl_ to query and download a webpage (clearinghouse); use _time_ function to register the time to get to the server --> plot the graph over time and analyze the results
- Usage
  * number of programs run and their status
  * disk capacity

#### Where should monitoring tool run
Differ in places and privileges

Consider: low hurdle & open for everyone to be able to just run the monitoring tool easily

- Server: different server machines: advertise service, clearinghouse server
- Node: node manager (already solved); 
  * run on a local machine -> show list of services available
- From third party service host on, ie, AWS
- Free monitoring tool on the web
- On a Seattle node

#### Notification
_Best ways to handle the monitoring information?_ (decided later)
- Email
- RSS
- Web page
- Text (Twilio API)
- etc

#### Who can run the tool
- Seattle server operator
- Seattle contributor 
- Seattle users 
- General public (limited monitoring capability, however)