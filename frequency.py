import numpy.fft as fft
import librosa as lr
from glob import glob
import matplotlib.pyplot as plt
import librosa.display

# Reduce sample rate to 5000 to plot
SAMPLE_RATE = 5000
SAMPLING_SPACING = 1 / SAMPLE_RATE

# Loading the audio in the time-intensity domain
def load_audio():
	audio, sfreq = lr.load("./C_Maj.wav", SAMPLE_RATE)
	return audio

# Summary to compute frequency
# 1. Get array of fft output as complex numbers
# 	- Each complex number refers to a sin/cos wave at the given frequency bin
#	- Audio is made up of many waves at different freq
#	- The complex number tells us the magnitude (intensity) and phase of a wave the given frequency
#
# 2. Choose an index (which corresponds to a bin id)
#	- Note: to find most intense frequency, use index of max(abs(complex num))
#
# 3. To find frequency: Multiply the bin id by the size of frequency bin
#	- bin_id * sample rate / # samples
#
# 4. To find intensity: Compute abs(complex num) at the index
# 
# This allows us to find the intensity at different frequencies!  Which gives us the frequency-intensity domain.
#
# Additional notes
# Max frequency that can be detected is sample rate / 2
# Only half of the fft output is useful
def detect_freq(audio):
	# spec is output of fft as complex numbers
	spec = fft.fft(audio)

	# number of samples is length of spec
	num_samples = len(spec)

	# number of frequency bins is half of spec
	num_freq_bins = num_samples // 2

	#fr gives array frequencies that can be outputted since fft is discrete (note: this is not used)
	fr = fft.fftfreq(num_samples, SAMPLING_SPACING)

	plt.bar(fr[:num_freq_bins], abs(spec)[:num_freq_bins])
	plt.xlabel("Frequency")
	plt.ylabel("Intensity")
	plt.title("FFT Output")
	plt.show()

# In progress
def find_max_freq(spec):
	freq_arr = abs(spec)[:len(spec)//2].argsort()[-1:][::-1]

	for i in range(len(freq_arr)):
		freq = freq_arr[i] * SAMPLE_RATE / num_samples
		print(freq)

if __name__ == "__main__":
	audio = load_audio()

	detect_freq(audio)
	find_max_freq(spec)

# Resources
# https://stackoverflow.com/questions/4364823/how-do-i-obtain-the-frequencies-of-each-value-in-an-fft
# https://stackoverflow.com/questions/6740545/understanding-fft-output
# https://stackoverflow.com/questions/3694918/how-to-extract-frequency-associated-with-fft-values-in-python

