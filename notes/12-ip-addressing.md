# Lecture 12 – IP Addressing

---

## 1. Why IP Addressing Matters
Routing must **scale** to billions of devices. To reduce routing complexity, the Internet uses:
- **Hierarchical routing** (AS-level, BGP)
- **Hierarchical addressing** (IP prefixes)
- **Route aggregation** (CIDR + subnets)

---

## 2. Hierarchical Naming Analogy
Like postal addresses:
- Nearby locations have **similar addresses**
- The **farther away** a location, the **less specific** detail is used initially
- Progressive refinement along the path
> Same idea used in IP routing via prefixes and masks.

---

## 3. IP Addresses
- **Purpose:** Identify a device's **location in network topology**
- **Hierarchical** and **structured**
- **Not random** like MAC/Ethernet addresses
- Interfaces on the **same network share a prefix**
- Prefix allocated by **IANA → RIRs → ISP → customers**

---

## 4. IPv4 Address Format
- 32 bits, written in **dotted decimal**: `A.B.C.D`
- Example: `18.31.0.1 = 00010010.00011111.00000000.00000001`
- **IPv4 focus in class** (IPv6 similar but longer)

---

## 5. Classful Addressing (Legacy)
| Class | Range | Networks | Hosts per Network |
|--------|---------------------------|----------------|---------------------|
| **A** | 0.0.0.0 – 127.255.255.255 | 128 | 16M |
| **B** | 128.0.0.0 – 191.255.255.255 | 16K | 65K |
| **C** | 192.0.0.0 – 223.255.255.255 | 2M | 256 |

- Encoded **network/host** structure in address
- Wasted address space → **obsolete**

---

## 6. Sending a Packet (Exam Favorite!)
When sending to another network:
1. Host compares **destination network** with its own
2. If not local → send to **router**
3. To send to router:
   - Needs **router MAC** → **ARP**
   - Uses **router IP** learned from **DHCP**
4. **IP stays the same end-to-end**, **MAC changes hop-by-hop**
```text
IP Header ← stays same end-to-end
Ethernet Frame ← MAC changes every hop
```

---

## 7. CIDR – Classless Inter-Domain Routing
Replaces classful addressing. Supports **variable prefix lengths**.
- Format: `IP/prefix-length`
- Example: `128.13.0.0/16` → 65,536 addresses
- **Shorter prefix (/8)** → more addresses, **less specific**
- **Longer prefix (/24)** → fewer addresses, **more specific**

| Prefix | Addresses |
|--------|-----------|
| `/8`   | 16M       |
| `/16`  | 65K       |
| `/24`  | 256       |
| `/32`  | 1         |

---

## 8. Public vs Private IPs
| Type | Example | Scope |
|------|---------|-------|
| **Public** | `18.31.0.1` | Routable on Internet |
| **Private** | `10.0.0.0/8`, `192.168.0.0/16` | LAN only |

Private IPs require **NAT** to reach Internet.

---

## 9. Subnets – Divide a Prefix
Used to allocate IPs to **sub-organizations** inside a network.

- Split network using a **subnet mask**:
```text
IP: 192.168.10.35
Mask: 255.255.255.0 (/24)
Subnet = 192.168.10.0
```
- Computed using **bitwise AND**
- Subnetting keeps routing tables smaller internally

---

## 10. Aggregation – Combine Prefixes
Used by ISPs to **summarize routes**:
```text
192.24.0.0/21
192.24.8.0/21 → (combine) → 192.24.0.0/19
192.24.16.0/20
```
> Essential to reduce the load on the routing table!

---

## 11. IP Forwarding – Longest Prefix Match
Routers forward based on **prefix length specificity**:
- Choose the **most specific** match (largest prefix length)
```text
| Prefix | Next Hop |
|--------|----------|
| 192.24.0.0/18 | R1 |
| 192.24.12.0/22 | R2 |

Destination `192.24.14.32` matches /22 more, so it will go to R2
```

---

## 12. Hosts vs Routers
- **Hosts** send everything outside their subnet to **default gateway**
- **Routers** store routes to prefixes, not every host
- Use **default route**: `0.0.0.0/0`

---

## Summary
- IP uses **hierarchical addressing** to scale routing.
- CIDR replaces classes to use **prefix notation**.
- **Longest prefix match** is used for forwarding.
- Subnetting organizes internal networks; aggregation reduces routing tables.
- **IP stays constant hop-by-hop; MAC changes**.
