# CSE 160 – Lecture 06: Wireless and Contention-Free Protocols

---

## 1. Wireless Communication Challenges

- Still within the **Data Link Layer (MAC sublayer)**.  
- **Wireless ≠ Wired (Ethernet):**  
  - **Ethernet:** CSMA/CD (detect collisions).  
  - **Wi-Fi:** CSMA/CA (avoid collisions).  

### Key Issues
- **Attenuation:** Wireless signals degrade quickly with distance.  
- **Nodes cannot hear while sending:** Transmission swamps local reception; no collision detection.  
- **Hidden Terminals:**  
  - Two nodes out of range of each other may collide at a common receiver.  
- **Exposed Terminals:**  
  - Nodes unnecessarily postpone transmission because they sense another sender, even though no collision would occur.  

---

## 2. Wireless Medium Access

### CSMA/CA (Collision Avoidance)
- Sender senses medium.  
- If idle, wait a random backoff before sending.  
- Receiver sends **ACK** on success.  
- If no ACK, sender infers collision → exponential backoff.  

### RTS/CTS (MACA refinement)
- **RTS (Request to Send):** Sender asks to reserve medium.  
- **CTS (Clear to Send):** Receiver confirms.  
- Nodes hearing RTS/CTS stay silent.  
- Reduces hidden terminal collisions, but:  
  - Still possible if two nodes send RTS at the same time.  

---

## 3. Wi-Fi (IEEE 802.11)

- **Physical Layer:**  
  - 2.4 GHz band → longer range, slower.  
  - 5 GHz band → shorter range, faster.
  - Uses **OFDM modulation**, multiple antennas (MIMO in 802.11n+).  

- **Link Layer:**  
  - Uses **CSMA/CA** with optional RTS/CTS.  
  - Frames acknowledged via **ARQ**.  
  - Error detection with **CRC-32**.  
  - Special addressing due to Access Points (APs).  

- **Persistence:**  
  - Wi-Fi often uses **1-persistence** (transmit immediately after medium is idle).  

---

## 4. Contention-Free Protocols

- **Motivation:** Avoid collisions by taking turns or making reservations.  
- Provide **deterministic service** (bounded delay, fairness, QoS).  

### Examples
1. **Token Ring (802.5):**  
   - Token circulates among nodes.  
   - Holder sends; token then passed on.  
   - Ensures fairness but adds complexity (lost tokens, ring management).  

2. **FDDI (Fiber Distributed Data Interface, 802.4):**  
   - Dual counter-rotating token rings for redundancy.  
   - Higher speed (100 Mbps, 200 km).  

3. **DQDB (Distributed Queue Dual Bus, 802.6):**  
   - Two unidirectional buses with fixed-size cells.  
   - Nodes maintain distributed FIFO queues.  
   - Reservations handled by marking cells as busy/free.  

---

## 5. Comparison: Random vs. Contention-Free

- **Random Access (CSMA/CA, ALOHA, Ethernet):**  
  - Simple, decentralized, scalable.  
  - Efficient under **low load**.  
  - Collisions and fairness issues under **high load**.  

- **Contention-Free (Token Ring, FDDI, DQDB):**  
  - Deterministic, avoids collisions.  
  - Higher complexity, fragile (e.g., token loss).  
  - Better for QoS but less common in practice.  

---

## Summary

- **Wireless MAC** is harder than wired: attenuation, hidden/exposed terminals, no collision detection.  
- **Wi-Fi (802.11)** uses CSMA/CA, optional RTS/CTS, and operates differently across 2.4 vs. 5 GHz bands.  
- **RTS/CTS** reduces but does not eliminate collisions.  
- **Contention-free protocols** (Token Ring, FDDI, DQDB) provide deterministic service but add complexity.  
- In practice, **randomized distributed protocols** dominate due to simplicity and scalability.  

---
