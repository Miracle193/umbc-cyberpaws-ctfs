# Fall 2024 - Week 11: Object of My Ire

### Category: Forensics

### Files: transferredFile.pcapng

### Description:
I accidentally deleted an image I needed for a power point! Luckily I always record my network traffic and remembered that I had originally had to move the file onto my computer, could you get the file back for me?

### Solution
Open the `transferredFile.pcapng` in Wireshark. Since we are recovering a deleted image file, the obvious is to export the file. Navigate to File -> Export Objects -> FTP-DATA... and save the cat.jfif file.

Once the file has been saved, open the image to retrieve the flag.

Flag is `Paws{n3tw0rk_0bjects}`
