# Fall 2024 - Week 5: A Beautiful Park

### Category: Forensics

### File: whereIsThisImage.jpg

### Description:
I cant remember what National Park I took this picture at, could you help me out? Flag format: snake_case, Paws{name_national_park}

### Solution:
For the CTF, we will use the exiftool command:

```bash
exiftool whereIsThisImage.jpg
```

This outputs the geolocation of the picture: `38 deg 28' 45.83" N, 78 deg 27' 15.14" W`. Navigate to Google Maps and enter the geolocation replacing "deg" with '°': `38°28'45.8"N 78°27'15.1"W`.

Flag is `Paws{shenandoah_national_park}`
