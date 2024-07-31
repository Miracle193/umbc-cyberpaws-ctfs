# Fall 2023 - Week 7: Network Sleuth

### Category: Forensics

### Files: network_log_device_0632.pcap

### Description: 
You’ve been contracted to investigate a recent ransomware incident at a Fortune 500 company. 

The company suspects that an employee visited a malicious website at work. Luckily, they saved their network logs on an external server that wasn't affected by the attack.

So far, you've deduced which company device was the entrypoint of the attack. Now, your job is to analyze the device's network log and see if you can find the website and any clues about a possible decryption key.

### Solution:
To begin analyzing the .pcap file, I used the WireShark app to open the file. In WireShark, there is an 'Export Objects' function which can be accessed via File > Export Objects > HTTP... to export the html files of the website(s) that were visited. 

I clicked the 'Save All' button to save all the files and I opened the text/html files with a Chrome browser to inspect the websites visited. In the `legit_download.html` source code, the flag can be found `const secretKey = 'Paws{3a49bdecf05784d5b9f409c1ea4b1373}'`.

Flag is `Paws{3a49bdecf05784d5b9f409c1ea4b1373}`
