from Task_Practical.FIR.CompareSignal import *
from Task07.task07 import *
import numpy as np

def create_filter(gui):
    fs = float(gui.fs_txb.get())
    fc = float(gui.fc_txb.get())
    fc1 = float(gui.fc1_txb.get())
    fc2 = float(gui.fc2_txb.get())
    step_attenution = float(gui.step_attenuation_txb.get())
    transition_width = float(gui.tansition_width_txb.get())
    filter_type = gui.display_opt.get()
    test_file = gui.test_file
    
    gui.fs = fs 
    gui.fc = fc
    gui.fc1 = fc1
    gui.fc2 = fc2
    gui.step_attenution = step_attenution
    gui.transition_width = transition_width
    gui.filter_type = filter_type
    
    norm_transition_width = transition_width / fs
    print("norm_transition_width = ", norm_transition_width)
    
    if step_attenution <= 21: # rectangular: 0.9/N
        N = 0.9 / norm_transition_width
        window_func = rectangular_window
    elif step_attenution <= 44: # hanning: 3.1/N
        N = 3.1 / norm_transition_width
        window_func = hanning_window
    elif step_attenution <= 53: # hamming: 3.3/N
        N = 3.3 / norm_transition_width
        window_func = hamming_window
    elif step_attenution <= 74: # blackman: 5.5/N
        N = 5.5 / norm_transition_width
        window_func = blackman_window
    else:
        print("Not valid Step attenuation")
        
    N = int(np.ceil(N))
    if N % 2 == 0:
        N += 1
    
    print("N = ", N)
    N_start = int(-1 * ((N-1) / 2))
    N_end = int(((N-1) / 2))
    h = []
    print("fc = ", fc)
    print("transition_width = ", transition_width)
    print("fs = ", fs)
    
    if filter_type == "low_pass":
        fc_norm = (fc + (transition_width/2))/fs
        print("fc_norm = ", fc_norm)
    elif filter_type == "high_pass":
        fc_norm = (fc - (transition_width/2))/fs
        print("fc_norm = ", fc_norm)
    elif filter_type == "band_pass":
        fc1_norm = (fc1 - (transition_width/2))/fs
        fc2_norm = (fc2 + (transition_width/2))/fs
        print("fc1_norm = ", fc1_norm)
        print("fc2_norm = ", fc2_norm)
    elif filter_type == "band_stop":
        fc1_norm = (fc1 + (transition_width/2))/fs
        fc2_norm = (fc2 - (transition_width/2))/fs
        print("fc1_norm = ", fc1_norm)
        print("fc2_norm = ", fc2_norm)
        
    
    
    for n in range(N_end+1):
        if filter_type == "low_pass":
            if n == 0:
                h.append(2 * fc_norm)  # Sinc at zero
                print("n = ", n)
                print("value = ", 2 * fc_norm)
                print("==========================================")
            else:
                up = np.sin(n * 2 * np.pi * fc_norm)
                down = np.pi * n
                value = up/down
                h.append(value)
                print("low pass")
                print("n = ", n)
                print("up = ", up)
                print("down = ", down)
                print("value = ", value)
                print("==========================================")

        elif filter_type == "high_pass":
            if n == 0:
                h.append(1 - 2 * fc_norm)
            else:
                up = -1 * np.sin(n * 2 * np.pi * fc_norm)
                down = np.pi * n
                value = up/down
                h.append(value)
                print("high pass")
                print("n = ", n)
                print("up = ", up)
                print("down = ", down)
                print("value = ", value)
                print("==========================================")

        elif filter_type == "band_pass":
            if n == 0:
                h.append(2 * (fc2_norm - fc1_norm))
            else:
                up1 = np.sin(n * 2 * np.pi * fc2_norm)
                down1 = np.pi * n
                value1 = up1/down1
                up2 = np.sin(n * 2 * np.pi * fc1_norm)
                down2 = np.pi * n
                value2 = up2/down2
                value = value1 - value2
                h.append(value)

        elif filter_type == "band_stop":
            if n == 0:
                h.append(1 - 2 * (fc2_norm - fc1_norm))
            else:
                up1 = np.sin(n * 2 * np.pi * fc1_norm)
                down1 = np.pi * n
                value1 = up1/down1
                up2 = np.sin(n * 2 * np.pi * fc2_norm)
                down2 = np.pi * n
                value2 = up2/down2
                value = value1 - value2
                h.append(value)

        # else:
        #     print("Invalid filter type")
        #     return None
    
    
    # Apply the selected window
    print("first h = ", h)
    print("window_func = ", window_func)
    window = window_func(N_end+1)
    print("window = ", window)
    # h = [h[i] * window[i] for i in range(N_end+1)]
    for i in range(N_end+1):
        h_val = h[i]
        w_val = window[i]
        product = h_val * w_val
        print("i = ", i)
        print("h[i] = ", h_val)
        print("w[i] = ", w_val)
        print("product =  ", product)
        print("==========================================")
        
        h[i] = product

    print("h = ", h)
    
    print("len of h = ", len(h))
    
    indices = list(range(N_start, N_end+1))
    samples = []
    for i in range(1, N_end+1):
        samples.append(h[-1 * i])
    samples = samples + h
    
    print("indices = ", indices)
    print("samples = ", samples)
    
    if gui.current_indices_one and gui.current_samples_one:
        indices_one = gui.current_indices_one
        samples_one = gui.current_samples_one
        indices_two = indices
        samples_two = samples
        
        
        indices_conv, samples_conv = perform_conv(indices_one, samples_one, indices_two, samples_two)
        gui.current_indices_result, gui.current_samples_result = indices_conv, samples_conv
        gui.display_signal_result_text(gui.current_indices_result, gui.current_samples_result)
        print("==========================================")
        print("Testing Filtered Signal using Convolutional")
        Compare_Signals(test_file, indices_conv, samples_conv)
        print("==========================================")
        
        # Calculate the target length
        target_length = len(samples_one) + len(samples_two) - 1

        # Zero-pad signal and filter
        padded_samples_one = zero_pad(samples_one, target_length)
        padded_samples_two = zero_pad(samples_two, target_length)
        
        # Perform DFT on zero-padded signals
        dft_real_one, dft_imaginary_one, dft_amplitude_one, dft_phase_one = perform_dft(indices_one, padded_samples_one)
        dft_real_two, dft_imaginary_two, dft_amplitude_two, dft_phase_two = perform_dft(indices_two, padded_samples_two)
        
        # print("len of indices = ", len(indices_one))
        # print("len of samples = ", len(samples_one))
        # print("len of dft_real_one = ", len(dft_real_one))
        # print("len of dft_imaginary_one = ", len(dft_imaginary_one))
        # print("len of dft_real_two = ", len(dft_real_two))
        # print("len of dft_imaginary_two = ", len(dft_imaginary_two))
        
        dft_real_result = []
        dft_imaginary_result = []
        for i in range(len(dft_real_one)):
            real_part = dft_real_one[i] * dft_real_two[i] - dft_imaginary_one[i] * dft_imaginary_two[i]
            imaginary_part = dft_real_one[i] * dft_imaginary_two[i] + dft_imaginary_one[i] * dft_real_two[i]
            dft_real_result.append(real_part)
            dft_imaginary_result.append(imaginary_part)
        
        # print("len of dft_real_result = ", len(dft_real_result))
        # print("len of dft_imaginary_result = ", len(dft_imaginary_result))
        
        # Perform IDFT to get the result in the time domain
        result_indices, result_samples = perform_idft(dft_real_result, dft_imaginary_result)
        
        # Adjust result indices to reflect convolution start
        result_indices = adjust_indices(len(samples_one), len(samples_two))
        
        gui.current_indices_result, gui.current_samples_result = result_indices, result_samples
        gui.display_signal_result_text(gui.current_indices_result, gui.current_samples_result)
        
        print("==========================================")
        print("Testing Filtered Signal using Fourier")
        # print("len of indices = ", len(result_indices))
        # print("len of Samples = ", len(result_samples))
        # print("Indices = ", result_indices)
        # print("Samples = ", result_samples)
        Compare_Signals(test_file, result_indices, result_samples)
        
        print("==========================================")
    else:
        gui.current_indices_result, gui.current_samples_result = indices, samples
        gui.display_signal_result_text(gui.current_indices_result, gui.current_samples_result)
        print("==========================================")
        print("Testing Result Filter")
        Compare_Signals(test_file, indices, samples)
        print("==========================================")
        
        
        

def perform_conv(indices_one, samples_one, indices_two, samples_two):
    indices_conv = []
    samples_conv = []
    
    len_one = len(samples_one)
    len_two = len(samples_two)
    len_conv = (len_one + len_two - 1)
    
    samples_conv = [0] * len_conv
    first_index_conv = indices_one[0] + indices_two[0]
    last_index_conv = indices_one[len_one - 1] + indices_two[len_two -1]
    indices_conv = list(range(first_index_conv, last_index_conv + 1))
    
    for n in range(len_conv):
        for m in range(len_one):
            if 0 <= n - m < len_two:
                samples_conv[n] += samples_one[m] * samples_two[n - m]
                
    return indices_conv, samples_conv

# Windows
def rectangular_window(N):
    return [1 for _ in range(N)]
def hanning_window(N):
    total_N = (2*N - 1)
    return [0.5 + 0.5 * np.cos((2*np.pi*n)/total_N) for n in range(N)]
def hamming_window(N):
    total_N = (2*N - 1)
    return [0.54 + 0.46 * np.cos((2*np.pi*n)/total_N) for n in range(N)]
def blackman_window(N):
    total_N = (2*N - 1)
    return [0.42 + 0.5 * np.cos((2*np.pi*n)/(total_N-1)) + 0.08*np.cos((4*np.pi*n)/(total_N-1)) for n in range(N)]

def zero_pad(signal, target_length):
    padded_signal = signal + [0] * (target_length - len(signal))
    return padded_signal

# Adjust indices for the result
def adjust_indices(signal_length, filter_length):
    start_index = -(filter_length // 2)
    end_index = signal_length + filter_length - 2 - (filter_length // 2)
    return list(range(start_index, end_index + 1))