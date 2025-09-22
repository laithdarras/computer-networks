# CSE 160 – Lecture 05: Multiplexing and Randomized Access

---

## 1. Multiplexing Basics

- **Multiplexing (mux):** Sharing a common resource (e.g., a link).  
- Common in **radio/TV stations, cellular networks, telecoms**.  

### Static Partitioning
1. **Time Division Multiplexing (TDM)**  
   - Users take turns on a fixed schedule.  
   - Each gets full rate, but only during its time slot.  

2. **Frequency Division Multiplexing (FDM)**  
   - Users assigned distinct frequency bands.  
   - Each transmits continuously but at a lower rate.  

**Comparison:**  
- TDM → burst of high-rate transmissions.  
- FDM → continuous low-rate transmissions.  

**Use Cases:**  
- Works well for **continuous traffic** and fixed number of users.  
- Used in TV, radio (FDM), GSM cellular (TDM within FDM).  

---

## 2. Statistical Multiplexing

- **Network traffic is bursty**: peak rate ≫ average rate.  
- Fixed allocation (TDM/FDM) is inefficient.  
- **Statistical multiplexing:** share channel according to actual demand.  
- Leads to **multiple access protocols**.  

---

## 3. Multiple Access Protocols

Two approaches:  

1. **Randomized Access**  
   - Nodes transmit without coordination.  
   - Suited for **bursty traffic** and low load.  
   - Examples: **ALOHA, CSMA, Ethernet**.  

2. **Contention-Free Access**  
   - Nodes ordered or scheduled.  
   - Suited for **high load** or strict QoS.

---

## 4. ALOHA Protocol

- Origin: Hawaii timesharing system (1960s).  
- **Distributed allocation**: no central control, no single point of failure.  
- **Protocol:**  
  1. Send data when available.  
  2. If no ACK, wait random time and resend.  

- **Performance:**  
  - Works well at low load.  
  - Max efficiency:  
    - Pure ALOHA: ~18%  
    - Slotted ALOHA: ~36%  

- **Insight:** Distributed randomized solutions are simple, fault-tolerant, and scalable.  

---

## 5. CSMA (Carrier Sense Multiple Access)

- Improvement over ALOHA: **listen before transmitting**.  
- **CSMA variants:**  
  - **1-persistent:** Transmit immediately when idle.  
  - **Non-persistent:** Wait random time if busy, then retry.  
  - **p-persistent:** Transmit with probability *p* when idle (slotted time).  

- Still possible collisions due to **propagation delay**.  
- Effectiveness depends on **bandwidth-delay product (a = BW × Delay / Frame Size)**.  
  - Small *a* (LANs) → effective.  
  - Large *a* (satellites) → less effective.  

---

## 6. CSMA with Collision Detection (CSMA/CD)

- Detect collisions while transmitting.  
- Abort and send **jam signal** so all nodes detect it.  
- Requires **minimum frame size = 2D seconds** (round-trip time across medium).  
- Ethernet uses CSMA/CD.  

---

## 7. Binary Exponential Backoff (BEB)

- Strategy for handling repeated collisions.  
- After *Nth* collision: wait random time chosen from `0 … 2^N – 1` slots.  
- Maximum backoff capped (give up after 16 attempts).  
- **Properties:**  
  - Adapts quickly to congestion.  
  - Efficient over wide load ranges.  
  - Scalable for small and large networks.  

---

## 8. Classic Ethernet

- **Standard:** IEEE 802.3.  
- **Characteristics:**  
  - 10 Mbps over coaxial cable (original).  
  - 64–1500 byte frames.  
  - Uses **Manchester coding** + CRC-32.  
  - Globally unique **MAC addresses (6 bytes)**.  
- **Limitations:**  
  - Random access not perfectly fair (one node can dominate).  
  - Collisions reduce efficiency as network grows.  

- **Modern Ethernet:**  
  - Now based on **switches**, not shared medium.  
  - Still uses Ethernet framing/standards.  

---

## Summary / Takeaways

- **Multiplexing:** TDM/FDM = static, best for predictable continuous traffic.  
- **Statistical multiplexing:** Better for bursty traffic, requires multiple access protocols.  
- **ALOHA → CSMA → Ethernet:** evolution from pure random access to more efficient schemes.  
- **CSMA/CD with BEB:** backbone of classic Ethernet, providing scalability and efficiency.  
- **Distributed randomized solutions** are essential for scalability, performance, and fault tolerance — a principle that ties into [CSE 168 (Distributed Systems)](https://github.com/laithdarras/distributed-systems).  

---
