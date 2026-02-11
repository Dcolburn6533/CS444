#Dylan Colburn 
#RC4 Implementation 
#2/11/2026

def encrypt_rc4(message, key): 

    # KSA (Key-Scheduling Algorithm)
    S = list(range(256))
    K = list(key)
    T = [K[i % len(K)] for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA (Pseudo-Random Generation Algorithm) and encryption
    i = j = 0
    out = bytearray()
    for m in message:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = (S[i] + S[j]) % 256
        out.append(m ^ S[k])
    return bytes(out)



if __name__ == "__main__":
    key = b"MyKey"  # bytes
    pt = b"Secure Programming"  # bytes
    ct = encrypt_rc4(pt, key)
    print(f"Cipher (Hex): {ct.hex()}")