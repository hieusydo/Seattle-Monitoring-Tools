# Distributed Monitoring Tool

### Design and Implementation Questions
Target to monitor: 
- Seattle infrastructure server (which?)
  * experiment manager (which handles vessels across computers)
- Seattle node
  * all vessels within a node
- Seattle services (which?) - APIs
  * file IO
  * network
  * timer
- etc

What metrics: 
- Availability
  * how many nodes are available
- Performance (w/ respect to what?)
  * performance test implementation
- Usage
  * number of programs run and their status
- etc

Where should monitoring tool run 
- Server: experiment manager
- Node: sandbox component and node manager 
- etc

Notification 
- Email
- RSS
- Web page
- Text (Twilio API)
- etc

Who can run the tool 
- Seattle server operator
- Seattle contributor 
- etc