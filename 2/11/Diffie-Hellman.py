#pip install sympy 
# Dylan Colburn
# Diffie Hellman Algorithm Implementation
# 2/11/2026

from sympy.ntheory import isprime, is_primitive_root 

 


if __name__ == "__main__":
    # Assign Publicly shared values  
    p = 17
    g = 3

    if isprime(p) and is_primitive_root(g, p): 
        a = int(input("Alice, enter your private key (a): "))
        b = int(input("Bob, enter your private key (b): "))

    #generate alice_secret 
        alice_secret = pow(g, a, p) #formula from canvas slide 57 (step 3)
        print("Alice secret (A):", alice_secret)
    #generate bob_secret 
        bob_secret = pow(g, b, p) #formula from canvas slide 58 (step 3)
        print("Bob secret (B):", bob_secret)
    #pow(g, a, p) g^a mod p

    

        if alice_secret == bob_secret: 

            print("\nSuccess! Both parties share the same secret key.") 
        else:
            
            
            shared_key_alice = pow(bob_secret, a, p) #formula from canvas slide 59-60 (step 4/5)
            print("Alice computes shared key:", shared_key_alice) 
            shared_key_bob = pow(alice_secret, b, p) #formula from canvas slide 59-60 (step 4/5)
            print("Bob computes shared key:", shared_key_bob)
            if shared_key_alice == shared_key_bob:
                print("\nSuccess! Shared keys match.")
            else:
                print("\nError: Shared keys do not match.")

    else: 
        print("Invalid parameters: p must be prime and g must be a primitive root.") 

    
    