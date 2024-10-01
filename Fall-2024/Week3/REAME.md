# Fall 2024 - Week 3: Who Am I

## Category: OSINT

### Description:
Somewhere within the public information of the amazon.com domain, there’s a clue that will lead you to a relatively well-known location. Your task is to dig into this data and uncover the name of the largest, closest park near the domain's listed registrant address. Think carefully about what tools might reveal a domain's background, and follow the trail to the flag.

Note: Format will be Paws{park_name}, all lowercase. Any and all spaces should be replaced with underscores.

### Solution:
Run the following command in the terminal to get the registrant address of amazon.com domain:
```bash
whois amazon.com
```
The output shows that the registrant's address is in Reno, NV with zip code of 89507. Navigate to Google Maps and search for the location of the registrant's address. Look around the pinpoint of the location for parks. The closest and largest park next to the address is Rancho San Rafael Regional Park.

Flag is `Paws{rancho_san_rafael_regional_park}`