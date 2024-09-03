# Spring 2024 - Week 10: Baby's First Reversing

### Category: Reverse Engineering

### Files: encrypted_flag.txt and reverse_me (week10_files)

### Description: 
The same group of cyber criminals whose python encryption scheme you looked at last week, are back at it again!

This time they're using a compiled C Binary (reverse_me) instead of Python. That means you don't have access to the source code this time around. 

But we still have important messages (encrypted_flag.txt) that need decrypting. We need your help!

### Solution:
For this CTF, I used the Ghidra tool to decompile the functions in reverse_me. The main function performs a XOR encryption of each character in the encrypted flag with `3` to result to the encrypted flag. A breakdown of the code function is found [here](CodeDesc.md)].

To decrypt the encrypted flag, I created a python script which XORs each character with `3`. The code is [here](decrypt.py).

Alternatively, you can navigate to the CyberChef site and decrypt the encrypted string using the XOR tool and setting the HEX value as `3`. 

Flag is `Paws{x0r_4ll_0v3r_ag4in}`
