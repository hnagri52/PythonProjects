# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:40:48 2020

@author: Christopher John Risi, Hussein Nagri, Thomas Zerbs
"""

import os
import wave
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from pydub import AudioSegment
from pydub.playback import play

###Function that does the Phase 1 Sound Processing
def phase1Task3(filename, playSound_Y_N="Y", writeNewFileOveride="Y"):
    #3.1 Create audio file wave object
        sound_signal = wave.open(filename, 'r')
        wav_sound = AudioSegment.from_file(file = filename)
        
        input_sound_channels = wav_sound.channels
        input_sound_framerate = wav_sound.frame_rate
        input_sound_max_amplitude = wav_sound.max
        input_sound_length = len(wav_sound)
        print("Summary Information of" ,filename, "\n")
        print("\t Sound Channels: This sound file has", "one channel therefore it's mono." if input_sound_channels == 1 else "two channels therefore it's stereo. The soundfile will be adjusted to mono format.")
        print("\t Sampling Rate: The sampling rate of the inputted sound file is ", input_sound_framerate/1000, "kHz. \n", "\t\t - The framerate will be downsampled to 16 kHz and saved as a new file." if input_sound_framerate > 16000 else "")
        print("\t Loudness: The maximum amplitude of this sound file is", str(input_sound_max_amplitude) + ".")
        print("\t Length: This audio file is", input_sound_length/1000, "seconds long.")
        
    #3.2 Check whether the input is stereo or mono, adjust to mono if stereo.
        if input_sound_channels == 2:
            wav_sound = wav_sound.set_channels(1)
        
    #3.3 Play the sound in Python
        if playSound_Y_N == "Y": 
            print("You are now listening to:", filename)
            play(wav_sound)
            cos_wav = AudioSegment.from_file(file = "cos_1kHz.wav")
            play(cos_wav)
        else: 
            print("User requested that", filename, "to not be played.")
    
    #3.6 Check if sampling rate of the input signal is 16 kHz.
    ## If it's greater than 16 kHz downsample to 16 kHz, if it is great
        if input_sound_framerate > 16000:
            wav_sound = wav_sound.set_frame_rate(16000)
    
    #3.4 Write the sound to a new file if specified by user AND the audio parameters have been altered.
        if (input_sound_framerate > 16000 or input_sound_channels == 2) and writeNewFileOveride=="Y":
            print("A new file has been written using the name:", filename[:-4] + "16kHzMono.wav")
            new_name = filename[:-4]+"16kHzMono.wav"
            wav_sound.export(out_f=new_name, format="wav")
    
    #3.5 Plot the sound waveform as a function of sample number
    
        # Read all frames from wave object 
        signal_frames = sound_signal.readframes(-1)
        soundwave_ = np.frombuffer(signal_frames, dtype='int16')
             
        time_stamps = np.linspace(start=0,
                              stop=len(soundwave_)/input_sound_framerate,
        					  num=len(soundwave_))
        
        
        plt.title(filename + " Soundwave")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.plot(time_stamps, soundwave_, label=filename, alpha=0.6)
        plt.legend()
        plt.savefig(filename[:-4]+'.png')
        plt.show()
        
        #3.7 Create cosin function that oscillates at 1 kHz.
        time_stamps_cos = np.arange(start=0, stop=2*np.pi/1000, step=1/16000)
        coswave = 500*np.cos(2*np.pi*1000*time_stamps_cos)
        plt.title("Cosine Wave Oscillating at 1 kHz")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
      
        startPlot = int(round(input_sound_length/2,0))
        endPlot = startPlot+33
      
        
        plt.xlabel("Time (ms)")
        plt.plot(1000*time_stamps_cos[0:33], coswave[0:33], label="500*cos(2*pi*1000*t)", alpha=0.6)
        plt.plot(1000*time_stamps_cos[0:33], soundwave_[startPlot:endPlot], label=filename, alpha=0.6, color="r")
        plt.savefig('1kHzCosine.png')
        plt.legend()
        plt.show()
        
        return soundwave_

### END OF FUNCTION

### This portion of the code was written to be able to loop through all of the sound files in your working directory.
### I've left it commented out because of the large number of sound files to be tested. Obviously you would need to ...
### ...change the file path to be relevant to your own working directory.
##  Main Loop      
#directory = r'C:\Users\resse\OneDrive\Documents\University\University of Waterloo\SYDE252\Project\Phonemes Examples\ForSubmission'
#
#for filenameDir in os.listdir(directory):
#    if filenameDir.endswith(".wav"):
#        phase1Task3(filename=filenameDir, playSound_Y_N="Y", writeNewFileOveride="N")
#    else:
#        continue      

## Example Function Run:  
#phase1Task3(filename='BabyElephantWalk6016kHzMono.wav', playSound_Y_N="Y", writeNewFileOveride="Y")

sound = phase1Task3(filename='cons_k_22_pdl.wav', playSound_Y_N="N", writeNewFileOveride="Y")

print(sound)
print("hello")
len(sound)


###################################################################################################
###################################################################################################
############PHASE 2#######################PHASE 2####################PHASE 2#######################
###################################################################################################
###################################################################################################


from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y



#Task 4, 5, 6
def task4BandFilter(bandEndpoints = [100,200,400,800,1600,3200,6400,7999] ,order=4, sampleFrequency=16000, sound_signal=sound):
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz

    # Sample rate and desired cutoff frequencies (in Hz).
    fs = sampleFrequency
    bandEndpoints.sort()

    # Plot the frequency response for a few different orders.
    plt.figure(1)
    plt.clf()
    
    for lowcut, highcut in zip(bandEndpoints,bandEndpoints[1:]):
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
        w, h = freqz(b, a)
        plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="band = {}-{}".format(lowcut, highcut))

    plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],'--', label='sqrt(0.5)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.grid(True)
    plt.legend(loc='upper right')

    # Filter a noisy signal.
    T = len(sound_signal)/fs
    nsamples = len(sound_signal)
    t = np.linspace(0, T, int(nsamples), endpoint=False)
    x = sound_signal
    pick_order = order
    
    ## Determine the number of bands
    num_of_bands = len(bandEndpoints)
    y_values = []

    for i in range(1, num_of_bands):
       y_values.append(butter_bandpass_filter(data=x, lowcut=bandEndpoints[i-1], highcut=bandEndpoints[i], fs=16000, order=pick_order))

    LineColors = ['b','g','r','c','m','y','k'] ###
    
    fig, axs = plt.subplots(len(bandEndpoints), figsize=(15,20), sharey='col')  
    axs[0].plot(t, x, label='Input Signal')
    
    for j in range(1,len(y_values)+1):
        axs[j].plot(t,y_values[j-1], label='Filtered signal {} Hz -{} Hz'.format(bandEndpoints[j-1], bandEndpoints[j]), color=LineColors[j%len(LineColors)])
    
     
    
    for k in range(0,len(bandEndpoints)):
        axs[k].grid()
        axs[k].legend(loc='upper right')
        axs[k].set_xlabel('time (seconds)')
        

    plt.tight_layout(pad=3.0)
    plt.show()

    return(y_values)


BPF = task4BandFilter(bandEndpoints = [100,150,200,250,300,400,600,800,1200,1600,3200,6400,7999])


###TASK 7###
def BPF_rectified(BPF):
    for i in range(len(BPF)):
        for j in range(len(BPF[i])):
            BPF[i][j] = abs(BPF[i][j])

    return BPF

Rectified_BPF = BPF_rectified(BPF=BPF)


#Task 8

def envelope_extraction(order, nyq_frequency, rectified_obj):











