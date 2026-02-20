def rc4(key, plaintext):
    # Key Scheduling Algorithm (KSA)
    S = [i for i in range(8)]  # S[i] = i for i = 0 to 7
    T = [key[i % len(key)] for i in range(8)]  # T[i] = K[i mod |K|]
    print(f"Initial S: {S}")
    print(f"Initial T: {T}")
    j = 0
    for i in range(8):
        j = (j + S[i] + T[i]) % 8
        S[i], S[j] = S[j], S[i]
        print(f"KSA Step {i}: S = {S}, j = {j}")

    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    ciphertext = []
    print("Starting PRGA...")
    for idx, Mi in enumerate(plaintext):
        i = (i + 1) % 8
        j = (j + S[i]) % 8
        S[i], S[j] = S[j], S[i]
        k = (S[i] + S[j]) % 8
        Ci = Mi ^ S[k]
        ciphertext.append(Ci)
        print(f"PRGA Step {idx}: i = {i}, j = {j}, k = {k}, S[k] = {S[k]}, Mi = {Mi}, Ci = {Ci}, S = {S}")

    return ciphertext

# Example usage
key = [4, 2, 1, 3]
plaintext = [2, 1, 3, 2]
ciphertext = rc4(key, plaintext)
print("Ciphertext:", ciphertext)