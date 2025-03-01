# Spring 2025 - Week 3: Panic! At the Kernel

### Category: Forensics

### Files: treasuremap.jpg, treasurehunt.py

### Description:
Yes, it happened again. As I'm sure you're already aware, our company was hit with another ransomware attack. Phishing emails, am I right? Well, we paid the ransom (against my better judgment), and everything was supposed to be fine. But Jenkins decided to be "funny" instead of keeping things professional. He thought it would be hilarious to heckle the ransomware operators. 

Turns out, they value their pride almost as much as they value my money, and they activated the ransomware’s self-destruct mechanism. Click, click, boom. Simulated kernel panic. They nuked our critical server into a death spiral of failed reboots. Three times it tried to recover, and three times it crashed again. Now it’s completely stuck, and the poor thing was only up 36 maybe 37 hours. 

Fortunately, the ransomware’s seppuku signal uses a toggle mechanism. The same key that brought it down should be able to bring it back up. It’s in the kernel panic syslogs somewhere. Find it, yea? 

You deal with that and I'll deal with Jenkins.

### Solution:

Flag is ``

