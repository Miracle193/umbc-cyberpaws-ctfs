# Fall 2023 - Week 3: Ziplocked, You Rock!

### Category: Crypto

### Files: challenge.zip

### Description: 
We recovered this seemingly benign zip file from the computer of a known cybercriminal. It seems impossible to open without the password, but we need to get inside. We believe that the criminal may have been trying to hide data inside of the archive so that they can elude authorities. 

Interestingly, despite the advanced nature of this criminal, the other passwords we recovered on their machine could easily be found on a common password list. 

Maybe this archive uses a similarly weak password. Download the zip file and do what you can and try to open it. We think important data is inside. 

### Solution:
Looking at the description of this CTF, the first phrase that stood out to me was "common password list" and I immediately thought of John the Ripper which is a popular and powerful open-source password cracking tool primarily used to detect weak passwords by attempting to crack password hashes using various methods. 

The first step I took was to extract the hash from the zip file. This hash would also contain the hash of the password:
```bash
zip2john challenge.zip > challenge.hash
```

The next step is to crack the password using a list of passwords:
```bash
john ---wordlist=rockyou.txt challenge.hash
```

I set the wordlist as the `rockyou.txt` file provided in this CTF challenge. Similarly, John the Ripper has a common list of passwords stored usually in the `/usr/share/wordlists/rockyou.txt` directory or you can also just run `john challenge.hash`.

After running the command, this output the password:
```bash
spongebob (challenge.zip/flag.txt)
```
Similarly, you can also run the command `john --show challenge.hash` to show the password.

Using the cracked password to extract the challenge.zip file, the flag can be retrieved in the `flag.txt` file: 
```
Paws{n1c3_on3_sup3rst4r!}
```