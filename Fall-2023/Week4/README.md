# Fall 2023 - Week 4: Exfiltration Expedition

### Category: Incident Response

### Files: partial_log.png

### Description: 
A significant amount of sensitive data has been unexpectedly transferred out of the company's servers. You've been provided with partial firewall logs from the time of the breach. 

Your role as a cyber incident responder is to analyze these logs and identify potential Indicators of Compromise (IoCs) that could lead you to the culprit's IP address. 

Which source IP warrants further investigation in relation to the data exfiltration incident?

### Solution:
From the description, the key words here are 'significant amount of sensitive data', so when we look at the partial logs we are looking for the source IP address that sent out a huge amount of data.

When reviewing the partial log, the log with the significant amount of data sent is 80MB and the source IP address is 10.1.24.102.

Flag is `Paws{10.1.24.102}`
