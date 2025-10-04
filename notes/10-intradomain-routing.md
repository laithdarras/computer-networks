# Lecture 10 – Intra-Domain Routing

---

## Overview

**Focus:** How routing works within a single domain (e.g., a campus or enterprise network).

**Topics Covered:**
- **Distance Vector (DV)** routing – basis for RIP  
- **Equal-Cost Multi-Path (ECMP)** routing  
- **Dynamic Host Configuration Protocol (DHCP)**  
- **Address Resolution Protocol (ARP)**  
- **IPv6**

---

## Distance Vector (DV) Routing

**Goal:** Compute shortest paths in a distributed network where each node only knows the cost to its immediate neighbors.

### Key Concepts
- **DV needs to know its neighbors.**
- Each node maintains a **vector (array) of distances** (costs) and next hops to all destinations.
- Based on the **Bellman-Ford algorithm**.
- Used by **RIP** (Routing Information Protocol).
- Converges to correct routes but is **slow** and can form routing loops.

### Algorithm Overview
1. Initialize distances to neighbors (direct costs); others set to ∞.  
2. Periodically share your distance vector with neighbors.  
3. On receiving a neighbor’s vector, update:
```txt
cost_to_dest = neighbor_cost + neighbor_vector[dest]
if cost_to_dest < current_cost:
update next_hop and cost
```
4. Repeat until no more updates (convergence).

**Properties:**
- Distributed and iterative  
- Adapts to topology changes  
- Vulnerable to certain failure modes (e.g., count-to-infinity)

---

## Distance Vector Dynamics

- **Adding routes:** News travels one hop per exchange.
- **Removing routes:** If a node fails, others gradually forget it.
- **Problem:** “**Count-to-infinity**” loops occur when nodes mislead each other after a failure.

### Example:
```txt
A ↔ B ↔ Internet

B’s direct link to Internet fails.

B hears from A: “I can reach Internet in 2 hops.”

B updates to 3 hops (via A) → wrong path!

A hears back from B, updates to 4 hops...

Cycle continues → infinite increase.
```

---

## Preventing Count-to-Infinity

### Split Horizon
- Don’t advertise a route back to the neighbor that provided it.

### Split Horizon with Poison Reverse
- Advertise the route back with **infinite cost** to ensure it’s not reused.

Even with these, DV can still fail in complex topologies.

---

## Routing Information Protocol (RIP)

**Type:** Distance Vector (DV) protocol  
**Metric:** Hop count  
**Max hops:** 15 (16 = ∞)
> Only for small to medium-sized networks

### Operation
- Routers broadcast routing tables every **30 seconds** using **UDP**.  
- Triggered updates on link failure.  
- Route timeout = **180 seconds**.  
- **Split Horizon + Poison Reverse** used to limit loops.

**Specifications:**
- **RIPv1:** RFC 1058  
- **RIPv2:** RFC 1388 (adds authentication)

### Characteristics
- Simple and widely supported  
- Suitable for **small to medium networks** (e.g., campus, ISP)  
- Poor scalability for Internet-scale routing
> Next topic will cover planetary-scale routing :)

---

## DV vs. Link-State (LS) Routing

| Property | Distance Vector | Link-State |
|-----------|-----------------|-------------|
| Algorithm | Bellman-Ford | Dijkstra |
| Information Sharing | Neighbors only | Global flooding |
| Convergence | Slow | Fast |
| Complexity | Low | Higher |
| Scalability | Excellent | Moderate |
| Example | RIP | OSPF |

**Mnemonic:**  
- DV → “Tell your neighbors about the world.”  
- LS → “Tell the world about your neighbors.”

---

## Equal-Cost Multi-Path (ECMP) Routing

**Idea:** Allow traffic to use **multiple paths** of equal cost to the same destination.

### Why ECMP?
- Improves performance and reliability.  
- Balances load across redundant links.

### Mechanism
- Keep all equal-cost paths found by Dijkstra or DV.  
- The **source tree** becomes a **Directed Acyclic Graph (DAG)** — multiple next hops.

**Example:**  
```txt
A → B → E (cost 8)
A → B → C → E (cost 8)
A → B → C → D → E (cost 8)
All are valid ECMP paths.
```

### Forwarding with ECMP
- Random next-hop selection → good load balance, but adds jitter.  
- **Flow-based forwarding:**  
  - Each source-destination pair (flow) consistently uses the same path.  
  - Reduces jitter while maintaining load balance across flows.

---

## IP Helpers – DHCP and ARP

### DHCP – Dynamic Host Configuration Protocol
**Purpose:** Automatically assign IP addresses and configuration info to hosts.

**Layer:** Network Layer  
**Transport:** UDP (Ports 67/68)

**Provides:**
- IP address lease  
- Subnet mask  
- Default gateway (router)  
- DNS and time servers  

#### Message Flow (DORA)
```txt
Client → DISCOVER (broadcast: "Who can give me an IP?")
Server → OFFER (offers an IP)
Client → REQUEST (accepts offer)
Server → ACK (confirms assignment)
```

**Renewal:**  
Client periodically sends `REQUEST → ACK` to extend lease.

---

### ARP – Address Resolution Protocol
**Purpose:** Map IP addresses to **Link Layer (MAC)** addresses.  
**Layer:** Link Layer  

#### Operation
1. Node broadcasts: “Who has IP X.X.X.X?”  
2. Target replies with: “I do → MAC address.”  

**ARP Table:** Cached mappings of IP addr ↔ MAC addr pairs.  
**Example:**  
`192.168.1.10 → 00:1A:2B:3C:4D:5E`

**Relationship:**
- **ARP:** Link Layer  
- **DHCP:** Network Layer  

---

## 10. IPv6 – The Future of IP

### Motivation
- **IPv4 exhaustion:** 32-bit addresses (~4.3 billion) fully allocated by 2015.  
- IPv6 provides **128-bit addresses**, enabling enormous address space.

### IPv6 Address Format
- 8 groups of 4 hexadecimal digits (16 bits each).  
- Leading zeros can be omitted; groups of zeros replaced with `::`.

**Example:**
```txt
Full: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
Short: 2001:db8:85a3::8a2e:370:7334
```

### Key Improvements
- **Simplified header** for faster processing  
- **Flow labels** for QoS and traffic grouping  
- Built-in support for **multicasting**, **mobility**, and **security**  
- **Dual stack deployment** – IPv4 and IPv6 coexist  
- **Translators** and **tunnels** help during transition

---

## Summary

- **Distance Vector Routing** uses the Bellman-Ford algorithm; nodes share distance info with neighbors.  
- **RIP** is a DV protocol using hop count; limited to small networks (15-hop max).  
- **ECMP** allows multiple equal-cost paths for redundancy and load balancing.  
- **DHCP** (Network Layer) assigns IPs; **ARP** (Link Layer) maps IP → MAC.  
- **IPv6** (128-bit) resolves IPv4 exhaustion and introduces improved efficiency and scalability.
