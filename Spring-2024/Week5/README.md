# Spring 2024 - Week 5: [File Carving]

### Category: Forensics

### Files: challenge.pdf

### Description: 
In a recent cyber investigation, we stumbled upon a peculiar PDF file seemingly devoid of any content. However, our digital forensic experts suspect that there may be more to this file than meets the eye.

Despite initial appearances, we believe that this seemingly blank document may hold a hidden secret—a secret that could potentially uncover vital clues to the cybercriminal's activities.

Your task is to delve into the depths of this enigmatic PDF file and unveil the concealed truth within. The fate of the investigation rests in your hands.

Can you carve out the hidden PNG image concealed within the depths of this seemingly innocuous PDF file? 

### Solution:
To begin extracting the .png file, I ran the following using binwalk utility to get the 
byte offset of the .png file:
```bash
binwalk -e challenge.pdf
```

The output shows that the .png file starts in offset of 296.

I then ran the following to extract the .png file:
```bash
dd if=challenge.pdf bs=1 skip=296 count=62 of=extracted_image.png
```

However, when I opened the extracted image, it was a blank .png file. This is likely because my count value was not sufficient to capture the entire .png file.

So I ran the following instead to to extract all embedded files, regardless of type, which can be very effective when you're not sure exactly what you're looking for or when other methods don't work as expected:
```bash
binwalk --dd='.*' challenge.pdf
```

The .png file is saved as `128` in the _challenge.pdf.extracted folder that is generated. Edit the file to a .png file and open the image.

Flag is `Paws{F1L3_C4RV1NG_4_K1DZ}`
