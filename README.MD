# Seatte Monitoring Tools

<!-- ### Table of Content
1. [Design and Implementation Questions](https://github.com/hieusydo/Seattle-Monitoring-Tools#1-design-and-implementation-questions)
  * [Target to monitor](https://github.com/hieusydo/Seattle-Monitoring-Tools#target-to-monitor)
  * [What metrics](https://github.com/hieusydo/Seattle-Monitoring-Tools#what-metrics)
-->

## Design and Implementation Overview

### 1. Target to monitor
- Advertising Service: central, central_v2, udp
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
- central_v2
- udp

#### Software Updater

#### Zenodotus 

#### Custom Installer Builder

<!-- ### Monitoring Pipeline

<img src="https://github.com/hieusydo/Seattle-Monitoring-Tools/blob/master/img/monitor-pipline.png" width="750" />
 -->