def decrypt_xor(encoded_string):
    decrypted = ''.join([chr(ord(c) ^ 3) for c in encoded_string])
    return decrypted

# Example usage:
with open('encrypted_flag.txt', 'r') as f:
    encrypted_flag = f.read().strip()

flag = decrypt_xor(encrypted_flag)
print("Decrypted flag:", flag)