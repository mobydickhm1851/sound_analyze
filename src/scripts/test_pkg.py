# /usr/bin/

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt


'''Default
'''
fs = 44100 # 48000
sd.default.samplerate = fs
sd.default.channels = 2

duration = 3  # seconds
#myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
#myrecording = sd.rec(int(duration * fs))
myrecording = sd.rec(int(duration * fs), dtype='float64')
sd.wait() #hold the process till the recording finished
print("recording finished")

#myrecording = sd.playrec(myrecording, fs, channels=2)
#sd.play(myrecording, fs)
#sd.wait() #hold the process till the playback finished
#print("playback finished")


''' Plot in time domain
'''
plt.figure(1)
arrt = np.arange(0,duration, 1/fs)
arrch1 = myrecording[:,0]
arrch2 = myrecording[:,1]
plt.plot(arrt, arrch1)
plt.xlabel("time (t)")
plt.ylabel("$f (x)$")

''' Use fft to plot in frequency domain
'''
plt.figure(2)
timestep = 1/fs
n = arrch1.size
freq = np.fft.fftfreq(n, d=timestep)
fft_result_1 = np.fft.fft(arrch1, n)
rpart_1 = fft_result_1.real
ipart_1 = fft_result_1.imag
amp = np.sqrt(np.power(rpart_1, 2) + np.power(ipart_1, 2))
plt.plot(freq, amp)
plt.xlim(0,10000)
plt.xlabel("frequency (hz)")
plt.ylabel("$f_{hat} (x)$")


''' tune up the pitch
'''
#UPBY = 100
#new_result = fft_result_1.real + UPBY
new_result = fft_result_1 


''' Inverse fft
'''
inv_fft = np.fft.ifft(new_result, n)
plt.figure(3)
t = np.arange(0, n*timestep, timestep)
plt.plot(t, inv_fft.real)

''' playback after inverse_fft
'''
sd.play(inv_fft.real, fs)
sd.wait() #hold the process till the playback finished
print("playback finished")


plt.show() #plot all figures

