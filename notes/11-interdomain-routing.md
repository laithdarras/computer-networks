# Lecture 11 – Inter-Domain Routing 

---

## 1. Overview

**Focus:** How the Internet scales routing across global networks.

**Core Topics:**
- **Hierarchical Routing**
- **Autonomous Systems (AS)**
- **Border Gateway Protocol (BGP)**
- **Routing Policies** (transit, peering)
- **Internet Exchange Points (IXPs)**
- **Multi-homing** and **network neutrality**

---

## 2. Motivation: Scaling Routing to Internet Size

### Why Scaling Matters
- The Internet contains **1.75B+ hosts** and **113K+ ASes** (as of 2023).  
- Global routing must balance **connectivity, scalability, and policy control**.
- Key principle: **Don’t aim for perfect optimality — aim for scalability.**

### Problems with Growth
1. **Forwarding tables grow** → increased memory and lookup time.  
2. **Routing messages grow** → more control-plane traffic.  
3. **Computation grows** → shortest-path algorithms scale poorly with size.

---

## 3. Hierarchical Routing

### Concept
- Divide the network into **regions** (e.g., ISPs, ASes).
- **Route to regions** instead of individual nodes.  
- Hides internal details of a region from others.

### Benefits
- Reduces routing table size and message overhead.  
- Decreases computation complexity.  
- Enables hierarchical structure for scalability.  

### Trade-off
- May produce **longer, suboptimal paths** (acceptable for scalability).
```text
Route to Region → Route to Prefix → Route to Host
```

---

## 4. The Structure of the Internet

### Hierarchical Tiers
| Tier | Description | Examples |
|------|--------------|-----------|
| **Tier 1** | Global backbones interconnecting continents | AT&T, NTT, Sprint |
| **Tier 2** | National ISPs connecting local regions | Telecom Argentina |
| **Tier 3** | Local ISPs serving cities or neighborhoods | Regional ISPs |

### Autonomous Systems (AS)
- Each AS represents a **network operated under a single administrative domain**.
- ASes interconnect to form the Internet’s global routing fabric.
- **AS Number (ASN):** unique identifier assigned by IANA regional registries (APNIC, ARIN, RIPE, etc.).

---

## 5. Inter-Domain vs Intra-Domain Routing

| Type | Scope | Example Protocols | Managed By |
|------|--------|------------------|-------------|
| **Intra-Domain (IGP)** | Within an AS | RIP, OSPF | Internal administrators |
| **Inter-Domain (EGP)** | Between ASes | BGP | AS border routers |

**Goal:** Inter-domain routing connects multiple autonomous systems while respecting **policy and autonomy**.

---

## 6. Border Gateway Protocol (BGP)

### Overview
- **Primary inter-domain routing protocol** of the Internet.  
- Type: **Path Vector Protocol** (extension of Distance Vector).  
- Operates over **TCP** (reliable transport, port 179).  

### Characteristics
- Exchanges **reachability** (not cost-based) information.
- Each route announcement includes:
  - **IP prefix** (destination block)
  - **Path vector** (AS sequence)
  - **Next hop**
```text
Announcement: [Prefix P, Path = (AS1, AS3, AS7), Next Hop = R3]
```
- Shorter paths are preferred, but only among **policy-compliant** options.

### Operation Flow
1. **Border routers** advertise aggregated internal routes to neighbors.  
2. **ASes** manually configure filters and policies.  
3. **Announcements** propagate in the opposite direction of traffic flow.  
4. **Routers** select best path based on local policies (not always shortest).

### Convergence
- BGP may experience **slow convergence** (similar to count-to-infinity).  
- Multiple invalid paths can be explored before stabilization.

---

## 7. Routing Policies

Routing is dominated by **business, administrative, and security constraints** — not purely technical ones.

### Common Policy Types

#### 1. **Transit**
- **Customer–Provider relationship.**
- ISP provides full connectivity to/from the Internet.
- Customer pays ISP for global reachability.
```text
Customer ↔ ISP ↔ Rest of Internet
```

#### 2. **Peer**
- **Mutual exchange** of customer traffic between ISPs.
- Free bilateral relationship (no payment).
- Each side carries only customer traffic, not third-party transit.
```text
ISP A ↔ ISP B (exchange traffic for their own customers only)
```

#### Simplified Roles
- **Providers** sell transit to **customers**.  
- **Peers** exchange customer routes directly.  
- **Tier-1s** peer with each other to maintain global reachability.

---

## 8. Policy Constraints 

| Category | Description | Example |
|-----------|--------------|----------|
| **Economic** | Who pays for bandwidth or transit? | Longer, cheaper paths preferred |
| **Administrative** | Allowed routes per agreement | Route hiding, selective advertisement |
| **Security** | Trust and data privacy concerns | Avoid paths through untrusted ASes |

**Result:** The “best” path = shortest among those allowed by policy.

### Security Example
> An AS may choose a longer path to avoid traversing an untrusted operator performing traffic inspection (e.g., AS B).

---

## 9. Internet Exchange Points (IXPs)

### Purpose
- Provide a **neutral interconnection point** where multiple ASes can connect easily.  
- Located in **data centers** — physically central, with redundant power and cooling.
> It's just like a LAN party! 

### Benefits
- Avoids the cost and complexity of direct point-to-point links.  
- Simplifies peering between many networks via a shared **Layer 2 fabric**.  
- Enables dynamic policy changes without physical rewiring.

### Economic Role
- ASes pay a monthly fee based on connection speed.  
- IXPs must remain **neutral** (no preferential treatment).

**Insight:**  
The number of IXPs correlates strongly with a country's **telecommunication development**.

---

## 10. Multi-Homing

### Concept
- A network connects to **multiple upstream providers** for redundancy and load balancing.

### Benefits
- Reliability and fault tolerance.  
- Better control over **outgoing** traffic (path selection).  
- **Less control** over incoming paths — depends on how other ASes route traffic to you.
```text
Customer
↕
Provider A Provider B
```

---

## 11. Network Neutrality

### Definition
All Internet traffic should be treated equally — without prioritizing or discriminating based on source, content, or application.

### Violations
- **Preferential treatment:** faster service for certain content.  
- **Traffic blocking:** slower or no service for disfavored content.  

### Real-World Examples
- ISPs prioritizing traffic from revenue-sharing partners.  
- Blocking or slowing peer-to-peer (P2P) traffic.  
- Favoring **asymmetric** (download-heavy) over **symmetric** (upload) traffic.

**Debate:**  
Strict neutrality can conflict with **QoS**, **security**, and **traffic management** goals.

---

## 12. Key Insights: BGP and Global Connectivity

- **Path vectors** (BGP) generalize **distance vectors** to AS-level routing.  
- The Internet’s scalability arises from **hierarchical routing** and **AS abstraction**.  
- Each AS independently manages its internal network and external policies.  
- Global connectivity emerges through **cooperation and commercial relationships**.  
- IXPs and multi-homing increase redundancy -> resilient network.

---

## Summary

- **Hierarchical routing** allows scalability by routing to **regions (ASes)** instead of hosts.  
- **BGP** is the backbone of Internet routing — path-vector, policy-driven, and decentralized.  
- **Routing policies** (transit, peering) reflect economic and trust relationships.  
- **IXPs** serve as neutral hubs interconnecting ASes for cost-efficient routing.  
- **Multi-homing** and **network neutrality** highlight real-world Internet governance and performance trade-offs.
