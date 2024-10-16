# Fall 2024 - Week 4: Inside Job

### Category: REV

### File: CyberPaws_Chal_Week4

### Description:
It seems one of our developers has gone rogue, stealing this week's flag and hiding it inside a program. To make matters worse, the program demands a password to reveal the flag. Your mission is to uncover the password hidden within their compiled program, or find a way to bypass the check entirely. Time is running out, and we need that flag back!

### Solution:
Run the command the binary file to get an idea of what it does:
```bash
chmod +x CyberPaws_Chal_Week4
./CyberPaws_Chal_Week4
```
Running the binary file prompts for a password to reveal the flag. This obviously calls for reverse engineering of the binary file to get the password. For this, I used Ghidra on Kali Linux to extract the code for the binary file:
```bash
./ghidraRun
```
The above command will run the Ghidra app on Kali Linux, export the binary file and analyze the file. In the main function of the binary file, we see that the function compares the input string to `secretpassword`, thus `secretpassword` is the password. 

Run the binary file and enter `secretpassword` as the password to retrieve the flag.

Flag is `Paws{d3v_Th0u9ht_It_w4s_S4f3}`
