# CSE 160 – Lecture 07: Bridging LANs

---

## 1. Motivation: Scaling Beyond a Single LAN

- **LAN limits:**  
  - Distance, number of nodes, performance.  
  - CSMA/CD and wireless contention constrain scalability.  
- **Solution:** Interconnect LANs using **switches**.  
- Leads to an **extended LAN** with multiple collision domains.  

---

## 2. Switching (a.k.a. Bridging)

- **Definition:** Transferring a packet from one LAN to another LAN.  
- **Bridges:**  
  - Receive frames on one LAN, forward to another.  
  - Each LAN remains its own collision domain.  
  - Operates at the **Link Layer (Data Link sublayer)**.  

---

## 3. LAN Switches

- Modern Ethernet uses **switches**, not shared cables.  
- **Switched Ethernet:**  
  - Hosts wired via twisted pair to a switch.  
  - Centralized wiring location (e.g., **IDF closets** in enterprise networks).  
  - More reliable (wire cut ≠ total failure).  
- **Inside a switch:**  
  - **Fabric** connects input ports to output ports.  
  - Supports **full-duplex** (send/receive simultaneously).  
  - Requires **buffers** for congestion → risk of frame loss under overload.  

---

## 4. Switch Forwarding & Backward Learning

- Switch must find output port for destination **MAC address**.  
- Hosts can move → must avoid static configs.  

### Backward Learning
1. Switch observes **source address** of incoming frames.  
2. Learns which port leads to that host, adds entry to look-up table (**port/address table**).  
3. If destination unknown → **floods** frame to all ports.  
4. Entries are **aged** for robustness (topology changes).  

- **Dynamic systems are essential**: switches must adapt automatically.  
- **Key point:** Communication is always between **hosts**, not switches.  

---

## 5. Loops and the Spanning Tree Protocol (STP)

- **Problem:** Loops in switch topology cause **broadcast storms** and infinite forwarding.  
- **Goal:** Plug-and-play robustness without host changes.  
- **Solution:** Switches collectively compute a **Spanning Tree (ST)**.  

### Spanning Tree Algorithm (Radia Perlman, 1985)
- **Steps:**  
  1. Elect a **root bridge** (lowest ID).  
  2. Compute shortest paths from all switches to root.  
  3. Disable non-tree links (turn off some ports).  
- **Mechanism:**  
  - Switches exchange **configuration messages**: (sender ID, root ID, distance in hops).  
  - Updates propagate until convergence.  
  - Root bridge continues sending periodic updates.  
- **Dynamic adaptation:** If topology changes (e.g., root fails), switches recompute tree.  

---

## 6. Practical Notes

- **IDFs and BDFs (Intermediate/Building Distribution Frames):** Real-world locations where switches reside.  
- **Design principle:**  
  - First design a solution that works (correctness > performance).  
  - Then optimize for performance later.  
- **Switching limits:**  
  - High load --> large forwarding tables.  
  - Uncontrolled broadcast domains.  
  - Slow reconfiguration of spanning tree.  
  - Poor at interconnecting heterogeneous LANs → need **routing (Network Layer)**.  

---

## Summary

- Scaling LANs requires **switches** instead of shared media.  
- **Backward learning** enables switches to dynamically map MACs to ports.  
- **Loops** cause major issues → solved by the **Spanning Tree Protocol**.  
- Switches provide scalability and reliability but have limitations at large scale.  
- Routing (next topic) is required for true wide-area scalability. 

---
