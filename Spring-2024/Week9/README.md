# Spring 2024 - Week 9: Unbreakable Encryption

### Category: Crypto

### Files: crack_this.py AND encrypted_flag.txt (week9_files)

### Description: 
You've been tasked with reverse engineering an encryption system being used by a group of cyber criminals. Luckily for you, your team has managed to recover the python code for the encryption program. The bad news is that they couldn't get their hands on the decryption code. Worse yet, there's a crucial message (encrypted_flag.txt) that needs to be decrypted ASAP. 

See if you can figure out a way to find the text that produces the encrypted flag when run through the attached program.

### Solution:
There are to ways to solve this CTF; either to decode the flag manually by working your way backwards through the code or by creating a decryption code which is the reverse of the encryption code. I created the decryption code and ran the `encrypted_flag.txt` with `decode.py`

A summary of what the encryption is doing:
1. The flag is converted to a list.
2. The flag then goes through a character rotation.
3. The flag is converted back to a string.
4. The flag then goes through a string rotation.
5. The flag is coverted to a list again.
6. The flag then goes through a character rotation again.
7. The flag is converted back to a string again and returned.

Flag is `Paws{l1t3r4lly_unbr3ak4bl3}`
