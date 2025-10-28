# Lecture 14 – Connections and the Socket API

---

## 1. Overview  
**Goal:** Understand how **processes communicate** through the transport layer.  
Key focus:  
- Naming and identifying processes  
- UDP and TCP mechanisms  
- Connection setup and teardown  
- Programming with the **Socket API**

---

## 2. Naming Processes with Ports  
- A **process** (e.g., HTTP, DNS, SMTP) is an endpoint of communication.  
- Process IDs and memory addresses are **OS-specific** → not portable across systems.  
- TCP and UDP use **16-bit port numbers** as “mailboxes” to identify processes.  
  - Range: **0–65K (2^16)**  
  - Tuple identifying a process:  
    ```
    (IP address, protocol, port)
    ```
  - OS maps this tuple to a process via a **socket** handle.  

### Port Allocation
| Type | Range | Description |
|------|--------|-------------|
| **Well-Known Ports** | 0–1023 | Fixed for standard services (e.g., HTTP 80, DNS 53) |
| **Registered Ports** | 1024–49151 | For specific apps or protocols |
| **Ephemeral Ports** | 49152–65535 | Temporarily assigned to clients |

**Example well-known ports:**  
FTP (20,21), SSH (22), SMTP (25), HTTP (80), POP3 (110), HTTPS (443).  

---

## 3. UDP – User Datagram Protocol  
**Purpose:** Lightweight, message-oriented communication between processes.  

- **Unreliable**: No retransmission, ordering, or flow control.  
- **Use cases:**  
  - DNS (quick lookups)  
  - DHCP (bootstrapping)  
  - VoIP / Real-time streaming  

### UDP Header Fields  
| Field | Size (bits) | Description |
|--------|--------------|-------------|
| Source Port | 16 | Sender process port |
| Destination Port | 16 | Receiver process port |
| Length | 16 | Datagram size (header + data) |
| Checksum | 16 | Error detection (optional in IPv4, mandatory in IPv6) |

- **Checksum rule:**  
  - 0s = not used  
  - If computed sum = 0, transmit as **all 1s** (one’s complement rule).  

---

## 4. TCP – Transmission Control Protocol  
**Purpose:** Provides reliable, ordered, and full-duplex byte-stream delivery between processes.  

### Key Features  
- **Connection-oriented:** Requires setup (3-way handshake).  
- **Reliable:** Uses sequence numbers, acknowledgments (ACKs), and retransmissions.  
- **Flow control:** Prevents receiver buffer overflow.  
- **Congestion control:** Prevents network overload.  
- **Byte-stream abstraction:** No message boundaries (unlike UDP).  

### TCP Header Summary  
| Field | Size | Description |
|--------|------|-------------|
| Source/Destination Port | 16 bits each | Identifies endpoints |
| Sequence Number | 32 bits | Byte position of first data byte |
| Acknowledgment Number | 32 bits | Next expected byte |
| Advertised Window | 16 bits | Flow control window size |
| Flags | 9 bits | Control signals (SYN, ACK, FIN, etc.) |
| Checksum | 16 bits | Ensures integrity |
| Urgent Pointer | 16 bits | Rarely used |

---

## 5. TCP Connection Establishment – Three-Way Handshake  
Used to **synchronize sequence numbers** and **establish a connection**.  
```txt
Client Server

SYN(x) -----------------> (1) Synchronize sequence number
<----------------- SYN(y), ACK(x+1) (2) Acknowledge & respond
ACK(y+1) -----------------> (3) Confirm and start data transfer
```

- **Purpose:**  
  - Synchronize both endpoints.  
  - Avoid **delayed duplicates** using unique Initial Sequence Numbers (ISN).  
  - **Resilient** against duplicates or packet reordering.  
- **Timeouts:** Packets are resent if no ACK is received.  

---

## 6. TCP State Machine  
- Each endpoint maintains a **state** (e.g., `LISTEN`, `SYN_SENT`, `ESTABLISHED`, `TIME_WAIT`).  
- Both client and server run instances of this **finite state machine**.  
- Enables TCP to handle:  
  - Simultaneous opens  
  - Retransmissions  
  - Graceful close procedures  

---

## 7. TCP Connection Teardown  
**Goal:** Graceful, reliable closure with all data delivered.  

### Two-Step Termination  
1. **Active side:** Sends `FIN(x)`, waits for `ACK`.  
2. **Passive side:** Sends `FIN(y)`, active side ACKs.  
- Each FIN/ACK closes one direction of data transfer.  

### TIME_WAIT State  
- Waits for **2×MSL (Maximum Segment Lifetime)** before final closure (~60s).  
- Prevents interference from **delayed duplicates** of old connections.  
- Ensures old packets don’t mix with new sessions.  

---

## 8. Socket API – Network Programming Interface  
The **Socket API** provides a system call interface for using transport protocols.  
Developed in BSD Unix (~1982), available in all major OSes.  

### Common Socket Calls  
| Function | Role | Used by |
|-----------|------|---------|
| `socket()` | Create new socket (returns descriptor) | Both |
| `bind()` | Assign local address/port | Server |
| `listen()` | Mark socket as passive | Server |
| `accept()` | Wait for incoming connections | Server |
| `connect()` | Actively initiate connection | Client |
| `send()` / `recv()` | Data transfer | Both |
| `close()` | Release socket | Both |

**Analogy:** Like plugging a cable into an electrical socket — connects application to network.  

---

### TCP Server–Client Flow  
```txt
Server    Client

socket() socket()
bind() connect()
listen() (3-way handshake)
accept() send()/recv()
send()/recv() close()
close()
```

### UDP Server-Client Flow
```txt
Server   Client

socket() socket()
bind() sendto()
recvfrom() recvfrom()
```

---

## 9. Backlog and Connection Queues
- `listen(socket, backlog)` defines how many pending connections can queue before being accepted.  
- Prevents overflow and protects against **Denial-of-Service (DoS)** attacks.  

---

## Summary

- Processes communicate via **ports (16-bit identifiers)** → up to **65K connections per host**.  
- **UDP**: lightweight, unreliable message delivery.  
- **TCP**: reliable, ordered, full-duplex byte stream with flow and congestion control.  
- **Three-Way Handshake** ensures reliable setup; **TIME_WAIT** prevents delayed duplicate interference.  
- The **Socket API** is the universal interface for writing client-server applications.  
