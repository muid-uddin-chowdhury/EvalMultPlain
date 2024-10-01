from phe import paillier 

# Key generation
public_key, private_key = paillier.generate_paillier_keypair()

# encrypting a plaintext value 
x = 6
encrypted_x = public_key.encrypt(x)

# plaintext multiplier 
a = 3

encrypted_result = encrypted_x * a

print('EvalMultPlain: ', encrypted_result)

# decrypt the result
decrypted_result = private_key.decrypt(encrypted_result)

# output the result
print(f'Result of EvalMultPlain (Paillier): {x} * {a} = {decrypted_result}')