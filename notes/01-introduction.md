# Lecture 01: Introduction to Computer Networks

---

## Administrative Notes
- Course page: CatCourses (all materials posted there).  
- **Projects:** 55% of grade (4 projects).  
  - Build a networking stack using **TinyOS** and **TOSSIM**.  
  - Projects are cumulative → falling behind early creates a cascade effect.  
  - Start coding immediately and dedicate consistent time.  
- **Homework:** ~10% of grade. Essential for preparing for exams.  
- **Reading:** Chapters must be done *before lecture* to keep up.  
- **Environment:** TinyOS has no dynamic memory allocation (all static). Data structures must be pre-allocated.  
- **Teams:** Projects are in pairs — choose a competent partner.  

---

## Course Goals
- Understand how to **design and build distributed computer networks**.  
- Learn **fundamental problems** in networking: reliability, scalability, congestion, addressing, security.  
- Explore **design principles of proven value**.  
- Learn about **protocols, layering, and implementations** that underpin the Internet.  
- This is a **systems course**, not about signals or hardware.  

---

## Why Study Networks?
- **Curiosity:** Understand what happens when you browse the web.  
- **Impact:** The Internet drives societal and economic change.  
- **Careers:** Networking knowledge is fundamental in industry.  

---

## Historical Context
- **ARPANET (1969–1971):** The origin of packet-switched networks.  
- **Internet (2021):** A global institution connecting billions, spanning work, home, and mobile contexts.  

---

## Networking Fundamentals
### Intellectual Interest
- **Reliability:**  
  - Issues: failures, corruption, dropped/out-of-order packets.  
  - Solutions: error detection/correction, routing around failures.  
- **Scalability:**  
  - Addressing and naming.  
  - Protocol layering.  
- **Resource Allocation:**  
  - Bandwidth sharing, multiple access, congestion control.  
- **Security:**  
  - Confidentiality, authentication, resilience against threats.  

### Reinvention
- Internet evolves with technology trends:  
  - Web → CDNs  
  - Media sharing → Peer-to-peer  
  - Mobile devices → Wireless protocols  
  - Address space growth → IPv6  
- Fundamentals remain constant even as technologies shift.  

---

## Components of a Network
- **Application (App/User):** Uses the network (e.g., Skype, Amazon).  
- **Host (End-System):** Supports applications (e.g., laptops, phones).  
- **Router/Switch:** Relays messages across links.  
- **Link/Channel:** Connects nodes (wired, wireless, satellite).  

### Types of Links
- **Full-duplex:** Bidirectional simultaneously.  
- **Half-duplex:** Bidirectional, but not simultaneous.  
- **Simplex:** Unidirectional.  
- **Wireless:** Broadcast to all nodes in range → potential inefficiency.  

### Network Scales
- PAN (Bluetooth) → LAN (Wi-Fi, Ethernet) → MAN (Cable, DSL) → WAN (ISP) → Internet.  

---

## Characteristics of Large-Scale Networks
- **Intrinsic Unreliability:**  
  - Packets may be lost, duplicated, corrupted, reordered, intercepted, or modified.  
- **Distributed:**  
  - Independent failures and administrative domains.  
  - Leslie Lamport: *“A distributed system is one in which I can’t do my work because some computer I’ve never heard of has failed.”*  
- **Heterogeneous:**  
  - Different devices and technologies working together.  
  - Drives innovation and global scale.  

---

## Key Interfaces
1. **App ↔ Network:** How applications use the network (e.g., **sockets**).  
2. **Network ↔ Network:** How nodes cooperate (e.g., **traceroute** reveals path).

---

## Applications of Networks
- **User Communication:** VoIP, video conferencing, messaging, social networking.  
  - Metric: **low latency**.  
- **Content Delivery:** Videos, apps, software updates.  
  - Metric: **bandwidth / throughput efficiency**.  
- **Resource Sharing:** Cloud computing, search indices, printers.  
  - Metric: **cost-effective multiplexing**.  

---

## Multiplexing
### Static Multiplexing
- **Frequency Division Multiplexing (FDM):** Different frequency bands.  
- **Time Division Multiplexing (TDM):** Timeslots assigned to users.  
- **Problem:** Inefficient for bursty data traffic (peak >> average usage).  

### Statistical Multiplexing
- **On-demand sharing** of resources, based on actual usage.  
- Well-suited for data networks with bursty traffic.  
- Gains efficiency by oversubscribing capacity (probability of overload is low).  
- **Tradeoff:** occasional congestion / queuing delays.  

---

## Summary / Takeaways
- Networking is about **reliability, scalability, efficiency, and security** in connecting distributed systems.  
- The **Internet’s design principles** (layering, addressing, error control, multiplexing) allow it to scale despite unreliability.  
- **TinyOS + TOSSIM projects** are central: start early, code consistently, and understand nesC.  
- **Homework + reading** are vital for exams.  
- **Multiplexing** is the first major technical concept: static (TDM/FDM) vs. statistical (dynamic, efficient).  
