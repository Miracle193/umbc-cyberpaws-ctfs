# Fall 2023 - Week 10: Where Am I?

### Category: OSINT

### Files: corrupted_footage.png

### Description: 
We've managed to recover this image from a cybercriminal's hard drive, which appears to show a remote surveillance camera on a small road. 

We've received confirmation that this image contains the vehicle of the criminal. 
Can you determine what state this photograph was taken? 

(Note: The flag will be the name of a state, with all capitals, only letters, no spaces, and should be surrounded by Paws, like so: Paws{NEWSOUTHWALES})

### Solution:
Looking at the corrupted image, the element that stands out is the license plate number on the car. 

Navigate to the https://en.wikipedia.org/wiki/United_States_license_plate_designs_and_serial_formats and search through the images of license plates for each state. Eventually, I found one that was similar to the license plate in the corrupted_footage.png file. This was the state, Oregon.

Flag is: `Paws{OREGON}`
