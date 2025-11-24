# Lecture 16 – TCP Congestion Control  

---

## 1. Overview  

**Goal:** Reach and maintain **equilibrium** in TCP connections while maximizing throughput and minimizing congestion.  

**Key Principles:**  
- **Packet Conservation:** Only inject a new packet when an old one exits the network.  
- **Equilibrium:** Achieved when the number of packets in flight equals the bandwidth–delay product (BDP).  
- **Congestion Control Mechanisms:**  
  - **Slow Start** – reach equilibrium quickly.  
  - **AIMD (Additive Increase Multiplicative Decrease)** – maintain equilibrium.  
  - **Fast Retransmit / Fast Recovery** – repair losses without timeouts.  
  - **ECN (Explicit Congestion Notification)** – proactive congestion signaling via routers.

---

## 2. Reaching Equilibrium – Slow Start  

### Purpose  
Quickly determine the appropriate **congestion window (cwnd)** size to match network capacity.  

### Algorithm  
1. Initialize `cwnd = 1` (or small value).  
2. For each **ACK** received → `cwnd += 1`.  
3. Send up to `min(cwnd, receiver_window)` packets.  
4. **Double cwnd every RTT** (exponential growth).
5. When packet loss occurs → congestion detected.  

- **Result:** Reaches the ideal window (cwnd_ideal) in ~`log₂(W)` RTTs.
```txt
Exponential Growth: cwnd: 1 → 2 → 4 → 8 → 16 → ...

RTT 0: cwnd = 1
RTT 1: cwnd = 2
RTT 2: cwnd = 4
RTT 3: cwnd = 8 → pipe full (BD)
``` 

### Transition to Additive Increase  
- On first loss → set **ssthresh = cwnd / 2**.  
- Restart growth using **AIMD** to probe near equilibrium.  

---

## 3. Maintaining Equilibrium – AIMD  

### Concept  
**Additive Increase Multiplicative Decrease (AIMD)** dynamically adjusts cwnd based on feedback:  

- **Additive Increase (AI):**  
  - Each ACK → `cwnd += 1/cwnd` (≈ +1 per RTT).  
  - Slowly increases sending rate when no congestion.  
- **Multiplicative Decrease (MD):**  
  - On packet loss → `cwnd = cwnd / 2`.  
  - Rapidly backs off to prevent collapse.  

**Control Law Summary:**  
| Event | cwnd Update | Behavior |
|--------|--------------|-----------|
| ACK | `cwnd += 1/cwnd` | Probe bandwidth |
| Loss | `cwnd /= 2` | Back off quickly |

**Rationale:**  
- Increase cautiously (avoid overshooting).  
- Decrease aggressively (avoid congestion).  

### AIMD Properties  
- Converges to **fair and efficient** bandwidth sharing.
    - Produces the **TCP sawtooth** pattern
 
- Works with binary feedback (ACK = success, loss = congestion)

---

## 4. Combination: Slow Start + AIMD  

### Motivation  
- **Slow Start:** Efficient at beginning, but can overshoot.  
- **AIMD:** Stable near equilibrium but slow to reach it.  

### Combined Strategy  
1. Use **Slow Start** initially or after timeouts.  
2. When `cwnd > ssthresh`, switch to **AIMD**.  
3. On loss:  
 - Set `ssthresh = cwnd / 2`.  
 - Reset `cwnd = 1` and start over (TCP Tahoe).  
```txt
Example Timeline:
Slow Start → AIMD → Timeout → Slow Start → AIMD ...
```

## 5. TCP Tahoe vs. TCP Reno  

| Feature | TCP Tahoe | TCP Reno |
|----------|------------|----------|
| Loss Detection | Timeout only | Duplicate ACKs (Fast Retransmit) |
| Recovery | Always restart Slow Start | Uses Fast Recovery |
| cwnd Behavior | Drops to 1 | Halves cwnd |
| Efficiency | Conservative | Higher throughput |

---

## 6. Fast Retransmit  

**Problem:** Waiting for timeout wastes time.  

**Solution:**  
- Sender detects **3 duplicate ACKs** -> infers packet loss.  
- Immediately retransmits the missing segment **before timeout**.  
```txt
Example:
ACK 1, 2, 3, 4, 5, 5, 5, 5 → packet 6 lost
→ retransmit packet 6 after 3rd duplicate ACK
```


**Benefit:** Recovers from isolated losses faster than waiting for timeout.

---

## 7. Fast Recovery  

**Goal:** Avoid entering Slow Start after Fast Retransmit.  

### Steps  
1. After Fast Retransmit -> halve cwnd (`cwnd = cwnd / 2`).  
2. For each additional **duplicate ACK**, treat it as an ACK for a packet that left the network -> send a new packet.  
3. When the ACK “jumps” (indicating the loss was recovered) -> exit Fast Recovery and continue AIMD.  

**Effect:**  
- Keeps ACK clock running (no idle time).  
- Maintains throughput after single losses.  

---

## 8. TCP Reno, NewReno, and SACK  

| Version | Key Feature | Benefit |
|----------|--------------|----------|
| **Reno** | Fast Retransmit + Fast Recovery | Repairs one loss per RTT |
| **NewReno** | Improved ACK logic | Handles multiple losses |
| **SACK (Selective ACK)** | Explicit ACK ranges | Retransmits only missing packets |

---

## 9. Explicit Congestion Notification (ECN)  

**Problem:** Traditional TCP only reacts after packet loss.  

**Solution:** Proactively detect congestion **before loss** using router support.  

### Mechanism  
1. **Router detects congestion** (from queue buildup).  
2. **Marks packets** in IP header (instead of dropping).  
3. **Receiver informs sender** of ECN-marked packets.  
4. **Sender reduces cwnd** as if loss occurred.  

**Advantages:**  
- No packet loss or retransmission overhead.  
- Early detection.  
- Clear router-to-host signaling.  

**Disadvantages:**  
- Requires ECN-capable routers and hosts.
```txt
Example:
[Host] → [Congested Router] → [Host]
↑ Marks packets (IP ECN field)
```


---

## 10. Key Concepts  

- **Slow Start:** Quickly reaches operating point by exponential cwnd growth.  
- **AIMD:** Maintains fair and efficient congestion window through additive increase and multiplicative decrease.  
- **Fast Retransmit:** Detects loss early via duplicate ACKs.  
- **Fast Recovery:** Keeps ACK clock running and avoids unnecessary Slow Start.  
- **ECN:** Proactive congestion control using IP header marking. 

---

## Takeaways  

- **Equilibrium** is achieved when packet injection matches network capacity.  
- **Slow Start + AIMD** form the foundation of modern TCP congestion control.  
- **Fast Retransmit/Recovery** improve responsiveness to isolated losses.  
- **TCP Reno** and successors maintain efficiency by avoiding full restarts.  
- **ECN** allows routers to signal congestion **before packet loss**, reducing delays and retransmissions.  
