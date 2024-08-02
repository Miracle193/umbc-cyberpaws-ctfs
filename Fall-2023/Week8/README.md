# Fall 2023 - Week 8: Fine Arts & Crafts

### Category: Steganography

### Files: subtle_message.png

### Description: 
From the desk of an esteemed art curator, a mysterious tale has unraveled. A painting, recently auctioned at a lavish gallery, contains more than meets the eye. 

The legend amongst cyber sleuths is that a secret criminal organization has used the artwork to conceal a message vital to their clandestine operations. We've used the latest in restoration technology to delicately scan the painting and present to you an identical digital copy. 

Your mission, should you choose to accept it, is to peel back the layers of this artwork and send back any messages hidden amidst its pixels. 
Can you unveil the painting's secrets and decipher the hidden message?

### Solution:
For this exercise, I used the Ristretto Image Viewer app in Kali Linux to open the subtle_message.png file. Looking at the image, it is clear there is a hidden message written in the white background. To make the hidden message more visible, I open Edit in the menu pane of the app, then click 'Open with ImageMagick (color depth=q16)'. In the ImageMagick app, I clicked Image Edit > Color... and then played around with the pixel to make the hidden message more visible: 

Ciphertext of Flag: `Ufbx{m41Q_h43xfW}`

Reading the hidden message of the image, the riddle mentions using 5 bricks. This may mean that the encryption method used is a Caesar cipher. To decrypt the ciphertext, I naviagated to the site, https://www.dcode.fr/caesar-cipher, entered the ciphertext and the shift number of 5.

Flag is: `Paws{h41L_c43saR}`
