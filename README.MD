# Seatte Monitoring Tools

<!-- ### Table of Content
1. [Design and Implementation Questions](https://github.com/hieusydo/Seattle-Monitoring-Tools#1-design-and-implementation-questions)
  * [Target to monitor](https://github.com/hieusydo/Seattle-Monitoring-Tools#target-to-monitor)
  * [What metrics](https://github.com/hieusydo/Seattle-Monitoring-Tools#what-metrics)
-->

## Design and Implementation Overview

### 1. Target to monitor
- Advertising Service: central, central_v2, udpcentral
- Software Updater
- Zenodotus 
- Custom Installer Builder
- Targets already monitored: 
  * disk space (```monitor_disk.py```)
  * resource violation (```nanny.py```)
  * vessel info (checked in the installer)

### 2. How to monitor
To consider: 
- metrics: availability, performance, usage, etc.
- location: local machine, node manager, Seattle server, Clearinghouse server, etc.
- users: server operator, contributor, Seattle users, general public
- notification

#### Advertising Service
- central 
  * check status of ```advertiseserver.poly.edu``` (port 10102) by first validating the hostname and then trying to open a connection to the hostname
    * alive
    * dead -> why? _NetworkAddressError_, _ConnectionRefusedError_, _TimeoutError_, _InternetConnectivityError_
  * announce and lookup a test _<key, value>_ pair
- central_v2
  * check status of ```advertiseserver_v2.poly.edu``` (port 10102): same as with central
  * __[PROBLEM]__ attempts to announce a pair raises ```Exception (with class '.SocketTimeoutError'): recv() timed out!!```, while connection to ```advertiseserver_v2.poly.edu``` is successful. [Issue #182](https://github.com/SeattleTestbed/seattlelib_v2/issues/182)
- udpcentral
  * check if UDP server is listening 
  * announce and lookup test


#### Software Updater

#### Zenodotus 

#### Custom Installer Builder

<!-- ### Monitoring Pipeline

<img src="https://github.com/hieusydo/Seattle-Monitoring-Tools/blob/master/img/monitor-pipline.png" width="750" />
 -->