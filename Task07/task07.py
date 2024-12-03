import numpy as np
from Task07.TestCases import *
import matplotlib.pyplot as plt

def DFT(gui):
    indices = gui.current_indices_one
    samples = gui.current_samples_one
    gui.dft_real, gui.dft_imag, gui.dft_amp, gui.dft_phase = perform_dft(indices, samples)
    print("dft_real = ", gui.dft_real)
    print("dft_imag = ", gui.dft_imag)
    print("dft_amp = ", gui.dft_amp)
    print("dft_phase = ", gui.dft_phase)
    

def IDFT(gui):
    amplitudes = gui.current_indices_two
    phases = gui.current_samples_two
    real = []
    imag = []
    
    for amplitude, theta in zip(amplitudes, phases):
        real.append(amplitude * np.cos(theta))
        imag.append(amplitude * np.sin(theta))
        
    gui.idft_indices, gui.idft_samples = perform_idft(real, imag)
    gui.current_indices_result, gui.current_samples_result = gui.idft_indices, gui.idft_samples
    
    print("dft_real = ", gui.dft_real)
    print("dft_imag = ", gui.dft_imag)
    print("dft_amp = ", gui.dft_amp)
    print("dft_phase = ", gui.dft_phase)
    print("result_indices = ", gui.idft_indices)
    print("result_samples = ", gui.idft_samples)
    

def perform_dft(indices, samples):
    length = len(samples)
    dft_real = []
    dft_imaginary = []
    dft_amplitude = []
    dft_phase = []
    
    for k in range(length):
        sum_real = 0
        sum_imaginary = 0
        for n in range(length):
            theta = (-2 * np.pi * k * n) / length
            sum_real += samples[n] * np.cos(theta)
            sum_imaginary += samples[n] * np.sin(theta)
        dft_real.append(sum_real)
        dft_imaginary.append(sum_imaginary)
    
    for x, y in zip(dft_real, dft_imaginary):
        r = np.sqrt(x**2 + y**2)
        dft_amplitude.append(r)    
        phase = np.arctan2(y, x)
        dft_phase.append(phase)
    
    return dft_real, dft_imaginary, dft_amplitude, dft_phase
    
def perform_idft(real, imag):
    
    length = len(real)
    result_indices = list(range(length))
    result_samples = []
    
    for n in range(length):
        sum_real = 0
        for k in range(length):
            theta = (2 * np.pi * k * n) / length
            sum_real += real[k] * np.cos(theta) - imag[k] * np.sin(theta)
        result_samples.append(sum_real / length)
    
    return result_indices, result_samples


def plot_frequency(gui):
    
    real = gui.dft_real
    amplitudes = gui.dft_amp
    phases = gui.dft_phase
    fs = int(gui.fs_txb.get())
    
    # Frequency axis
    n = len(real) # anyone will work, all have same length
    freqs = [(fs / n) * k for k in range(n)]

    # Plot Frequency vs Amplitude
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.stem(freqs, amplitudes)
    plt.title("Frequency vs Amplitude")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    
    # Plot Frequency vs Phase
    plt.subplot(1, 2, 2)
    plt.stem(freqs, phases)
    plt.title("Frequency vs Phase")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (Radians)")
    
    plt.tight_layout()
    plt.show()
    
