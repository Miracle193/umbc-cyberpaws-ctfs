# Fall 2024 - Week 6: Blood in the Water

### Category: Forensics

### File: PCAPdroid_28_Sep_11_48_45.pcap

### Description:
Larry the Shark really loves wires and strings for some reason, rather than loving Jason Statham like a normal shark of his stature. This particular prey starts with "{C", Larry can smell it from over a mile away (also, his weirdly keen electromagnetic sensors)! Find him dinner. (Encase the string in Paws{}, with the brackets being the same as those in the string - don't double bracket.)

### Solution:
Open the pcap file in Wireshark and filter for the frame that contains the string "{C":
```
frame contains "{C"
```

Flag is `Paws{Cyb3rD0gg0z}`
