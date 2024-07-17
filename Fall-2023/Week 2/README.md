# Fall 2023 - Week 2: Family Photo

### Category: Steganography

### Files: EVIDENCE_0024.jpg

### Description: 
New materials just came in for a criminal case. The bulk of the materials includes bank statements, receipts, emails, phone records, and contracts. However, nothing seems to be suspicious or criminal in them. 

There is one piece of evidence that sticks out to us, though. 

Please investigate this photo. It is an image of the suspect and his family. Our forensics guys are telling us this is not as innocuous as it seems.
Can you figure out what data this image might be hiding?

### Solution:
Looking at the decription and category of this CTF, it is clear that we are looking for the hidden text within the .jpg file. One of the tools we can use when examining an image or other files for hidden data is using the `strings` tool. 

`strings` is a command-line utility that is used to extract and display readable text from binary files. This can be useful for finding hidden messages or text embedded within files that are otherwise not human-readable, such as images, executables, and other binary formats.

To extract the hidden data, on my Kali Linux VM I ran the following command:
```bash
strings EVIDENCE_0024.jpg
```

Scanning through the data output, the flag could be found:
```bash
Paws{3X1F_D4T4}
```

Similarly, you can use `exiftool`, a powerful command-line application for reading, writing, and editing metadata information for a variety of file types, including images, audio, and video files, to extract the metadata and hidden data of the image.