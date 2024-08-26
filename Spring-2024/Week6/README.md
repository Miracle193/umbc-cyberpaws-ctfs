# Spring 2024 - Week 6: Decryption Description

### Category: Crypto

### Files: flag.enc, privatekey.pem, and publickey.pem

### Description: 
Your division has been handed these keys and an encrypted file. In order to decrypt this file, you'll need to use the contents of the keys somehow. Maybe what lies within the keys will give you the clue? 

(The flag will be in Paws{} format inside of the decrypted file, just paste it in when you're done)

### Solution:
From the files given, the encryption is likely using RSA. I used the OpenSSL pkeyutl which performs low-level public key operations using any supported algorithm
```bash
openssl pkeyutl -decrypt -inkey privatekey.pem -in flag.enc -out flag.txt
```

Open the `flag.txt` file.

Flag is `Paws{55H_1s_C00L!}`
