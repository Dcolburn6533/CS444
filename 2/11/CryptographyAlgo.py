#Dylan Colburn 
#RC4 Implementation 
#2/11/2026

def encrypt_rc4(message, key): 

    # KSA (Key-Scheduling Algorithm)
    S = list(range(8))
    K = list(key)
    T = [K[i % len(K)] for i in range(8)]
    print(f"Initial T: {T}")
    j = 0
    temp = S.copy()  # Temporary vector to show steps
    for i in range(8):
        j = (j + S[i] + T[i]) % 8
        S[i], S[j] = S[j], S[i]
        print(f"KSA Step {i}: S = {S}, j = {j}, temp = {temp}")
        temp[i] = S[i]  # Update temp to reflect changes

    # PRGA (Pseudo-Random Generation Algorithm) and encryption
    i = j = 0
    out = bytearray()
    for m in message:
        i = (i + 1) % 8
        j = (j + S[i]) % 8
        S[i], S[j] = S[j], S[i]
        k = (S[i] + S[j]) % 8
        out.append(m ^ S[k])
    return bytes(out)



if __name__ == "__main__":
    key = b"4213"  # bytes
    pt = b"2132"  # bytes
    ct = encrypt_rc4(pt, key)
    print(f"Cipher (Hex): {ct.hex()}")