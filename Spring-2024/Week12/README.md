# Spring 2024 - Week 12: Final Paper

### Category: Forensics

### Files: FINAL_PAPER_v3.pdf

### Description: 
You've received a frantic message from your friend, who is in a state of panic. It turns out that their final paper, crucial for graduation, has been corrupted and rendered unreadable due to a mysterious issue with the PDF file. They've reached out to you for help, knowing your expertise in digital forensics and file recovery.

Your task is to analyze the corrupted PDF file, identify the root cause of the corruption, and restore it to its original state so that your friend can submit it before the deadline. Time is of the essence, and your friend's academic future hangs in the balance.

### Solution:
To analyze the file for corruption we first analyze the pdf using pdfinfo:
```bash
pdfinfo FINAL_PAPER_v3.pdf
```
This outputs a syntax warning that warns the file may not be a valid PDF which confirms the file is corrupted.

To further analyze the pdf file, we will inspect the beginning of the file to check if it starts with `%PDF-`:
```bash
xxd FINAL_PAPER_v3.pdf | head
```
The output shows that `%PDF-` is missing from the header.

We analyze the end of the pdf file once more to check if it ends with `%%EOF`:
```bash
xxd FINAL_PAPER_v3.pdf | tail
```
The output shows that `%%EOF` is present at the end of the file.

To add `%PDF-` in the header of the pdf file, we first extract the hex of the file:
```bash
xxd FINAL_PAPER_v3.pdf > file.hex
```
Open `file.hex` and add `%PDF-` to the beginning of the bytes and `25 50 44 46 2D` to the beginning of the hex and save. Then run the following command to extract the fixed pdf file:
```bash
xxd -r file.hex FIXED.pdf
```

Flag is ` Paws{F1X3D_TH3_S1GN4TUR3}`
