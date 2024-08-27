# Spring 2024 - Week 7: Priority Voicemail

### Category: Audio/Video

### Files: NewMessage.wav

### Description: 
A critical voicemail notification illuminates your phone's screen. It's from your supervisor. You know this must be important; they rarely use voicemails.  Your fingers tremble slightly as you press play.

The message that follows is a series of distorted sounds, a cryptic sequence that seems nonsensical.  However, your supervisor's final words echo clearly: "Promotion to the first person who deciphers the message."

This is your chance to prove your analytical skills and dedication.  Can you crack the code and unlock your potential within the company? Utilize your critical thinking and research abilities to unravel the hidden message before your colleagues.

### Solution:
This one was a bit tough on me so I looked at the hint:

Do you know anything spectrograms? I heard they can see alot, even things humans can't.

So clearly this CTF is about decoding the spectogram of the audio file. According to Wikipedia, a spectrogram is a visual representation of the spectrum of frequencies of a signal as it varies with time.

To begin this, I downloaded the audio analyzer tool, Sonic Visualiser, on my Kali Linux:
```bash
sudo apt-get install sonic-visualiser
```

Then I ran the tool via the command line:
```bash
sonic-visualiser
```

Navigate throught the app and open the NewMessage.wav file. Click 'Pane' in the window pane and select 'Add Spectrogram > G (All Channels Mixed)'. This would output the spectrogram of the audio file.

Flag is `Paws{H3AR_M3_S33_M3}`
