# CSE 160 – Lecture 03: Bits and Bandwidth

---

## 1. Link Model

- **Message Model**  
  - Message size: **M bits**  
  - Link rate (bandwidth): **R Mbps**  
  - Propagation delay: **D seconds**  

- **Latency (One-Way Delay)**  
  - **Transmission delay:** M / R (time to put message on wire)  
  - **Propagation delay:** D (time for signal to travel across medium)  
  - **Total latency:**  
    ```
    L = M/R + D
    ```
  - **Round Trip Time (RTT):** 2 × one-way latency  

- **Throughput**  
  - System’s ability to output data.  
  - Formula:  
    ```
    Throughput = Transfer Size / Transfer Time
    ```
  - Accounts for protocol overheads.  
  - Different from raw bandwidth.  

- **Bandwidth-Delay Product (BDP)**  
  - Amount of data “in flight” in the network:  
    ```
    BDP = Bandwidth × Delay
    ```
  - Example: 200 Mbps × 50 ms = 1.25 GB  
  - Important for understanding buffering and flow control.

---

## 2. Media Types

- **Wires (Copper)**  
  - **Twisted Pair:** Common in LANs, reduces noise via twisting, Cat5e/Cat6.  
  - **Coaxial Cable:** Better shielding, higher performance.  

- **Fiber Optics**  
  - Glass strand with **total internal reflection**.  
  - Extremely high bandwidth (terabits).  
  - Multi-mode (dispersion limited) vs. single-mode.  

- **Wireless**  
  - Broadcast medium, signal radiates in all directions.  
  - Subject to **interference** when multiple users share the same frequency.  
  - Concept of **spatial reuse**: same frequency reused in different locations (basis of cellular systems).  

---

## 3. Signals and Encoding

- **Digital → Analog Conversion**  
  - Bits transmitted as analog waveforms.  
  - Degradation: delay, attenuation, noise, frequency cutoff.  

- **Effect of Less Bandwidth**  
  - Fewer frequencies → degraded signals.  
  - Limits rapid transitions needed for digital communication.  

- **Interference in Wireless**  
  - Multiple signals on same frequency interfere.  
  - Leads to **spatial reuse** techniques.  

- **Clock Synchronization**  
  - Challenge: distinguishing long runs of 0s or 1s.  
  - Solutions:  
    - Send separate clock (expensive).  
    - Limit message length.  
    - Embed clock into data (coding schemes).  

- **Common Encoding Schemes**  
  - **NRZ (Non-Return to Zero):** High = 1, Low = 0. Problem: long runs cause sync issues.  
  - **NRZI:** Transition = 1, no transition = 0.  
  - **Manchester Coding:** Transition in middle of bit. Self-clocking, but 50% efficiency.  
  - **4B/5B, 8B/10B Codes:** Map data bits to larger coded sequences with guaranteed transitions. Improve sync and DC balance.

- **Passband Modulation**  
  - Needed for fiber and wireless.  
  - Modulates a **carrier frequency** by varying:  
    - Amplitude (ASK)  
    - Frequency (FSK)  
    - Phase (PSK)  

---

## 4. Fundamental Limits

- **Nyquist Limit (1924)**  
  - Maximum bit rate without noise:  
    ```
    R = 2B log2(V)
    ```
  - B = bandwidth (Hz), V = signal levels.  

- **Shannon Capacity (1948)**  
  - Maximum reliable rate with noise:  
    ```
    C = B log2(1 + S/N)
    ```
  - S/N = signal-to-noise ratio (linear).  
  - Expressed in dB:  
    ```
    SNR_dB = 10 log10(S/N)
    ```

- **Implications**  
  - Wired links: engineered SNR and bandwidth → fixed data rate.  
  - Wireless links: variable SNR → adaptive data rates.  

---

## 5. Practical Example – DSL

- Reuses twisted pair telephone lines.  
- Up to ~2 MHz bandwidth, but only lowest 4 kHz for voice.  
- Uses **passband modulation (QAM)** with separate bands for upstream and downstream.  
- Variable bits per symbol depending on SNR.  

---

## Summary / Takeaways

- **Latency = Transmission + Propagation + Queueing.** RTT doubles one-way delay.  
- **Throughput ≠ Bandwidth**; overhead and protocol effects matter.  
- **Bandwidth-Delay Product** measures data “in flight” and influences buffering.  
- **Signals degrade** over media; encoding and modulation techniques counteract this.  
- **Nyquist and Shannon limits** define the theoretical maximum data rates.  

---
