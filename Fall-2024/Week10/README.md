# Fall 2024 - Week 10: Turing Test

### Category: Crypto

### Files: Turing_Message.txt

### Description:
Alan Turing, a pioneering mind in computing, left us with many puzzles. We've found a mysterious set of hexadecimal values, but there's a twist—they've been XOR'ed with a significant year from his life. Can you uncover the message hidden beneath?

Your task is to identify the year, use it to XOR the hex values, and retrieve the original message. Dig into Turing's legacy, decode the values, and reveal what lies hidden.

49,73,6e,61,62,46,6c,60,70,7c,7e,4d,41,5d,4b,4d,5a,7a,6b,7b,6a,66,76,62,71,77,6b,6f

### Solution:
This CTF is pretty straight forward so we will head over to CyberChef to decrypt the ciphertext. 

In CyberChef, copy and paste the ciphertext, add 'From Hex' in the recipe, then 'XOR' with the key of 1912 (Turing's birth year).

Flag is `Paws{Turing_XOR_Christopher}`
