import sys

encoded_flag = str(sys.argv[1])
SPIN = 4124
ROT = 58

# First, undo the second ROT operation
encoded_flag = list(encoded_flag)
for i, _ in enumerate(encoded_flag):
    newchar = (((ord(encoded_flag[i]) - 33) - ROT) % 93 + 93) % 93 + 33
    encoded_flag[i] = chr(newchar)
encoded_flag = ''.join(encoded_flag)

# Then, reverse the SPIN (rotate back)
spin_amount = SPIN % len(encoded_flag)
encoded_flag = encoded_flag[-spin_amount:] + encoded_flag[:-spin_amount]

# Undo the first ROT operation
encoded_flag = list(encoded_flag)
for i, _ in enumerate(encoded_flag):
    newchar = (((ord(encoded_flag[i]) - 33) - ROT) % 93 + 93) % 93 + 33
    encoded_flag[i] = chr(newchar)
decoded_flag = ''.join(encoded_flag)

print(decoded_flag)
