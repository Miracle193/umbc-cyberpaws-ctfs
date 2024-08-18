# Spring 2024 - Week 1: Files in Files

### Category: Steganography

### Files: birb.jpg

### Description: 
A recent investigation has unveiled a curious set of images intercepted from a suspect known for credit card fraud. While initial assessments by the interception team labeled these images as innocuous, potentially just memes or random pictures, a deeper dive suggests otherwise.

Among these images, one stands out. We are confident that it's a conduit for hidden information.

Employ your skills and tools to uncover any concealed messages that could be the key to cracking this case. Your findings could be the missing link in this puzzling case of clandestine communication.

### Solution:
Since the category of this CTF is steganography, I used the tools `strings` and `exiftool` to see if there was any hidden data in the file which unfortunately were unsuccessful. I then proceeded to use the `binwalk` tool which is a tool used primarily for analyzing, reverse engineering, and extracting data from binary files. It's particularly useful in the context of cybersecurity, forensics, and CTF challenges, where hidden data or embedded files may be concealed within various types of files (such as images, firmware, etc.).

I ran the command:
```bash
binwalk -e birb.jpg
```

The result showed there was a hidden zip file with the file `sus.png` and the hexadecimal of `0x93F7`.

To extract `sus.png`:
```bash
unzip _birb.jpg.extracted/93F7.zip
```

Alternatively, you can run:
```bash
dd if=birb.jpg bs=1 skip=37879 count=6455 of=archive.zip
unzip archive.zip
```

The Flag is `Paws{h1ding_s0m3th1ng}`
