# Distributed Monitoring Tools

### Table of Content
1. [Design and Implementation Questions](Design-and-Implementation-Questions)
2. [Monitoring Pipeline](Monitoring-Pipeline)

### 1. Design and Implementation Questions

#### Target to monitor
- Seattle infrastructure server:
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

### 2. Monitoring Pipeline
__Overview__

![graph](img/monitor-pipeline.png)

__Node manager__
- Is there enough diskspace on a node? 
  * Yes: nothing 
  * No: notify the node owner and the experiment manager
- Is the key/value pair valid? Look up the users' public keys in the Advertise Server -> are the users assigned a node? 
  * Yes: return a list of IPs of the vessels
  * No: determine which case? 
    * Users have not acquire resources on ClearingHouse -> notify users
    * The Advertise Server is corrupted/compromised -> notify sysadmins
- Get info: 
  * each node: number of vessels
  * each vessel: IP addresses, status (started, stopped, combined, split, changed)

__Advertise server__
- Are the critical processes running? (determine the role of these processes)
    * on Seattle server: advertiseserver.py
    * on Seattle ClearingHouse: 
      * transition\_donation\_to\_canonical.py, transition\_onepercentmanyevents\_to\_canonical.py, transition\_canonical\_to\_twopercent.py, transition\_twopercent\_to\_twopercent.py, check\_active\_db\_nodes.py, 
      * apache2
      * /usr/sbin/mysqld
      * backend\_daemon.py, lockserver\_daemon.py
	* -> notify the admins if critical processes are down

__Software Update Server__
- Is _softwareupdater.py_ running? 
  * Yes: nothing
  * No: notify sysadmins
- Is the software update service set up on a vessel? Check the public keys
  * Yes: nothing, check if the update service is running
  * No: notify users -> set up the update service

__Zenodotus__
- Is _zenodotus\_advertise.repy_ running? 
  * No: notify sysadmins
  * Yes: return the node info associated with a domain name