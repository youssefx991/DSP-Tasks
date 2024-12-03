import numpy as np
from Task07.TestCases import *

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