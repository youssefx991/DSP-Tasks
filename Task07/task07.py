import numpy as np
import matplotlib.pyplot as plt


def read_output_signal(file_name):
    indices=[]
    samples=[]
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=float(L[0])
                V2=float(L[1])
                indices.append(V1)
                samples.append(V2)
                line = f.readline()
            else:
                break
    return indices,samples
def test_dft(amplitudes, phases):
    expected_amplitudes, expected_phases = read_output_signal("Output_Signal_DFT_A,Phase.txt")
    result = SignalComapreAmplitude(amplitudes, expected_amplitudes)
    if result:
        print("Amplitude Test Case Passed")
    else:
        print("Amplitude Test Case Failed")
    
    result = SignalComaprePhaseShift(phases, expected_phases)
    if result:
        print("Phase Test Case Passed")
    else:
        print("Phase Test Case Failed")
    
    
def test_idft(indices, samples):
    expected_indices, expected_samples = read_output_signal("Output_Signal_IDFT.txt")
    result = SignalComapreAmplitude(indices, expected_indices)
    if result:
        print("Indices Test Case Passed")
    else:
        print("Incices Test Case Failed")
    
    result = SignalComapreAmplitude(samples, expected_samples)
    if result:
        print("Samples Test Case Passed")
    else:
        print("Samples Test Case Failed")
def DFT(gui):
    indices = gui.current_indices_one
    samples = gui.current_samples_one
    gui.dft_real, gui.dft_imag, gui.dft_amp, gui.dft_phase = perform_dft(indices, samples)
    print("dft_real = ", gui.dft_real)
    print("dft_imag = ", gui.dft_imag)
    print("dft_amp = ", gui.dft_amp)
    print("dft_phase = ", gui.dft_phase)
    test_dft(gui.dft_amp, gui.dft_phase)

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
    test_idft(gui.idft_indices, gui.idft_samples)

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
    


#Use to test the Amplitude of DFT and IDFT
def SignalComapreAmplitude(SignalInput = [] ,SignalOutput= []):
    if len(SignalInput) != len(SignalOutput):
        return False
    else:
        for i in range(len(SignalInput)):
            if abs(SignalInput[i]-SignalOutput[i])>0.001:
                return False
            # elif SignalInput[i]!=SignalOutput[i]:
            #     return False
        return True

def RoundPhaseShift(P):
    while P<0:
        p+=2*math.pi
    return float(P%(2*math.pi))

#Use to test the PhaseShift of DFT
def SignalComaprePhaseShift(SignalInput = [] ,SignalOutput= []):
    if len(SignalInput) != len(SignalOutput):
        return False
    else:
        for i in range(len(SignalInput)):
            A=round(SignalInput[i])
            B=round(SignalOutput[i])
            if abs(A-B)>0.0001:
                return False
            # elif A!=B:
            #     return False
        return True

