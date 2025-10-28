# Lecture 15 – TCP and Network Congestion  

---

## 1. Introduction to Congestion  

- **Congestion** is a form of “traffic jam” in the network.  
- Routers use **queues** to buffer packets when input > output rate.  
- If input exceeds output **persistently**, queues overflow → **packet loss**.  
- **Dropped packets** contradict TCP’s reliability, leading to **retransmissions**, delay, and instability.  

**Goal:**  
Design mechanisms to let senders pace themselves without overloading the network.  

---

## 2. Nature and Effects of Congestion  

- Routers maintain **FIFO queues** that drop packets when full.  
- **Temporary bursts** can be absorbed, but sustained overload → congestion.  
- Effects as load increases:  
  - **Delays** rise (due to queue buildup).  
  - **Losses** increase.  
  - **Throughput** eventually **drops** below offered load.  
  - **Goodput** (useful data delivered) falls below throughput due to spurious retransmissions.  

> **Ideal operation:** run the network just before the onset of congestion!

---

## 3. Bandwidth Allocation  

### Goals  
- **Efficiency:** fully utilize available capacity without congestion.
  - Can't be slow!
- **Fairness:** each sender gets a reasonable share of bandwidth.
  - Avoid starvation!

### Challenges  
- Number of active senders changes dynamically.  
- Each sender’s capacity varies with route.  
- No global coordination — each endpoint only sees **local feedback**.  

### Cooperation Across Layers  
- **Network layer:** detects congestion (via packet loss, delay).  
- **Transport layer:** reacts by **reducing offered load**.  
- Together, they continuously **adapt transmission rates** for stability and fairness.

---

## 4. Congestion Collapse  

- **Historical event (1986–87):** Internet throughput dropped by **1000×** due to uncontrolled retransmissions.  
- TCP originally used **fixed-size windows** without feedback-based adaptation.  
- As congestion grew, routers dropped packets → TCP senders **retransmitted aggressively**, worsening congestion.  
- Led to the **congestion collapse** of the ARPANET.  

### Key Lesson  
“Sending more packets when the network is already overloaded makes it worse.”  
→ inspired **Van Jacobson’s** algorithms (TCP Tahoe/Reno).

---

## 5. Van Jacobson’s Contributions  

- Developed core TCP congestion control mechanisms:  
  - **Slow Start**  
  - **Congestion Avoidance**  
  - **Fast Retransmit**  
  - **Fast Recovery**  
  - **Adaptive Timeouts**  

- Introduced the **packet conservation principle**:  
  > “A new packet should not enter the network until an old packet leaves.”

---

## 6. TCP Tahoe & Reno  

- Avoid congestion **without router changes**.  
- Introduced a **congestion window (cwnd)** to complement the flow-control window.  
- **AIMD (Additive Increase, Multiplicative Decrease)**:  
  - **Increase cwnd** gradually (avoid underutilization).  
  - **Halve cwnd** when detecting loss (avoid collapse).  
- Feedback: packet **loss** and **ACK timing** signal network conditions.  

---

## 7. TCP ACK Clocking  

**Definition:**  
TCP’s **self-clocking mechanism** that regulates the sending rate based on ACK arrival times.  
```txt
[Sender] --segments--> [Network] --ACKs--> [Sender]
```

- Each in-order ACK **advances the sliding window** → allows sending of a new segment.  
- ACKs effectively act as a **“clock”** for data transmission.  

### Benefits  
- Smooths out bursts of traffic.  
- Matches sending rate to **bottleneck link capacity**.  
- Prevents queue buildup and packet loss.  
- Maintains **low delay** and **high throughput** equilibrium.

---

## 8. TCP Congestion Control Rules  

1. **Reach equilibrium:** stabilize sending rate to match network capacity.  
2. **Packet conservation:** don’t inject new data until an old packet has left.  
   - A packet “leaves” when:  
     - It’s acknowledged (ACK received), or  
     - It’s declared lost (timeout).  
3. **Re-stabilize** when conditions change (e.g., new flows join).

---

## 9. Retransmission Timeouts (RTO)  

- **Purpose:** determine when to resend unACK'd packets.  
- **Challenge:** timeout must be “just right.” 
  - Too long → idle connection, wasted bandwidth.  
  - Too short → early resends, duplicate packets.  

**Easy on LANs:** stable RTT.  
**Hard on Internet:** variable RTT due to queueing and routing dynamics.

---

## 10. Estimating Round-Trip Time (RTT)  

### Approach 1: Constant RTT (Bad)
- Simple but not adaptive — unsuitable for dynamic networks.  

### Approach 2: Adaptive Estimation (Good)
Use **Smoothed RTT (SRTT)** via **Exponential Weighted Moving Average (EWMA):**
```txt
SRTT_{n+1} = (1 - g) * SRTT_n + g * RTT_{n+1}
```
- 0 <= g <= 1
  - Typical (g = 0.1-0.2).  
  - Smaller (g): smoother, slower to adapt.  
  - Larger (g): faster reaction, more jitter.

### RFC 793 Original Timeout  
```txt
RTO = 2 * SRTT
```
- Conservative multiplier accounts for variance.
- Too long is better than too short!
  - We want to ALWAYS avoid congestion collapse!

---

## 11. Jacobson/Karels Adaptive Timeout Algorithm  

Improves upon RFC 793 by factoring **variance** into timeout estimation:  

1. Estimate RTT deviation:
```txt
   SVar_{n+1} = (1 - beta) * SVar_n + beta * |RTT_{n+1} - SRTT_{n+1}|
```
   Typical: (beta = 0.1).  

2. Compute timeout:  
```txt
   RTO = SRTT + k * SVar
```
- Typical: (k = 4) provides safety margin.  

**Behavior:**  
- When variance is low → timeout ≈ SRTT.  
- When variance is high → timeout increases sharply to prevent false retransmits.

---

## 12. Karn/Partridge Algorithm  

**Problem:** RTT measurements for retransmitted packets are **ambiguous**.  

**Solution:**  
- Ignore RTT samples from retransmitted packets.  
- Maintain exponential backoff of timeout until a valid RTT sample is obtained.

---

## Summary  

- **Congestion** arises from persistent input > output rate at routers, causing loss and delay.  
- **Van Jacobson’s algorithms** (AIMD, ACK clocking, adaptive timeout) prevented Internet collapse.  
- **ACK clocking** self-regulates TCP to match bottleneck capacity and maintain stability.
- **Accurate RTT estimation** is crucial for setting retransmission timeouts.  
- **Jacobson/Karels** and **Karn/Partridge** algorithms supports modern TCP.
