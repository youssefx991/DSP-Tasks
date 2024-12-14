import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Task01.Task01 import *
from Task02.task02 import *
from Task01.Task1_testcases_and_testing_functions.DSP_Task2_TEST_functions import *
from Task03.Test_1.QuanTest1 import *
from Task03.Test_2.QuanTest2 import *
from Task05.testcases.Task05_test import *
from Task07.task07 import *
from Task07.TestCases import *
from Task_Practical.Correlation.correlation import *

import numpy as np

class DSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DSP App")

        # Create a notebook (tabs container)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Tab 1: Signal Processing Tab
        self.signal_processing_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.signal_processing_frame, text="Signal Processing")

        # Tab 2: Future Functionality Tab (extend here)
        self.signal_generation_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.signal_generation_frame, text="Signal Generation")

        # Tab 3: Task 3 - Quantization
        self.signal_quantize_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.signal_quantize_frame, text="Signal Quantization")

        # Task 5: Convolution
        self.signal_conv_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.signal_conv_frame, text="Signal Convolution")

        # Task 7: DFT
        self.dft_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.dft_frame, text="DFT")
        
        # Practical: Correlation
        self.corr_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.corr_frame, text="Correlation")

        # Assign functions for creating tabs
        self.create_signal_processing_tab(self.signal_processing_frame)
        self.create_signal_generation_tab(self.signal_generation_frame)
        self.create_signal_quantization_tab(self.signal_quantize_frame)
        self.create_signal_conv_tab(self.signal_conv_frame)
        self.create_signal_dft_tab(self.dft_frame)
        self.create_signal_corr_tab(self.corr_frame)

    # ====================== Practical - Correlation =================================================================
    def create_signal_corr_tab(self, root):
        # Read First Signal Button
        tk.Button(root, text="Read Signal 1", command=self.read_signal_one).pack()
        
        # Read Second Signal Button
        tk.Button(root, text="Read Signal 2", command=self.read_signal_two).pack()
        
        # Read Sampling Frequency
        tk.Label(root, text="Sampling Frequency").pack()
        self.fs_txb = tk.Entry(root)
        self.fs_txb.pack()
        self.fs_txb.insert(0, "100")
        
        # Text widget for displaying the signal 1 text
        tk.Label(root, text="Result Signal 1").pack()
        self.signal_one_display_text = tk.Text(root, height=3, width=75)
        self.signal_one_display_text.pack()

        # Text widget for displaying the signal 2 text
        tk.Label(root, text="Result Signal 2").pack()
        self.signal_two_display_text = tk.Text(root, height=3, width=75)
        self.signal_two_display_text.pack()

        # Text widget for displaying the signal result text
        tk.Label(root, text="Result Signal").pack()
        self.signal_result_display_text = tk.Text(root, height=3, width=75)
        self.signal_result_display_text.pack()
        
        # Text widget for displaying the Time Delay text
        tk.Label(root, text="Time Delay").pack()
        self.signal_time_delay = tk.Text(root, height=3, width=75)
        self.signal_time_delay.pack()
        
        # Text widget for displaying the Signal Class text
        tk.Label(root, text="Signal Class").pack()
        self.signal_signal_class = tk.Text(root, height=3, width=75)
        self.signal_signal_class.pack()

        # Correlation Button
        tk.Button(root, text="Perform Correlation", command=lambda: correlation(self)).pack()
        
        # Time Delay Button
        tk.Button(root, text="Calculate Time Delay", command=lambda: time_delay(self)).pack()
        
        # Class Button
        tk.Button(root, text="Determine_class", command=lambda: signal_class(self)).pack()
        
        # Display Signal 1 plot
        tk.Button(root, text="Display Signal 1", command=self.display_signal_one).pack()

        # Display Signal 2 plot
        tk.Button(root, text="Display Signal 2", command=self.display_signal_two).pack()

        # Display Signal result plot
        tk.Button(root, text="Display Signal result", command=self.display_signal_result).pack()
        
        self.time_delay = []
        self.signal_class = None

    
    # ====================== Task 07 =================================================================
    
    def create_signal_dft_tab(self, root):
        # Text widget for displaying the signal 1 text
        tk.Label(root, text="Signal").pack()
        self.signal_one_display_text = tk.Text(root, height=3, width=75)    # text
        self.signal_one_display_text.pack()
        # Read First Signal Button
        tk.Button(root, text="Read Signal", command=lambda: self.read_signal_one(1,1)).pack() # button

        # Text widget for displaying the signal 2 text
        tk.Label(root, text="DFT Signal").pack()
        self.signal_two_display_text = tk.Text(root, height=3, width=75)    # text
        self.signal_two_display_text.pack()
        # Read DFT Signal Button
        tk.Button(root, text="Read DFT Signal", command=lambda: self.read_signal_two(2,2)).pack() # button

        tk.Label(root, text="Sampling Frequency").pack()
        self.fs_txb = tk.Entry(root)
        self.fs_txb.pack()

        tk.Button(root, text="Perform DFT", command=lambda: DFT(self)).pack()
        tk.Button(root, text="Perform IDFT", command=lambda: IDFT(self)).pack()

        # Text widget for displaying the signal result text
        tk.Label(root, text="Result Signal").pack()
        self.signal_result_display_text = tk.Text(root, height=3, width=75)    # text
        self.signal_result_display_text.pack()
        # Display Signal result plot
        tk.Button(root, text="Display Signal result", command=self.display_signal_result).pack()

        # plot freq and amplitude Button
        tk.Button(root, text="Plot Frequency", command=lambda: plot_frequency(self)).pack() # button
        
        # variables
        self.dft_real = []
        self.dft_imag = []
        self.dft_amp = []
        self.dft_phase = []
        self.idft_indices = []
        self.idft_samples = []
        
        

    # ====================== Task 05 =================================================================
    def create_signal_conv_tab(self, root):
        # Read First Signal Button
        self.read_signal_one_button = tk.Button(root, text="Read Signal 1", command=self.read_signal_one) # button
        self.read_signal_one_button.pack()

        # Read Second Signal Button
        self.read_signal_two_button = tk.Button(root, text="Read Signal 2", command=self.read_signal_two) # button
        self.read_signal_two_button.pack()

        # Getting Window Size for Averaging
        self.window_size_label = tk.Label(root, text="Window Size") # label
        self.window_size_label.pack()
        self.window_size_entry = tk.Entry(root) # entry
        self.window_size_entry.pack()

        # Text widget for displaying the signal 1 text
        self.signal_one_display_label = tk.Label(root, text="Result Signal 1");   # label
        self.signal_one_display_label.pack()
        self.signal_one_display_text = tk.Text(root, height=3, width=75)    # text
        self.signal_one_display_text.pack()

        # Text widget for displaying the signal 2 text
        self.signal_two_display_label = tk.Label(root, text="Result Signal 2");   # label
        self.signal_two_display_label.pack()
        self.signal_two_display_text = tk.Text(root, height=3, width=75)    # text
        self.signal_two_display_text.pack()

        # Text widget for displaying the signal result text
        self.signal_result_display_label = tk.Label(root, text="Result Signal");   # label
        self.signal_result_display_label.pack()
        self.signal_result_display_text = tk.Text(root, height=3, width=75)    # text
        self.signal_result_display_text.pack()

        # Average Signal button
        self.average_signal_button = tk.Button(root, text="Average", command=self.average_signal) # button
        self.average_signal_button.pack()
        
        # First Derivative button
        self.first_diff_button = tk.Button(root, text="First Derivative", command=self.first_derivative) # button
        self.first_diff_button.pack()
        
        # Second Derivative button
        self.second_diff_button = tk.Button(root, text="Second Derivative", command=self.second_derivative) # button
        self.second_diff_button.pack()
        
        # Convolution button
        self.conv_button = tk.Button(root, text="Convolution", command=self.conv_signal) # button
        self.conv_button.pack()
        

        # Display Signal 1 plot
        self.display_one_signal_button = tk.Button(root, text="Display Signal 1", command=self.display_signal_one) # button
        self.display_one_signal_button.pack()

        # Display Signal 2 plot
        self.display_signal_two_button = tk.Button(root, text="Display Signal 2", command=self.display_signal_two) # button
        self.display_signal_two_button.pack()

        # Display Signal result plot
        self.display_signal_result_button = tk.Button(root, text="Display Signal result", command=self.display_signal_result) # button
        self.display_signal_result_button.pack()

    def average_signal(self):
        if self.window_size_entry.get():
            window_size = int(self.window_size_entry.get())
        else:
            messagebox.showerror("ERROR - Window size must be greater than 0")
            return

        if self.current_indices_one and self.current_samples_one:
            indices = self.current_indices_one
            samples = self.current_samples_one
            n = len(samples)
            averaged_samples = []
            averaged_indices = indices[0:n-window_size+1]
            
            for i in range(window_size - 1, n):
                window_start = i - window_size + 1 # actual start of window, could be negative
                start = max(0, window_start) # if it is negative then start from 0
                
                values = samples[start : i + 1] # get all values starting from start to the current index
                total_sum = sum(values) # sum all values in current window
                
                averaged_sample = total_sum / window_size
                averaged_sample = round(averaged_sample, 3) # round to 3 for test cases
                averaged_samples.append(averaged_sample) # average = (sum / #samples)
                
            self.current_indices_result, self.current_samples_result = averaged_indices, averaged_samples
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
            
            compare_signals("MovingAvg_out1.txt", averaged_indices, averaged_samples, window_size)
        else:
            messagebox.showerror("ERROR - Invalid Signal one data")
    
    def first_derivative(self):
        if self.current_indices_one and self.current_samples_one:
            indices = self.current_indices_one
            samples = self.current_samples_one
            
            diff_indices, diff_samples = self.perform_derivative(indices, samples)
            
            self.current_indices_result, self.current_samples_result = diff_indices, diff_samples
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
            
            compare_signals("1st_derivative_out.txt", diff_indices, diff_samples)
        else:
            messagebox.showerror("ERROR - Invalid Signal one data")
            
    def perform_derivative(self, indices, samples):
        n = len(samples)
        diff_samples = []
        diff_indices = indices[0 : n-1]
        for i in range(1, n):
            sample = samples[i] - samples[i-1]
            diff_samples.append(sample)
        
        return diff_indices, diff_samples
    def second_derivative(self):
        if self.current_indices_one and self.current_samples_one:
            indices = self.current_indices_one
            samples = self.current_samples_one
            
            diff1_indices, diff1_samples = self.perform_derivative(indices, samples)
            diff2_indices, diff2_samples = self.perform_derivative(diff1_indices, diff1_samples)
            
            self.current_indices_result, self.current_samples_result = diff2_indices, diff2_samples
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
            
            compare_signals("2nd_derivative_out.txt", diff2_indices, diff2_samples)
        else:
            messagebox.showerror("ERROR - Invalid Signal one data")
    def conv_signal(self):
        if self.current_indices_one and self.current_samples_one and self.current_indices_two and self.current_samples_two:
            indices_one = self.current_indices_one
            samples_one = self.current_samples_one
            indices_two = self.current_indices_two
            samples_two = self.current_samples_two
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
                        
            self.current_indices_result, self.current_samples_result = indices_conv, samples_conv
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
            
            compare_signals("Conv_output.txt", indices_conv, samples_conv)
        else:
            messagebox.showerror("ERROR -- Signals not valid for Convolution")

    # ====================== Task 03 =================================================================
    def create_signal_quantization_tab(self, root):
        # description label
        self.quantization_lbl = tk.Label(root, text="Quantization Settings")
        self.quantization_lbl.pack()

        
        # number of levels
        self.num_levels_lbl = tk.Label(root, text = "Number of Quantization Levels") # label
        self.num_levels_lbl.pack()
        self.num_levels_txb = tk.Entry(root) # textbox
        self.num_levels_txb.pack()

        # number of bits
        self.num_bits_lbl = tk.Label(root, text = "Number of bits") # label
        self.num_bits_lbl.pack()
        self.num_bits_txb = tk.Entry(root) # textbox
        self.num_bits_txb.pack()

        
        # Display Result
        self.quantized_signal_display_lbl = tk.Label(root, text="Quantized Signal")
        self.quantized_signal_display_lbl.pack()
        self.quantized_signal_display_txt = tk.Text(root, height=5, width=75)
        self.quantized_signal_display_txt.pack()

        # Quantize Button
        self.quantize_btn = tk.Button(root, text="Quantize Signal", command=self.quantize_signal)
        self.quantize_btn.pack()

        # Plot Quantized Signal Button
        self.plot_quantized_signal_btn = tk.Button(root, text="Plot Quantized Signal", command=self.plot_quantized_signal)
        self.plot_quantized_signal_btn.pack()

        # Canvas for Matplotlib Figure to show signla plot
        self.canvas = None

    def quantize_signal(self):
        num_levels_str = self.num_levels_txb.get()
        num_bits_str = self.num_bits_txb.get()

        if num_levels_str.strip():
            num_levels = int(num_levels_str)
        elif num_bits_str.strip():
            num_bits = int(num_bits_str)
            num_levels = 2 ** num_bits
        else:
            messagebox.showerror("ERROR - Please enter number of levels or number of bits")

        if self.current_indices_one and self.current_samples_one:
            samples = self.current_samples_one
            quantized_samples, errors, encoded_values, levels = self.perform_quantization(samples, num_levels)
            
            # Display results
            self.quantized_signal_display_txt.delete(1.0, tk.END)
            for sample, error, encoded_value, level in zip(quantized_samples, errors, encoded_values, levels):
                self.quantized_signal_display_txt.insert(tk.END, f"level:{level} encoded:{encoded_value} sample:{sample:.2f} error:{error}\n")


            # QuantizationTest1("Quan1_Out.txt", encoded_values, quantized_samples) # test 1
            # QuantizationTest2("Quan2_Out.txt", levels, encoded_values, quantized_samples, errors) # test 2

            return quantized_samples, errors, encoded_values, levels
        else:
            messagebox.showerror("ERROR - Invalid Signal One")

    def perform_quantization(self, signal, num_levels):
        # Define the range for quantization
        min_val = min(signal)
        max_val = max(signal)

        # Create quantization levels
        level_width = (max_val - min_val) / num_levels
        quantized_signal = []
        quantization_errors = []
        encoded_values = []
        levels = []
        num_bits = int(np.log2(num_levels))

        intervals = []
        midpoints = []

        for i in range(num_levels):
            start = min_val + i*level_width
            end = start + level_width
            midpoint = (start + end)/2
            
            start = round(start, 3)
            end = round(end, 3)
            midpoint = round(midpoint, 3)

            intervals.append((start, end))
            midpoints.append(midpoint)

        
        for sample in signal:
            found = False
            for level, (start, end) in enumerate(intervals):
                if start <= sample <= end:
                    found = True
                    quantized_val = midpoints[level]
                    error = round(quantized_val - sample, 3)

                    encoded_value = format(level, '0{}b'.format(num_bits))
                    encoded_values.append(encoded_value)

                    quantized_signal.append(quantized_val)
                    quantization_errors.append(error)
                    levels.append(level + 1)
                    break
            if not found:
                print("Didn't find any level for sample: ", sample)

        return quantized_signal, quantization_errors, encoded_values, levels

    def plot_quantized_signal(self):
        quantized_samples, errors, encoded_values, levels = self.quantize_signal()
        signal = self.current_samples_one
        indices = self.current_indices_one

        # Create a new window for the plot
        plot_window = tk.Toplevel(self.root)
        plot_window.title("Signal Plot")

        # Create a new figure for the plot
        figure, axis = plt.subplots(3, 1, figsize=(10, 6))  # 1 column for single plot, 2 columns for dual plots
        axis[0].grid(True)
        axis[1].grid(True)
        axis[2].grid(True)
        
        # Original Signal
        axis[0].plot(indices, signal, color='black')
        axis[0].set_title("Original Signal")
        axis[0].set_xlabel("Incices")
        axis[0].set_ylabel("Amplitude")
        
        # Quantized Signal
        axis[1].plot(indices, quantized_samples, color='green')
        axis[1].set_title("Quantized Signal")
        axis[1].set_xlabel("Indices")
        axis[1].set_ylabel("Amplitude")

        # Error
        axis[2].plot(indices, errors, color='red')
        axis[2].set_title("Quantization Error")
        axis[2].set_xlabel("")
        axis[2].set_ylabel("Error")

        # Adjust layout
        plt.tight_layout()

        # Create a canvas for the figure
        canvas = FigureCanvasTkAgg(figure, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # ====================== Task 02 =================================================================

    def create_signal_generation_tab(self, root):

        self.display_opt = tk.StringVar(value="Sin")
        self.sin_radio = tk.Radiobutton(root, text="Sin", variable=self.display_opt, value="Sin")
        self.cos_radio = tk.Radiobutton(root, text="Cos", variable=self.display_opt, value="Cos")
        self.sin_radio.pack()
        self.cos_radio.pack()
        

        self.amplitude_lbl = tk.Label(root, text="Amplitude")
        self.amplitude_txb = tk.Entry(root)
        self.amplitude_lbl.pack()
        self.amplitude_txb.pack()
        self.amplitude_txb.insert(0, "2")

        self.phase_shift_lbl = tk.Label(root, text="Phase shift")
        self.phase_shift_txb = tk.Entry(root)
        self.phase_shift_lbl.pack()
        self.phase_shift_txb.pack()
        self.phase_shift_txb.insert(0, "0.785")

        self.frequency_lbl = tk.Label(root, text="Frequency")
        self.frequency_txb = tk.Entry(root)
        self.frequency_lbl.pack()
        self.frequency_txb.pack()
        self.frequency_txb.insert(0, "5")

        self.fs_lbl = tk.Label(root, text="Sampling Frequency")
        self.fs_txb = tk.Entry(root)
        self.fs_lbl.pack()
        self.fs_txb.pack()
        self.fs_txb.insert(0, "10")

        self.cont_btn = tk.Button(root, text="Display Continious", command=self.display_cont)
        self.disc_btn = tk.Button(root, text="Display Discrete", command=self.display_disc)
        self.both_btn = tk.Button(root, text="Display Both", command=self.display_both)
        self.cont_btn.pack()
        self.disc_btn.pack()
        self.both_btn.pack()

        # Canvas for Matplotlib Figure to show signla plot
        self.canvas = None

    def display_plot(self, signal, time, signal_disc, n, mode:int):
        # Create a new window for the plot
        plot_window = tk.Toplevel(self.root)
        plot_window.title("Signal Plot")

        # Create a new figure for the plot
        figure, axis = plt.subplots(figsize=(10, 6))  # 1 column for single plot, 2 columns for dual plots
        axis.grid(True)
        
        # Check the mode to determine the plotting behavior
        if mode == 1:
            # Only the continuous signal
            axis.plot(time, signal, color='green')
            axis.set_title("Continuous Signal")
            axis.set_xlabel("Time (s)")
            axis.set_ylabel("Amplitude")

        elif mode == 2:
            # Only the discrete signal
            axis.scatter(n, signal_disc, color='red')
            axis.set_title("Discrete Signal")
            axis.set_xlabel("Index")
            axis.set_ylabel("Value")

        else:
            # Both continuous and discrete signals
            axis.plot(time, signal, color='green')
            axis.scatter(n, signal_disc, color='red')
            axis.set_title("Continuous/Discrete Signal")
            axis.set_xlabel("Time (s)/Index")
            axis.set_ylabel("Amplitude/Value")

        # Adjust layout
        plt.tight_layout()

        # Create a canvas for the figure
        canvas = FigureCanvasTkAgg(figure, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def display_cont(self):
        # messagebox._show(message=f"in display_cont {self.display_opt.get()}")
        signal, time, signal_disc, n = generate_signal(self)
        self.display_plot(signal, time, signal_disc, n, 1)

    def display_disc(self):
        # messagebox._show(message=f"in display_disc {self.display_opt.get()}")   
        signal, time, signal_disc, n = generate_signal(self)
        self.display_plot(signal, time, signal_disc, n, 2)

    def display_both(self):
        # messagebox._show(message=f"in display_both {self.display_opt.get()}")
        signal, time, signal_disc, n = generate_signal(self)
        self.display_plot(signal, time, signal_disc, n, 3)

    # ====================== Task 01 =================================================================

    def create_signal_processing_tab(self, root):
        # Read First Signal Button
        self.read_signal_one_button = tk.Button(root, text="Read Signal 1", command=self.read_signal_one) # button
        self.read_signal_one_button.pack()

        # Read Second Signal Button
        self.read_signal_two_button = tk.Button(root, text="Read Signal 2", command=self.read_signal_two) # button
        self.read_signal_two_button.pack()


        # Add Signal
        self.add_signal_button = tk.Button(root, text="Add Signal", command=self.add_signal) # button
        self.add_signal_button.pack()

        # Subtract Signal
        self.subtract_signal_button = tk.Button(root, text="Subtract Signal", command=self.subtract_signal) # button
        self.subtract_signal_button.pack()

        # Multiply Signal
        self.multiply_signal_label = tk.Label(root, text="Multiply Signal") # label
        self.multiply_signal_label.pack()
        self.multiply_signal_entry = tk.Entry(root) # entry
        self.multiply_signal_entry.pack()
        self.multiply_signal_button = tk.Button(root, text="Multiply", command=self.multiply_signal) # button
        self.multiply_signal_button.pack()

        # Shift Signal
        self.shift_signal_label = tk.Label(root, text="Shift Signal") # label
        self.shift_signal_label.pack()
        self.shift_signal_entry = tk.Entry(root) # entry
        self.shift_signal_entry.pack()
        self.shift_signal_button = tk.Button(root, text="Shift", command=self.shift_signal) # button
        self.shift_signal_button.pack()

        # Reverse Signal
        self.reverse_signal_button = tk.Button(root, text="Reverse Signal", command=self.reverse_signal) # button
        self.reverse_signal_button.pack()

        # Text widget for displaying the signal 1 text
        self.signal_one_display_label = tk.Label(root, text="Result Signal 1");   # label
        self.signal_one_display_label.pack()
        self.signal_one_display_text = tk.Text(root, height=3, width=75)    # text
        self.signal_one_display_text.pack()

        # Text widget for displaying the signal 2 text
        self.signal_two_display_label = tk.Label(root, text="Result Signal 2");   # label
        self.signal_two_display_label.pack()
        self.signal_two_display_text = tk.Text(root, height=3, width=75)    # text
        self.signal_two_display_text.pack()

        # Text widget for displaying the signal result text
        self.signal_result_display_label = tk.Label(root, text="Result Signal");   # label
        self.signal_result_display_label.pack()
        self.signal_result_display_text = tk.Text(root, height=3, width=75)    # text
        self.signal_result_display_text.pack()

        # Display Signal 1 plot
        self.display_one_signal_button = tk.Button(root, text="Display Signal 1", command=self.display_signal_one) # button
        self.display_one_signal_button.pack()

        # Display Signal 2 plot
        self.display_signal_two_button = tk.Button(root, text="Display Signal 2", command=self.display_signal_two) # button
        self.display_signal_two_button.pack()

        # Display Signal result plot
        self.display_signal_result_button = tk.Button(root, text="Display Signal result", command=self.display_signal_result) # button
        self.display_signal_result_button.pack()

        # Canvas for Matplotlib Figure to show signla plot
        self.canvas = None

        # Current used signals
        self.current_indices_one = [] 
        self.current_samples_one = []

        self.current_indices_two = []
        self.current_samples_two = [] 

        self.current_indices_result = []
        self.current_samples_result = []

    def read_signal_one(self, opt=1, opt2=1):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.current_indices_one, self.current_samples_one = ReadSignalFile(file_path, opt)
            self.display_signal_one_text(self.current_indices_one, self.current_samples_one, opt2)
        else:
            messagebox.showerror("ERROR in Reading Signal 1 - Only Text files are allowd")

    def read_signal_two(self, opt=1, opt2=1):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.current_indices_two, self.current_samples_two = ReadSignalFile(file_path, opt)
            self.display_signal_two_text(self.current_indices_two, self.current_samples_two, opt2)
        else:
            messagebox.showerror("ERROR in Reading Signal 2 - Only Text files are allowd")

    def display_signal_one_text(self, indices, samples, opt=1):
        if indices and samples: # There exists a current used signal
            self.signal_one_display_text.delete(1.0, tk.END)
            if opt==1: n1, n2 = "Indices", "Samples"
            else: n1, n2 = "Amplitude", "Phase"
            self.signal_one_display_text.insert(tk.END, f"{n1}: {indices}\n{n2}: {samples}\n")
            # display_signal(indices, samples)
        else:
            messagebox.showerror("ERROR in Displaying Signal 1 text- Passed Signal to display text is not valid")
            
    def display_signal_two_text(self, indices, samples, opt=1):
        if indices and samples: # There exists a current used signal
            self.signal_two_display_text.delete(1.0, tk.END)
            if opt==1: n1, n2 = "Indices", "Samples"
            else: n1, n2 = "Amplitude", "Phase"
            self.signal_two_display_text.insert(tk.END, f"{n1}: {indices}\n{n2}: {samples}\n")
            # display_signal(indices, samples)
        else:
            messagebox.showerror("ERROR in Displaying Signal 2 text- Passed Signal to display text is not valid")

    def display_signal_result_text(self, indices, samples, opt=1):
        if indices and samples: # There exists a current used signal
            self.signal_result_display_text.delete(1.0, tk.END)
            if opt==1: n1, n2 = "Indices", "Samples"
            else: n1, n2 = "Amplitude", "Phase"
            self.signal_result_display_text.insert(tk.END, f"{n1}: {indices}\n{n2}: {samples}\n")
            # display_signal(self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in Displaying Signal result text- Passed Signal to display text is not valid")

    def display_signal_one(self):
        if self.current_indices_one and self.current_samples_one: # There exists a current used signal
            
            # Create a new window for the plot
            plot_window = tk.Toplevel(self.root)
            plot_window.title("Signal Plot")

            figure, axis = plt.subplots()
            axis.plot(self.current_indices_one, self.current_samples_one)
            axis.set_title("Signal Plot")
            axis.set_xlabel("Index")
            axis.set_ylabel("Value")
            axis.grid(True)

            # Create a canvas for the figure
            canvas = FigureCanvasTkAgg(figure, master=plot_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showerror("ERROR in Displaying Signal 1 plot- Current Signal not valid to display plot")

    def display_signal_two(self):
        if self.current_indices_two and self.current_samples_two: # There exists a current used signal
            
            # Create a new window for the plot
            plot_window = tk.Toplevel(self.root)
            plot_window.title("Signal Plot")

            figure, axis = plt.subplots()
            axis.plot(self.current_indices_two, self.current_samples_two)
            axis.set_title("Signal Plot")
            axis.set_xlabel("Index")
            axis.set_ylabel("Value")
            axis.grid(True)

            # Create a canvas for the figure
            canvas = FigureCanvasTkAgg(figure, master=plot_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showerror("ERROR in Displaying Signal 2 plot- Current Signal not valid to display plot")

    def display_signal_result(self):
        if self.current_indices_result and self.current_samples_result: # There exists a current used signal
            
            # Create a new window for the plot
            plot_window = tk.Toplevel(self.root)
            plot_window.title("Signal Plot")

            figure, axis = plt.subplots()
            axis.plot(self.current_indices_result, self.current_samples_result)
            axis.set_title("Signal Plot")
            axis.set_xlabel("Index")
            axis.set_ylabel("Value")
            axis.grid(True)

            # Create a canvas for the figure
            canvas = FigureCanvasTkAgg(figure, master=plot_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showerror("ERROR in Displaying Signal result plot- Current Signal not valid to display plot")

    def add_signal(self):
        if self.current_indices_one and self.current_samples_one and self.current_indices_two and self.current_samples_two:
            self.current_indices_result, self.current_samples_result = add_signal(self.current_indices_one, self.current_samples_one, self.current_indices_two, self.current_samples_two)
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
            AddSignalSamplesAreEqual("Signal1.txt", "Signal2.txt", self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in Adding -- Signals not valid for adding")

    def subtract_signal(self):
        if self.current_indices_one and self.current_samples_one and self.current_indices_two and self.current_samples_two:
            self.current_indices_result, self.current_samples_result = subtract_signal(self.current_indices_one, self.current_samples_one, self.current_indices_two, self.current_samples_two)
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
            SubSignalSamplesAreEqual("Signal1.txt", "Signal2.txt", self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in subtracting -- Signals not valid for subtracting")
    
    def multiply_signal(self):
        if self.current_indices_one and self.current_samples_one:
            factor = float(self.multiply_signal_entry.get())
            self.current_indices_result = self.current_indices_one
            self.current_indices_result, self.current_samples_result = multiply_signal(self.current_indices_one, self.current_samples_one, factor)
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
            MultiplySignalByConst(factor, self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in multiplying --- Current Signal not valid for multiplying")

    def shift_signal(self):
        if self.current_indices_one and self.current_samples_one:
            shift = int(self.shift_signal_entry.get())
            self.current_indices_result, self.current_samples_result = shift_signal(self.current_indices_one, self.current_samples_one, shift)
            self.current_samples_result = self.current_samples_one
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
            ShiftSignalByConst(shift, self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in shifting --- Current Signal not valid for shift")

    def reverse_signal(self):
        if self.current_indices_one and self.current_samples_one:
            self.current_indices_result, self.current_samples_result = reverse_signal(self.current_indices_one, self.current_samples_one)
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
            Folding(self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in reversing --- Current Signal not valid for reverse")


if __name__ == "__main__":
    root = tk.Tk()
    app = DSPApp(root)
    root.mainloop()
    print('exit')
