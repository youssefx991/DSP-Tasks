import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Task01.Task01 import *
from Task02.task02 import *
from Task01.Task1_testcases_and_testing_functions.DSP_Task2_TEST_functions import *
from Task03.Test_1.QuanTest1 import *
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

        # Assign functions for creating tabs
        self.create_signal_processing_tab(self.signal_processing_frame)
        self.create_signal_generation_tab(self.signal_generation_frame)
        self.create_signal_quantization_tab(self.signal_quantize_frame)


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
        self.quantized_signal_display_txt = tk.Text(root, height=5, width=50)
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
            quantized_samples, errors, encoded_values = self.perform_quantization(samples, num_levels)
            
            # Display results
            self.quantized_signal_display_txt.delete(1.0, tk.END)
            for sample, error, encoded_value in zip(quantized_samples, errors, encoded_values):
                self.quantized_signal_display_txt.insert(tk.END, f"{encoded_value} {sample:.2f} error = {error}\n")

            QuantizationTest1("Quan1_Out.txt", encoded_values, quantized_samples)
            return quantized_samples, errors, encoded_values
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
        num_bits = int(np.log2(num_levels))
        for sample in signal:
            # Determine the quantization level
            level = int((sample - min_val) / level_width)
            level = max(0, min(level, num_levels - 1))  # Clamp level to valid range between [0, max_level]
            
            # Calculate quantized value and error
            quantized_value = min_val + (level + 0.5) * level_width
            error = sample - quantized_value
            
            # Append encoded signal (binary representation)


            encoded_value = format(level, '0{}b'.format(num_bits))
            encoded_values.append(encoded_value)

            quantized_signal.append(quantized_value)
            quantization_errors.append(error)


        return quantized_signal, quantization_errors, encoded_values

    def plot_quantized_signal(self):
        quantized_samples, errors, encoded_values = self.quantize_signal()
        signal = self.current_samples_one
        time = np.arange(len(signal))

        # Create a new window for the plot
        plot_window = tk.Toplevel(self.root)
        plot_window.title("Signal Plot")

        # Create a new figure for the plot
        figure, axis = plt.subplots(3, 1, figsize=(10, 6))  # 1 column for single plot, 2 columns for dual plots
        axis[0].grid(True)
        axis[1].grid(True)
        axis[2].grid(True)
        
        # Original Signal
        axis[0].plot(time, signal, color='black')
        axis[0].set_title("Original Signal")
        axis[0].set_xlabel("Time (s)")
        axis[0].set_ylabel("Amplitude")
        
        # Quantized Signal
        axis[1].plot(time, quantized_samples, color='green')
        axis[1].set_title("Quantized Signal")
        axis[1].set_xlabel("Time (s)")
        axis[1].set_ylabel("Amplitude")

        # Error
        axis[2].plot(time, errors, color='red')
        axis[2].set_title("Quantization Error")
        axis[2].set_xlabel("Time (s)")
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
        self.signal_one_display_text = tk.Text(root, height=1, width=50)    # text
        self.signal_one_display_text.pack()

        # Text widget for displaying the signal 2 text
        self.signal_two_display_label = tk.Label(root, text="Result Signal 2");   # label
        self.signal_two_display_label.pack()
        self.signal_two_display_text = tk.Text(root, height=1, width=50)    # text
        self.signal_two_display_text.pack()

        # Text widget for displaying the signal result text
        self.signal_result_display_label = tk.Label(root, text="Result Signal");   # label
        self.signal_result_display_label.pack()
        self.signal_result_display_text = tk.Text(root, height=1, width=50)    # text
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

    def read_signal_one(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.current_indices_one, self.current_samples_one = ReadSignalFile(file_path)
            self.display_signal_one_text(self.current_indices_one, self.current_samples_one)
        else:
            messagebox.showerror("ERROR in Reading Signal 1 - Only Text files are allowd")

    def read_signal_two(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.current_indices_two, self.current_samples_two = ReadSignalFile(file_path)
            self.display_signal_two_text(self.current_indices_two, self.current_samples_two)
        else:
            messagebox.showerror("ERROR in Reading Signal 2 - Only Text files are allowd")

    def display_signal_one_text(self, indices, samples):
        if indices and samples: # There exists a current used signal
            self.signal_one_display_text.delete(1.0, tk.END)
            self.signal_one_display_text.insert(tk.END, f"Indices: {indices}\nSamples: {samples}\n")
            # display_signal(indices, samples)
        else:
            messagebox.showerror("ERROR in Displaying Signal 1 text- Passed Signal to display text is not valid")
            
    def display_signal_two_text(self, indices, samples):
        if indices and samples: # There exists a current used signal
            self.signal_two_display_text.delete(1.0, tk.END)
            self.signal_two_display_text.insert(tk.END, f"Indices: {indices}\nSamples: {samples}\n")
            # display_signal(indices, samples)
        else:
            messagebox.showerror("ERROR in Displaying Signal 2 text- Passed Signal to display text is not valid")

    def display_signal_result_text(self, indices, samples):
        if indices and samples: # There exists a current used signal
            self.signal_result_display_text.delete(1.0, tk.END)
            self.signal_result_display_text.insert(tk.END, f"Indices: {self.current_indices_result}\nSamples: {self.current_samples_result}\n")
            # display_signal(self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in Displaying Signal result text- Passed Signal to display text is not valid")

    def display_signal_one(self):
        if self.current_indices_one and self.current_samples_one: # There exists a current used signal
            
            self.signal_one_display_text.delete(1.0, tk.END) # clear text from previous signal data
            self.signal_one_display_text.insert(tk.END, self.current_indices_one)   # fill it with cirrent signal data
            self.signal_one_display_text.insert(tk.END, self.current_samples_one)   # fill it with cirrent signal data
            # display_signal(self.current_indices_one, self.current_samples_one)

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
            
            self.signal_two_display_text.delete(1.0, tk.END) # clear text from previous signal data
            self.signal_two_display_text.insert(tk.END, self.current_indices_two)   # fill it with cirrent signal data
            self.signal_two_display_text.insert(tk.END, self.current_samples_two)   # fill it with cirrent signal data
            # display_signal(self.current_indices_two, self.current_samples_two)

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
        if self.current_indices_two and self.current_samples_two: # There exists a current used signal
            
            self.signal_result_display_text.delete(1.0, tk.END) # clear text from previous signal data
            self.signal_result_display_text.insert(tk.END, self.current_indices_result)   # fill it with cirrent signal data
            self.signal_result_display_text.insert(tk.END, self.current_samples_result)   # fill it with cirrent signal data
            # display_signal(self.current_indices_result, self.current_samples_result)

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
