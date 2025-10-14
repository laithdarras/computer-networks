# Lecture 13 – Sliding Windows and ARQ (Transport Layer)

---

## 1. Transport Layer Basics

- **Goal:** Provide reliable, end-to-end communication **between processes**.
- **Transport = Process-to-process** communication.
- **Network = Host-to-host** communication.

| Layer        | Data Unit | Example |
|---------------|-----------|---------|
| Application   | Message   | HTTP request |
| Transport     | **Segment** | TCP/UDP |
| Network       | **Packet**  | IP |
| Link          | **Frame**   | Ethernet |

- **Bytestream abstraction**: TCP sends a continuous stream of bytes between processes.
- Transport layer uses IP services but **adds reliability**.

---

## 2. TCP vs UDP (Quick Recap)

| Feature | TCP | UDP |
|----------|-----|-----|
| Type | Reliable stream | Unreliable datagram |
| Order | Guaranteed | Not guaranteed |
| Retransmission | Yes | No |
| Flow Control | Yes | No |
| Use Cases | Web, SSH | DNS, VoIP |

---

## 3. Reliability – ARQ (Automatic Repeat Request)

- **Core idea:** Sender resends lost data until ACK'd.
- **Mechanism:**
  - Receiver sends **ACK** for received segments.
  - Sender uses **timeouts** to detect loss.
  - Lost ACKs or duplicate packets handled using **sequence numbers**.

### ARQ Challenges
- **Timeout selection**:
  - Too long → idle link
  - Too short → useless retransmissions
  - Easy in LANs (low delay variance), hard in WANs
- **Duplicates**:
  - Use **sequence numbers** to detect duplicates.

---

## 4. Stop-and-Wait ARQ (Alternating Bit Protocol)
- **Only one unACK'd frame in flight.**
- Sequence numbers alternate: **0,1,0,1,...**
```text
Send Frame 0 → Wait for ACK 0 → Send Frame 1 → Wait for ACK 1 → ...
```

### Why OK for LANs?
- **Low propagation delay** and **small RTT**
- Simple and efficient enough

---

## 5. Bandwidth Utilization Problem
- Actual throughput limited by waiting for ACKs:
> Throughput = Message/{2 * Delay} 

- Example: Long-distance link → extremely low utilization.
- **Solution: pipeline segments** → Sliding Window.

---

## 6. Sliding Window Protocol

- Allows **multiple unACK'd packets in flight**.
- Window controls the number of outstanding frames.
- **Goal:** Keep the "network pipe" full to maximize throughput.
> W = {2 * BDP}/Packet_Size

---

## 7. Sliding Window Variants

| Protocol | Efficiency | Complexity | Retransmission Behavior |
|-----------|------------|------------|--------------------------|
| **Stop-and-Wait** | Low | Simple | One-by-one |
| **Go-Back-N** | Medium | Simple | Retransmit from first lost pkt |
| **Selective Repeat** | High | Complex | Retransmit only missing pkts |

---

## 8. Sliding Window Mechanics

### Sender State
- Maintains:
  - **LAR** – Last ACK Received
  - **LFS** – Last Frame Sent
  - **Window**: frames in `[LAR+1 ... LFS]`

### ACK Strategies
- **Cumulative ACK (TCP)**: "I received everything up to byte X."
- **Selective ACK**: "I received packets 5,6,8 - but missing 7."

---

## 9. Sequence Number Space

- Must support wraparound:
> **Max Seq Number** = 2^n - 1
- **Go-Back-N**: Need **W + 1** sequence numbers.
- **Selective Repeat**: Need **2W** sequence numbers.

---

## 10. Flow Control

- **Goal:** Prevent sender from overwhelming receiver.
- Receiver advertises **available buffer space** using `AdvertisedWindow`.
- Sender uses:
  - EffectiveWindow = AdvertisedWindow - (LastByteSent - LastByteAcked)
- Flow control is **receiver-based**, prevents buffer overflow.

---

## 11. TCP Sliding Window

Sliding window enables:
- **Reliable delivery** – ACK confirms receipt  -
- **In-order delivery** – sequence numbers
- **Flow control** – Advertised window

> **Note:** TCP also adds **congestion control** (later lecture)

---

## Summary

- ARQ achieves reliability using **ACK + timeout + retransmission**.
- **Stop-and-Wait** is simple but performs poorly over large delays.
- **Sliding Window** increases efficiency via pipelining.
- **Go-Back-N and Selective Repeat** balance reliability and efficiency.
- **Flow control prevents buffer overflow** at the receiver.
- **Correct but inefficient** on high-delay links.

