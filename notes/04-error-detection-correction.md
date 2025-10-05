# CSE 160 – Lecture 04: Framing, Error Detection and Correction

---

## 1. Framing

- **Goal**: Convert a raw stream of bits into **frames** (messages).  
- Requires **synchronization** at receiver to identify start/end of frames.  

### Methods

1. **Byte Count**
   - First byte = frame length.  
   - **Problems**:  
     - Corruption of length field → loss of synchronization.  
     - Wastes space and unreliable.  

2. **Byte Stuffing**
   - Use a **special flag byte** (e.g., `0x7E`) to mark frame boundaries.  
   - Escape occurrences of flag or escape within data:  
     - Replace `FLAG` → `ESC FLAG`  
     - Replace `ESC` → `ESC ESC`  
   - Reliable but introduces overhead.  

3. **Bit Stuffing**
   - Define **flag** as `01111110`.  
   - On transmit: after 5 consecutive `1`s, insert a `0`.  
   - On receive: remove `0` after 5 consecutive `1`s.  
   - **Pros**: more efficient than byte stuffing.  
   - **Cons**: more complex, handled at hardware level.  

**Example Flow (Bit Stuffing):**
- Data: 01111110
- Transmitted: 011111010 (insert 0 after 5th 1)
- Received: 01111110


---

## 2. Error Coding

- **Problem**: Noise may flip some bits during transmission.  
- **Approach**: Add redundancy to detect or correct errors.  

### Strategies
- **Detection**: Identify errors and request retransmission.  
- **Correction**: Infer correct data without retransmission.  

---

## 3. Error Detection

### Parity Bit
- Add 1 bit = XOR of all data bits.  
- Detects **odd number** of errors, misses even-numbered errors.  
- **2D Parity**: Extend parity across rows/columns → detects more errors and corrects single-bit errors.  

### Checksums
- Compute sum of data words, transmit with data.  
- Used in **TCP, UDP, IP**. 
- Weaker than CRC, stronger than parity.  

### Cyclic Redundancy Check (CRC)
- Widely used (Ethernet, Wi-Fi).  
- Based on polynomial division in finite fields.
- Uses XOR division (or mod 2).
- Sender: append remainder of `data / generator polynomial`.  
- Receiver: recompute, check remainder = 0.  
- Example: Ethernet **CRC-32**.  

---

## 4. Error Correction

### Hamming Distance
- Minimum number of bit changes to convert one valid codeword into another.  
- If distance = **d**:  
  - Detect up to **d–1** errors.  
  - Correct up to **⌊(d–1)/2⌋** errors.  

### Hamming Codes
- Distance = 3. Detects 2-bit errors, corrects 1-bit errors.  
- Check bits placed at **powers of 2** (positions 1, 2, 4, ...).   
- Decoding: recompute parity, form **syndrome** → indicates error position.  

### Other Codes
- **Convolutional codes**: Mix recent input bits, decoded via Viterbi algorithm.  
- **Reed-Solomon codes**: Used in CDs, Blu-rays, cable modems.  
- **LDPC (Low-Density Parity-Check)**: Modern state-of-the-art, used in Wi-Fi, LTE, DVB.  

---

## 5. Detection vs. Correction

- **Automatic Repeat reQuest (ARQ):**  
  - Detect errors, retransmit.  
  - Efficient for **bursty errors**.  

- **Forward Error Correction (FEC):**  
  - Encode with redundant bits to correct errors at receiver.  
  - Critical for **satellites** and **real-time media (VoIP, video conferencing)**.  

### Cases
1. **Random Errors (BER ~ 0.001):**  
   - Correction cheaper (10 check bits) vs. detection + retransmission (633 bits).  
2. **Bursty Errors:**  
   - Detection cheaper (≈34 bits) vs. correction (>1000 bits).  
3. **Teleconference (e.g., Zoom/Skype):**  
   - No retransmission → tolerate small errors.  
   - Correction adds delay, so often ignored.  

---

## Summary

- **Framing** converts bit streams into frames (byte stuffing, bit stuffing).  
- **Error detection**: parity, checksum, CRC → identify corrupted frames.  
- **Error correction**: Hamming, Reed-Solomon, LDPC → recover data without retransmission.  
- **Hamming distance** determines detection/correction capability.  
- **Strategy choice (ARQ vs. FEC)** depends on error type and application (random, bursty, real-time).  
