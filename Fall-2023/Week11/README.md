# Fall 2023 - Week 11: Grep Analysis

### Category: Forensics

### Files: dmidecode_output.txt

### Description: 
We recovered data about a hardware dump from a network transfer between a suspicious IP and a known cyber-criminal. 

We know that the cyber-criminal was at a specific Starbucks, but there are so many people there on laptops in the security footage that we can't tell which one is him. To make matters worse, the traffic has been proxied so we can't determine the IP info for the device either.

Because threat actors tend to have preferences for software, we think getting the product name used for the hardware dump can help us narrow it down. 

Can you figure out the product name from this hardware dump? 

(Note: The flag will be the alphanumeric name of the software, in all capitals and no spaces. You will need to surround it with Paws{} before submitting it, like so: Paws{PRODUCTNAME50})

### Solution:
This CTF is pretty straight forward. Since we are simply searching for the product name in the .txt file we will use the grep command line tool:
```bash
grep Product Name dmidecode_output.txt
```

Alternatively, we can use the -i flag which makes the search case insensitive:
```bash
grep -i "Product Name" dmidecode_output.txt
```

Flag is `Paws{21CFCTO1WW}`
