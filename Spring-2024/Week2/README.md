# Spring 2024 - Week 2: Choo Choo!

### Category: Crypto

### Files: trainsrideon.txt

### Description: 
You've been made lead investigator on a railway company related fraud scheme. The FBI has been trying to catch the fraudsters for years, and finally, they managed to capture one of the fraudster's dead drops, hidden under an old boxcar. You're the best detective we've got, can you figure out what this strange sequence of text, numbers, and dots could mean? 

(Your submission will contain numbers, punctuation, and letters, all lowercase, and underscores. It should be surrounded by Paws, like so: Paws{this_1snt_th3_fl4g!} 

### Solution:
I first tried to decipher the ciphertext with ROT13 and using brute force Caesar cipher decoder but those unfortunately did not work. After many attempts, I decided to look at the hint:

Hint: Maybe these railway fraudsters like railroads a little too much, maybe even to the extent that they might use the railway theming in their cipher mechanisms, too?

After reviewing the hint, I navigated to the CyberChef site and searched for the recipe 'Rail' and the 'Rail Fence Cipher Decode' popped up. Setting the key as 3 and the offset as 0, I was able to obtain the flag.

The Flag is `Paws{1_l1k3_tr41n5_th3y_4r3_sup3r_fun!}`


NOTE: The Rail Fence Cipher is a type of transposition cipher, which means it encrypts a message by rearranging the letters rather than substituting them. It's named for its resemblance to a zigzag or "rail fence" pattern, where letters are written in a diagonal pattern across multiple "rails" and then read off in rows.
