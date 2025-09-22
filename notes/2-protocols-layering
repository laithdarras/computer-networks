# CSE 160 – Lecture 02: Protocols and Layering

---

## 1. A Brief Tour of the Internet (Top-Down View)

- **Client–Server Interaction**  
  Clicking a web link sends a **request** from client → server; server replies with a **response**.

- **Scalability (9,000 ft)**  
  - **Caching** reduces redundant transfers.  
  - Local/proxy cache checked first → then server for updated version.

- **Naming (8,000 ft: DNS)**  
  - Maps **domain names → IP addresses**.  
  - Translations cached to avoid repeated lookups.  
  - Example: `www.google.com → 207.200.75.200`.

- **Sessions (7,000 ft: HTTP)**  
  - A single webpage = multiple objects (HTML, images, ads).  
  - Each object fetched via **GET** requests, sequentially or in parallel.  

- **Reliability (6,000 ft: TCP)**  
  - Messages may be lost.  
  - TCP provides **acknowledgment, timeout, retransmission**.

- **Congestion Control (5,000 ft: TCP)**  
  - Bandwidth shared among users.  
  - Senders probe path capacity and adjust sending rate.

- **Packets (4,000 ft: TCP/IP)**  
  - Long messages segmented into **packets**.  
  - Example: Ethernet max = 1.5 KB; typical webpage = 10 KB.  
  - Packets numbered for reassembly.

- **Routing (3,000 ft: IP)**  
  - Packets traverse multiple **routers** between hosts.

- **Multi-Access (2,000 ft: Shared Links, e.g., Cable)**  
  - Users share upstream bandwidth.  
  - **Polling or timeslot allocation** by headend.  
  - Uses link-layer addressing (below IP).

- **Framing & Modulation (1,000 ft: Physical Layer)**  
  - Add **headers, error correction (e.g., Reed-Solomon)**, synchronization.  
  - Convert payload into physical signals.  
  - Example: Cable downstream ~30 Mbps, upstream ~3 Mbps.

---

## 2. Protocols and Layers

- **Protocol** = formal agreement on data exchange.  
  - **Syntax:** bit/byte format.  
  - **Semantics:** meaning of fields and actions.  
  - Examples: TCP, HTTP, IP; also real-world analogies (drive-thru ordering).

- **Layering**  
  - Decomposes complexity; **each layer only uses services from below**.  
  - **Peer-to-peer communication** occurs between instances at the same layer (e.g., TCP on host ↔ TCP on server).  
  - **Protocol stack** = full set of layered protocols (e.g., HTTP/TCP/IP/Ethernet).

---

## 3. Encapsulation

- Higher-layer data is wrapped by lower-layer headers/trailers.  
- Analogy: letter in an envelope; postal system only sees outer wrapper.  
- Example:  
  - [802.11 Hdr [IP Hdr [TCP Hdr [HTTP Hdr [Payload]]]]]


- Adds **overhead**, but enables modularity and multiplexing.

---

## 4. Advantages and Disadvantages of Layering

**Advantages**  
- **Information hiding**: higher layers don’t need to know physical medium (Ethernet vs. Wi-Fi).  
- **Reuse**: same protocol can run over multiple lower layers.  
- **Extensibility**: enables interoperability across diverse systems.

**Disadvantages**  
- **Overhead**: each layer adds headers.  
- **Hidden info**: sometimes applications care about lower-layer details (e.g., wireless vs. wired).

---

## 5. Reference Models

### OSI Model (7 Layers)
1. **Application**  
2. **Presentation**  
3. **Session**  
4. **Transport**  
5. **Network**  
6. **Data Link**  
7. **Physical**

- Theoretical, influential, but **not widely implemented**.

### Internet (TCP/IP) Model (4 Layers)
1. **Application** (HTTP, SMTP, DNS, etc.)  
2. **Transport** (TCP, UDP)  
3. **Network** (IP = “narrow waist”)  
4. **Link/Physical** (Ethernet, Wi-Fi, DSL, Cable, etc.)

- Practical, used in real networks.  
- IP serves as the universal interconnection point.

---

## 6. Standards Bodies

- **ITU** – Telecom (e.g., ADSL, MPEG).  
- **IEEE** – Networking (Ethernet 802.3, Wi-Fi 802.11).  
- **IETF** – Internet protocols (RFCs for TCP/IP, HTTP, DNS).  
- **W3C** – Web standards (HTML, CSS).

---

## 7. Layer-Based Terminology

- **Units of data**:  
  - Application → **Message**  
  - Transport → **Segment**  
  - Network → **Packet**  
  - Link → **Frame**  
  - Physical → **Bit**

- **Devices**:  
  - Hub/Repeater → Physical  
  - Switch → Link  
  - Router → Network  
  - Proxy/Middlebox → App/Transport

- **Note**: Layers are **guidelines**, not strict rules. Multiple protocols may share a layer.

---

## 8. Functionality in Protocol Stacks

- **End-to-End Argument (Saltzer, Reed, Clark, 1984):**  
  - Place functionality at lower layer only if it can be implemented completely there.  
  - Otherwise, push to **endpoints**.  
  - Example: reliability (TCP vs. Ethernet error checks).  
  - This principle shaped Internet transparency and flexibility.

---

## 9. What’s Inside a Packet
- [Ethernet Hdr] [IP Hdr] [TCP Hdr] [HTTP Hdr] [Payload]


- Each layer contributes its own header.  
- Example: Ethernet source/dest, IP addresses, TCP ports, HTTP request.

---

## Summary / Takeaways

- **Protocols = syntax + semantics** for communication.  
- **Layering + encapsulation** manage network complexity via modularity.  
- **Reference models** (OSI vs. Internet) guide protocol placement; Internet model dominates in practice.  
- **Encapsulation adds overhead**, but enables interoperability and information hiding.  
- **End-to-end principle**: functionality belongs at endpoints unless fully handled in lower layers.
