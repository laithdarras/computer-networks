# Lecture 08 – IP, ICMP, and the Network Layer

## Why We Need a Network Layer
- Switches alone don’t scale:
  - **Routing tables** blow up at Internet scale.
  - Broadcasts across the Internet are infeasible.
  - Spanning tree convergence time grows with network diameter.
- Switches don’t work across multiple link-layer technologies (Ethernet, Wi-Fi, 5G, etc.).
- Limited traffic control — can’t plan routes/bandwidth.

**Solution**: The **network layer** provides:
- **Hierarchy** (prefix-based addressing, hierarchical routing).
- **Heterogeneity support** via a common protocol (**IP**).
- **Traffic control** through routing, QoS, and congestion management.

---

## Routing vs. Forwarding
- **Routing**:
  - Decides which direction traffic should go.
  - Distributed, global, computationally expensive.
  - Updates the **routing table**.
- **Forwarding**:
  - Moves packets to the next hop based on the routing table.
  - Local, fast, per-router operation.

**Example**  
- Routing = planning postal routes.  
- Forwarding = mailman delivering letters based on street address.

---

## Network Service Models

### Datagram Model (IP / Postal Service analogy)
- **Connectionless**, best-effort (unreliable).
- Each packet is independent.
- No delivery guarantees.
- Example: **IP**.

### Virtual Circuit Model (Telephone analogy)
- **Connection-oriented**: setup → data transfer → teardown.
- Routers maintain per-connection state.
- All packets follow the same path.
- Examples: **MPLS, ATM, Frame Relay**.

### Store-and-Forward Packet Switching
- Routers receive complete packets before forwarding.
- Use **internal buffers** (FIFO queues).
- If buffers are full → **packets dropped** (congestion).

---

## Datagrams vs Virtual Circuits

| Feature           | Datagram (IP)             | Virtual Circuit (MPLS/ATM)   |
|-------------------|---------------------------|------------------------------|
| Setup Phase       | None                      | Required                     |
| Router State      | Per destination           | Per connection               |
| Addressing        | Full destination address  | Short label                  |
| Routing           | Per packet                | Per circuit                  |
| Failures          | Easy to mask              | Harder to mask               |
| QoS Support       | Difficult                 | Easier                       |

---

## Internetworking
- **Networks differ**: service models, addressing, QoS, packet sizes, security.
- Solution: **IP as the common protocol (“glue”)**.
- Pioneers: **Cerf and Kahn** → designed TCP/IP in 1974.
- **Internet Reference Model**:
  - IP forms the **“narrow waist”**: minimal service but universal interoperability.
  - Provides only **best-effort connectivity**.

---

## Internet Protocol (IP)
- **IPv4 (RFC 791)**: 32-bit addressing, best-effort delivery.
- **IPv6**: 128-bit addressing, gradually adopted.
- **Routing protocols** (RIP, OSPF, BGP) update routing tables.
- **ARP** maps IP → MAC addresses.

### IPv4 Packet Format (memorize for exam!)
### IPv4 Header (Simplified Layout)

| Bits        | 0–3    | 4–7   | 8–15    | 16–18   | 19–31              |
|-------------|--------|-------|---------|---------|--------------------|
| **Row 1**   | Version | HLen | TOS     | Length  | Identifier         |
| **Row 2**   | Flags   | Fragment Offset                               |
| **Row 3**   | TTL     | Proto | Checksum                              |
| **Row 4**   | Source Address                                         |
| **Row 5**   | Destination Address                                    |
| **Row 6**   | Options (variable) | Padding (variable)                 |
| **Row 7**   | Data                                                   |

**Key fields**:
- **TTL**: decremented each hop, packet dropped if 0 → max Internet diameter = 255 hops.
- **Fragmentation**: splits large packets across links with smaller MTU.
- **Checksum**: covers header only, recalculated each hop.
- **Source/Destination addresses**: unchanged by routers.

---

## Fragmentation and MTU
- Different links have different **MTUs** (Ethernet = 1500B, Wi-Fi = 2300B, FDDI = 4500B).
- IPv4 fragments packets when needed; reassembly only at the **final destination**.

### Issues
- Loss of one fragment = loss of whole packet.
- Reassembly is costly, magnifies packet loss rate.
- Security vulnerabilities.

### Best Practice
**Avoid fragmentation** → use **Path MTU Discovery**:
- Sender tests packet sizes.
- Routers return ICMP “too big” messages when packet > MTU.
- Standard method today.

---

## ICMP (Internet Control Message Protocol)
- Defined in **RFC 792**. Runs on top of IP (Protocol field = 1).
- Provides:
  - **Error reporting** (router → source).
  - **Diagnostics** (ping, traceroute).

### ICMP Messages
- **Destination Unreachable** (host, network, port, protocol).
- **Redirect** (better route exists).
- **TTL Expired** (used by traceroute).
- **Echo Request/Reply** (used by ping).
- **Checksum errors**.

**Format**:
- Fields: **Type, Code, Checksum**.
- Includes part of offending IP packet in payload.

---

## Traceroute
- Exploits **TTL** and **ICMP errors**.

### Process
1. Send probe with TTL = 1 → router drops and sends ICMP “TTL expired”.
2. Increase TTL to 2 → next router responds.
3. Repeat until destination reached.

- Reveals each hop on the path.

---

## Summary
- **Routing** = global decision-making; **Forwarding** = local next-hop action.
- Two service models:
  - **Datagram (IP)**: flexible, best-effort, stateless.
  - **Virtual Circuit (MPLS/ATM)**: reliable path, more state, easier QoS.
- **IP** is the universal glue of the Internet, providing minimal services.
- **IPv4 header** (fields like TTL, fragmentation, checksum) is exam-critical.
- **Fragmentation is inefficient** → modern networks use **Path MTU Discovery**.
- **ICMP** provides error reporting and diagnostic tools like **ping** and **traceroute**.
