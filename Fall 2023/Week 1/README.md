# Fall 2023 - Week 1: Code Words

### Category: Crypto

### Files: book_reviews.pdf

### Description: 
An insider from a suspected cybercriminal group has tipped us off. Every month, they use a specific code word or phrase to authenticate members in their underground forum. 
This month, the code word is hidden within a book review posted in an online book club. Look through these reviews and decode the message to find the key.
What is the special phrase hidden by the cybercriminals?

### Solution:
To solve this, the first thing I did was to open and read the book_reviews.pdf file. The first thing that stood out to me immediately was the text, UGF3c3dkMG4ndF9QNG4xY30= which appears to be encoded in base64.

To decode this, on my Kali Linux VM I ran the following command:
```bash
echo "UGF3c3dkMG4ndF9QNG4xY30=" | base64 -d
```

This output the key:
```bash
Paws{d0n't_P4n1c}
```