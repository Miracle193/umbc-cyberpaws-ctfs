# Fall 2024 - Week 12: Is This a Threat? 

### Category: Forensics/OSINT

### Files: hidden.png

### Description:
An image of a character has been getting passed around recently, and, honestly, I'd like to know if it's a threat. Could there be a hidden message within? Analyze the image carefully and uncover the truth. Are they really a threat, or is something else concealed? P.S. If it asks for a password, try guest

### Solution
Since we are analyzing the .png file for hidden data, I used up a couple of tools known for extracting hidden information from image files:

```bash
strings hidden.png
exiftool hidden.png
binwalk hidden.png
```

Unfortunately, known of the above tools were able to extract the hidden message. It was time to use the final tool, `steghide` which is used to extract hidden data embedded in an image file:

```bash
steghide extract -sf hidden.png
```
* `steghide`: The tool used for hiding or extracting data in files.
* `extract`: Specifies that you want to extract data hidden in the file
* `-sf`: Stands for stegofile, the file from which data will be extracted.

Flag is `Paws{i_know_what_you_are}`
