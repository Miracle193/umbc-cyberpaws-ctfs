# Fall 2023 - Week 5: Strange File

### Category: Reverse Engineering

### Files: strange_file.exe

### Description: 
This file was found on one of our employee's computers, and he doesn't know how it got there. We've had some problems with malware, and we want to make sure his computer wasn't infected. 

As our company malware analyst, your job it to examine this file and determine its purpose. Can you analyze the file and see if there is anything weird or secret about it? (Note: Not actually malware, you can run it)

### Solution:
In order to examine the .exe file, I used the `strings` tool which is used to extract and display readable text from binary files. This can be useful for finding hidden messages or text embedded within files that are otherwise not human-readable, such as images, executables, and other binary formats.
```bash
strings strange_file.exe
```

Reviewing the output, I came across this:
```bash
Hello new analyst! If you are reading this, it means you have
done something productive towards your goal of analyzing this
file. All you need for the flag is the decimal number 21 and this data:
EtbfnQtbrJM=zg<|{rh
```

The instruction above states we need the decimal number 21 and the data which looks like an cipher text (`EtbfnQtbrJM=zg<|{rh`). Initially, I went tried using online tools to decode the data which I thought was encrypted as a Caesar cipher. This obviously didn't work. I navigated to the CyberChef site (https://gchq.github.io/CyberChef) and used the XOR tool, setting the key to the decimal of 21 and viola! It worked!

Flag is `Paws{Dawg_X(or)ing}`
