# Lecture 09 – Introduction to Routing Protocols

---

## 1. Overview

**Goal:** Understand how routers compute efficient paths for packets through a distributed network.  
**Scope:** Focus on **unicast routing** (single source → single destination).

Routing protocols update the **routing table**, a data structure that stores the next-hop information for each destination.

---

## 2. Forwarding vs. Routing

| Concept | Definition | Characteristics |
|----------|-------------|----------------|
| **Forwarding** | Sending a packet to the next hop based on the routing table. | Local, fast, data-plane function. |
| **Routing** | Deciding which path packets should take through the network. | Global, slower, control-plane function. |

Forwarding: Node A → Next Hop → Destination
Routing: Compute best paths across all nodes

---

## 3. Routing Fundamentals

- **Objective:** Deliver packets efficiently from source to destination.
- **Analogy:** Like car traffic — we aim for smooth flow and congestion avoidance.
- **Fairness:** Perfect fairness is impossible; instead aim for **proportional fairness** (avoid starvation).
- **Scalability:** The most critical aspect of routing — protocols must work as networks grow.

---

## 4. Network as a Graph

Routing can be modeled as a **graph problem**:
- **Routers = Nodes**
- **Links = Edges (with costs)**
- Routing = Finding optimal paths across the graph.

---

## 5. Bandwidth Allocation Timescales

| Mechanism | Adaptation Timescale | Example |
|------------|----------------------|----------|
| Load-sensitive routing | Seconds | Handle hotspots |
| Routing | Minutes | React to link/node failures |
| Traffic engineering | Hours | Adjust to network load |
| Provisioning | Months | Plan for new customers |

---

## 6. Routing Properties

Good routing algorithms should ensure:
- **Correctness:** Finds working paths  
- **Efficiency:** Uses bandwidth effectively  
- **Fairness:** Avoids starving any node  
- **Fast Convergence:** Recovers quickly after topology changes  
- **Scalability:** Handles large, growing networks

---

## 7. Routing Architectures

| Type | Description |
|------|--------------|
| **Centralized vs. Distributed** | Internet uses distributed — no central controller. |
| **Hop-by-Hop vs. Source Routing** | Each router makes independent decisions. |
| **Deterministic vs. Stochastic** | Predictable vs. probabilistic path selection. |
| **Static vs. Dynamic** | Static: fixed paths; Dynamic: adapts to changes. |

**Key Rule:** Routing must be **distributed**, concurrent, and robust to failures.

---

## 8. Flooding and Neighbor Discovery

**Flooding** = Broadcast every message to all nodes.  
**Neighbor Discovery (ND)** = Detect adjacent routers.
> Essence of Project 1!

### Flooding Mechanics
1. Node sends message to all neighbors except where it came from.  
2. Each node remembers message `(source, seq#)` to avoid duplicates.  
3. **Reliable flooding** uses **ARQ (Automatic Repeat reQuest)** — resend if ACK not received.

**Flooding + ND = complete topology knowledge** → run Dijkstra’s algorithm to compute shortest paths.

---

## 9. Shortest Path Routing

Routing decisions are based on **cost metrics** (e.g., latency, bandwidth, monetary cost).

### Defining “Best” Path
- **Cost Function:** Assign weight to each link  
- **Shortest Path:** Path with minimum cumulative cost  
- **Optimality Property:** Subpaths of shortest paths are also shortest paths  

**Example:**
```txt
A → B → C → E
Total Cost = 7
Other routes: 8, 9, 10 → not optimal
```

---

## 10. Dijkstra’s Algorithm (Link-State Computation)

**Purpose:** Compute shortest paths from one source to all destinations.  
**Used in:** Link-State Routing (e.g., OSPF).

### Algorithm Summary
1. Initialize distances from source to all neighbors  
2. Add the nearest unvisited node to the set `M`  
3. Update costs of its neighbors  
4. Repeat until all nodes are considered  

**Complexity:** `O(|E| + |V| log |V|)` using Fibonacci Heaps.  

**Result:** Builds a **sink tree** or **source tree** — the union of all shortest paths.

---

## 11. Link-State Routing

**Goal:** Each router independently builds a consistent view of the network.

### Process
1. **Flood Topology:**  
   Each node sends a **Link State Packet (LSP)** with `[router ID, neighbors, costs]` to all others.  
2. **Build Database:**  
   Each node stores all received LSPs to reconstruct the network graph.  
3. **Compute Routes:**  
   Run **Dijkstra’s algorithm** to generate the **forwarding table**.  

**Result:** Every router independently computes consistent shortest paths.

---

## 12. Handling Changes

### Link/Node Failures
- Adjacent routers detect failure and flood updated LSPs.  
- Old data removed using **sequence numbers** and **cost = ∞** signals.

### Additions
- New routers or links flood new LSPs.  
- Updated entries are incorporated automatically.

### Complications
- Sequence numbers may overflow or desynchronize.  
- Crashed nodes lose counters → need **aging** and **versioning** to resync databases.

---

## 13. Open Shortest Path First (OSPF)

**Most common link-state protocol.**

### Features
- **Authentication:** Prevent unauthorized routing updates  
- **Hierarchical Design:**  
  - Divides network into **areas**  
  - **Area Border Routers (ABRs)** summarize internal topology to reduce flooding  
- **Load Balancing:** Multiple equal-cost paths can be used

---

## 14. Routing Cost Metrics

| Metric Type | Description |
|--------------|-------------|
| **Static** | Manually assigned or hop-count based (cheap but inaccurate). |
| **Dynamic** | Reflects real-time load; may oscillate — damping required. |

**Revised ARPANET Metric:**  
- Limited variation (3:1 ratio).  
- Adjusts gradually based on utilization.  
- Prioritizes capacity at low loads.

---

## 15. Cost Estimation Techniques

Used to estimate link costs (e.g., delay, load).

| Method | Formula | Notes |
|---------|----------|-------|
| **Cumulative Average** | `(sum of samples) / n` | Simple but unresponsive |
| **Moving Average** | Avg of last *W* samples | Reacts to trends |
| **Weighted Moving Average** | Adds weights to recent samples | Prioritizes recent data |
| **Exponentially Weighted Moving Average (EWMA)** | `EWMAn = αSn + (1–α)EWMAn–1` | Common in dynamic routing (α = smoothing factor) |

EWMA enables **soft-state routing** — periodically refreshed, fault-tolerant, and adaptive.

---

## 16. Hard State vs. Soft State

| Type | Characteristics | Use Case |
|-------|-----------------|-----------|
| **Hard State** | Strict, static, low overhead | Stable networks |
| **Soft State** | Periodically refreshed, fault-tolerant | Dynamic environments (e.g., Internet routing) |

---

## Summary

- **Routing** determines global paths; **forwarding** executes local delivery.  
- **Flooding + Neighbor Discovery** provide topology info for link-state protocols.  
- **Dijkstra’s algorithm** forms the core of shortest-path computation.  
- **Link-State Routing** (e.g., **OSPF**) achieves fast convergence but at a scalability cost.  
- **Routing cost metrics** and **EWMA smoothing** ensure adaptive yet stable performance.  
- **Scalability and proportional fairness** are essential — routing must be distributed, resilient, and efficient.
