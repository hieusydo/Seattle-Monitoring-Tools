# Distributed Monitoring Tools

### Design and Implementation Questions

#### Target to monitor:
- Seattle infrastructure server (which?)
  * services: advertising
  * other services?
- Seattle node
  * all vessels within a node
- Seattle services: 
_APIs_
  * file IO
  * network
  * timer
_Services and helper functions_
  * monitoring space
  * etc

#### What metrics:
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