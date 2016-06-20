# Distributed Monitoring Tools

### Table of Content
1. [Design and Implementation Questions](https://github.com/hieusydo/Seattle-Monitoring-Tools#1-design-and-implementation-questions)
  * [Target to monitor](https://github.com/hieusydo/Seattle-Monitoring-Tools#target-to-monitor)
  * [What metrics](https://github.com/hieusydo/Seattle-Monitoring-Tools#what-metrics)
  * [Where should the monitoring tools run](https://github.com/hieusydo/Seattle-Monitoring-Tools#where-should-monitoring-tool-run)
  * [Notification](https://github.com/hieusydo/Seattle-Monitoring-Tools#notification)
  * [Who can run the tool](https://github.com/hieusydo/Seattle-Monitoring-Tools#who-can-run-the-tool)
2. [Monitoring Pipeline](Monitoring-Pipeline)
  * [Overview](https://github.com/hieusydo/Seattle-Monitoring-Tools#overview)
  * [Node manager](https://github.com/hieusydo/Seattle-Monitoring-Tools#node-manager)
  * [Advertise Server](https://github.com/hieusydo/Seattle-Monitoring-Tools#advertise-server)
  * [Software Update Server](https://github.com/hieusydo/Seattle-Monitoring-Tools#software-update-server)
  * [Zenodotus](https://github.com/hieusydo/Seattle-Monitoring-Tools#zenodotus)

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

#### Where should the monitoring tools run
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
#### Overview

<img src="https://github.com/hieusydo/Seattle-Monitoring-Tools/blob/master/img/monitor-pipline.png" width="750" />

#### Node manager
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

#### Advertise server
- Are the critical processes running? (determine the role of these processes)
    * on Seattle server: advertiseserver.py
    * on Seattle ClearingHouse: 
      * transition\_donation\_to\_canonical.py, transition\_onepercentmanyevents\_to\_canonical.py, transition\_canonical\_to\_twopercent.py, transition\_twopercent\_to\_twopercent.py, check\_active\_db\_nodes.py, 
      * apache2
      * /usr/sbin/mysqld
      * backend\_daemon.py, lockserver\_daemon.py
	* -> notify the admins if critical processes are down

#### Software Update Server
- Is _softwareupdater.py_ running? 
  * Yes: nothing
  * No: notify sysadmins
- Is the software update service set up on a vessel? Check the public keys
  * Yes: nothing, check if the update service is running
  * No: notify users -> set up the update service

#### Zenodotus
- Is _zenodotus\_advertise.repy_ running? 
  * No: notify sysadmins
  * Yes: return the node info associated with a domain name