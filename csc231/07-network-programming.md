# Network programming



## 1. In the beginning

- 1966: Advanced Research Projects Agency Network (ARPANET) - DOD 
- 1969: Four sites:
  - SRI: Stanford Research Institutte
  - Utah: University of Utah
  - UCLA
  - UCSB

<img src="../fig/07-networks/01.png" alt="scientific debugging" style="height:400px">

- 1977: East and West
  - MITRE Corporation: managed federally funded research and development centers (FFRDC) for
  a number of U.S. agencies (DOD, FAA, IRS, DVA, DHS, AO, CMMS, NIST)
  - BNN: now a subsidiary of Raytheon 
  - Burroughs: now part of Unisys

<img src="../fig/07-networks/02.png" alt="scientific debugging" style="height:400px">




## 2. Now

- 2012: the Carna Botnet was unleashed.
  - An ethical hacking experiment in 2012 that used Nmap Scripting Engine (NSE) to scan for random 
  devices with default telnet login username and password. 
  - Over 100,000 devices had these features and could easily be accessed. 
  - A spider-like crawling approach was used to have the vulnerable devices to scan for other vulnerable
  devices. 
  - In the end, a total of 420,000 devices were assisting the internet search, and of the 
  4.3 billion IP addresses possible, the Carna Botnet found 1.3 billion.
  - What came from the Carna Botnet was a **massive census of the internet** in 2012.

<img src="../fig/07-networks/03.gif" alt="carna botnet" style="height:800px">




## 3. A client-server transaction

- Most network applications are based on the client-server model:
  - A server process and one or more client processes
  - Server manages some resource
  - Server provides service by manipulating resource for clients
  - Server activated by request from client (vending machine analogy)
- Clients and servers are processes running on hosts (can be the same or 
different hosts).

<img src="../fig/07-networks/04.png" alt="scientific debugging" style="height:400px">




## 4. Computer networks

- A network is a hierarchical system of boxes and wires organized by geographical 
proximity
  - BAN (Body Area Network) spans devices carried / worn on body
  - SAN* (System Area Network) spans cluster or machine room
  - LAN (Local Area Network)  spans a building or campus
  - WAN (Wide Area Network) spans country or world
- An internetwork (internet) is an interconnected set of networks




## 5. From the ground up

- Lowest level: Ethernet segments 
  - consists of a collection of hosts connected by wires (twisted pairs) to a 
  hub (replaced by switches and routers today).
  - Spans room or floor in a building
  - Each Ethernet adapter has a unique 48-bit address called MAC address: 00:16:ea:e3:54:e6
  - Hosts send bits to any other host in chunks called frames
  - Hub copies each bit from each port to every other port
    - Every host sees every bit
- Next level: bridged Ethernet segments. 
  - Spans building or campus
  - Bridges cleverly learn which hosts are reachable from which ports and then 
  selectively copy frames from port to port.
- Next level: Internet
  - Multiple incompatible LANs can be physically connected by specialized computers called 
  routers.
  - The connected networks are called an internet (lower case)




## 6. Logical structure of an internet

- Ad hoc interconnection of networks
 - No particular topology
  - Vastly different router & link capacities
- Send packets from source to destination by hopping through networks
  - Router forms bridge from one network to another
  - Different packets may take different routes

<img src="../fig/07-networks/05.png" alt="Logical structure of an internet" style="height:400px">




## 7. The notion of an internet protocol

- How is it possible to send bits across incompatible LANs and WANs?
- Solution:  protocol software running on each host and router 
  - Protocol is a set of rules that governs how hosts and routers should cooperate when 
  they transfer data from network to network. 
  - Smooths out the differences between the different networks




## 8. What does an internet protocol do?

- Provides a naming scheme
  - An internet protocol defines a uniform format for **host addresses**.
  - Each host (and router) is assigned at least one of these internet addresses that uniquely 
  identifies it.
- Provides a delivery mechanism
  - An internet protocol defines a standard transfer unit (packet)
  - Packet consists of header and payload:
    - Header: contains info such as packet size, source and destination addresses
    - Payload: contains data bits sent from source host




## 9. Transferring internet data via encapsulation

- Ad hoc interconnection of networks
 - No particular topology
  - Vastly different router & link capacities
- Send packets from source to destination by hopping through networks
  - Router forms bridge from one network to another
  - Different packets may take different routes

<img src="../fig/07-networks/06.png" alt="data encapsulation" style="height:500px">


## 10. A trip down memory lane

<iframe width="560" height="315" src="https://www.youtube.com/embed/7Zf203Vmbig" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




## 11. Other issues

- We are glossing over a number of important questions:
  - What if different networks have different maximum frame sizes? (segmentation)
  - How do routers know where to forward frames?
  - How are routers informed when the network topology changes?
  - What if packets get lost?
- These (and other) questions are addressed by the area of  systems known as 
**computer networking**




## 12. Global IP Internet (upper case)

- Most famous example of an internet
- Based on the TCP/IP protocol family
  - IP (Internet Protocol)
    - Provides `basic naming scheme` and unreliable `delivery capability` of packets 
    (datagrams) from `host-to-host`
  - UDP (Unreliable Datagram Protocol)
    - Uses IP to provide `unreliable` datagram delivery from `process-to-process`.
  - TCP (Transmission Control Protocol)
    - Uses IP to provide `reliable` byte streams from `process-to-process` over 
    `connections`.
- Accessed via a mix of Unix file I/O and functions from the `sockets interface`.




## 13. Hardware and software organization of an Internet Application

<img src="../fig/07-networks/07.png" alt="Internet application" style="height:400px">




## 14. A programmer's view of the Internet

- Hosts are mapped to a set of 32-bit `IP addresses` (lookout for IPv6 in the future)
  - 128.2.203.179
  - 127.0.0.1 (always localhost)
- The set of IP addresses is mapped to a set of identifiers called Internet domain 
names: 144.26.2.9 is mapped to  www.wcupa.edu 
- A process on one Internet host can communicate with a process on another Internet host over a `connection`.




## 15. IP addresses

- 32-bit IP addresses are stored in an `IP address struct`.
  - IP addresses are always stored in memory in `network byte order` (**big-endian byte order**)
  - True in general for any integer transferred in a packet header from one machine to another.
    - E.g., the port number used to identify an Internet connection

~~~
/* Internet address structure */
struct in_addr {
  uint32_t s_addr; /* network byte order (big-endian) */
};
~~~


- Dotted decimal notation
  - By convention, each byte in a 32-bit IP address is represented by its 
  decimal value and separated by a period.
  - IP address: 0x8002C2F2 = 128.2.194.242
- Use `getaddrinfo` and `getnameinfo` functions (described later) to convert 
between IP addresses and dotted decimal format.
- Domain Naming System (DNS)
  - The Internet maintains a mapping between IP addresses and domain names in a 
  huge worldwide distributed database called DNS.
  - Conceptually, programmers can view the DNS database as a collection of millions 
  of host entries.
    - Each host entry defines the mapping between a set of domain names and IP
    addresses.
    - In a mathematical sense, a host entry is an equivalence class of domain names 
    and IP addresses.

~~~
$ nslookup localhost
$ hostname -f
$ nslookup www.facebook.com
$ nslookup www.twitter.com
~~~


<img src="../fig/07-networks/08.png" alt="nslookup" style="height:400px">




## 16. Internet connections

- Clients and servers communicate by sending streams of bytes over `connections`. 
Each connection is:
  - `Point-to-point`: connects a pair of processes.
  - `Full-duplex`: data can flow in both directions at the same time,
  - `Reliable`: stream of bytes sent by the source is eventually received by 
  the destination in the same order it was sent. 
- A `socket` is an endpoint of a connection
  - `Socket address` is an **IPaddress:port**  pair
- A `port` is a 16-bit integer that identifies a process:
  - `Ephemeral port`: Assigned automatically by  client kernel when client makes 
  a connection request.
  - `Well-known port`: Associated with some `service` provided by a server (e.g., port 
  80 is associated with Web servers)




## 17. Well known service names and ports

- Popular services have permanently assigned well-known ports and 
corresponding well-known service names:
  - echo servers: `echo  7`
  - ftp servers: `ftp 21`
  - ssh servers: `ssh 22`
  - email servers: `smtp 25`
  - Web servers: `http 80`
- Mappings between well-known ports and service names is contained in the 
file `/etc/services` on each Linux machine. 




## 18. Socket interface

- Set of system-level functions used in conjunction with Unix I/O to 
build network applications. 
- Created in the early 80’s as part of the original Berkeley distribution 
of Unix that contained an early version of the Internet protocols.
- Available on all modern systems: Unix variants, Windows, OS X, IOS, Android, ARM
- What is a socket?
  - To the kernel, a socket is an endpoint of communication
  - To an application, a socket is a file descriptor that lets the application 
  read/write from/to the network.
  - Remember: All Unix I/O devices, including networks, are modeled as files.
- Clients and servers communicate with each other by reading from and writing to 
socket descriptors.
- The main distinction between regular file I/O and socket I/O is how the 
application **opens** the socket descriptors.




## 19. Hands on: client/server network programming

- Create a directory called `07-networks`.
- Create the following files `server.c` and `client.c`.
 
<script src="https://gist.github.com/linhbngo/d1e9336a82632c528ea797210ed0f553.js?file=server.c"></script>
<script src="https://gist.github.com/linhbngo/d1e9336a82632c528ea797210ed0f553.js?file=client.c"></script>
>
- Compile the two programs. 
- Open a dual panel tmux and run `server` and `client` on each panel. 
- Type strings into `client` and observe how it shows up on `server`. 
- Type a corresponding string on `server` and observe how it shows on `client`. 
- Type `exit` on each side to stop `client` and `server`. 

~~~
$ gcc -o server server.c
$ gcc -o client client.c
~~~

<img src="../fig/07-networks/09.png" alt="server/client" style="height:400px">


