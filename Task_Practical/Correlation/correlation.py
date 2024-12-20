from Task_Practical.Correlation.Correlation_Task_Files.Point1_Correlation.CompareSignal import *
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from Task01.Task1_testcases_and_testing_functions.DSP_Task2_TEST_functions import *

def correlation(gui):
    samples_one = gui.current_samples_one
    samples_two = gui.current_samples_two
    
    result_samples = perform_corr(samples_one, samples_two)
    
    gui.current_indices_result, gui.current_samples_result = gui.current_indices_one, result_samples
    
    gui.corr_signal_result_display_text.delete(1.0, tk.END)
    gui.corr_signal_result_display_text.insert(tk.END, f"Indices: {gui.current_indices_result}\nSamples: {gui.current_samples_result}\n")
    
    
    time_delay(gui)
    
    up_signals = ["up1.txt", "up2.txt", "up3.txt", "up4.txt", "up5.txt"]
    down_signals = ["down1.txt", "down2.txt", "down3.txt", "down4.txt", "down5.txt"]
    
    result_class = get_signal_class(gui.current_indices_result, gui.current_samples_result, up_signals, down_signals)
    
    gui.signal_signal_class.delete('1.0', 'end')  # Clear the previous content
    gui.signal_signal_class.insert('1.0', result_class)
    
    Compare_Signals("CorrOutput.txt", gui.current_indices_result, gui.current_samples_result)

def perform_corr(samples_one, samples_two):
    n = len(samples_one)
    result_samples = []
    
    for shift in range(n):
        current_sum = 0
        for i in range(n):
            current_sum += samples_one[i] * samples_two[ (i+shift) % n ]
        result_samples.append(current_sum/n)
    
    norm_factor = 1/n * (sum(x**2 for x in samples_one) * sum(x**2 for x in samples_two))**0.5
    result_samples = [x / norm_factor for x in result_samples]
    
    return result_samples
    

def time_delay(gui):
    indices = gui.current_indices_result
    samples = gui.current_samples_result
    fs = int(gui.corr_fs_txb.get())
    gui.time_delay = get_time_delay(samples, fs)
    gui.signal_time_delay.delete('1.0', 'end')  # Clear the previous content
    gui.signal_time_delay.insert('1.0', f"Time Delay: {gui.time_delay} seconds")
    
def get_time_delay(samples, fs):
    ts = 1/fs
    max_corr_val = max(samples, key=abs)
    max_corr_idx = samples.index(max_corr_val)
    time_delay = max_corr_idx * ts
    return time_delay
    
def signal_class(gui):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        gui.current_indices_one, gui.current_samples_one = read_lines(file_path)
        gui.display_signal_one_text(gui.current_indices_one, gui.current_samples_one, 1)
    else:
        messagebox.showerror("ERROR in Reading Signal 1 - Only Text files are allowd")
        
    indices, samples = gui.current_indices_one, gui.current_samples_one
    
    up_signals = ["up1.txt", "up2.txt", "up3.txt", "up4.txt", "up5.txt"]
    down_signals = ["down1.txt", "down2.txt", "down3.txt", "down4.txt", "down5.txt"]
    
    result_class = get_signal_class(indices, samples, up_signals, down_signals)
    
    gui.signal_signal_class.delete('1.0', 'end')  # Clear the previous content
    gui.signal_signal_class.insert('1.0', result_class)
    
def get_signal_class(indices, samples, up_signals, down_signals):
    up_maxs = []
    down_maxs = []
    up_avg = 0
    down_avg = 0
    for file_name in up_signals:
        up_indices, up_samples = read_lines(file_name)
        result_samples = perform_corr(samples, up_samples)
        up_maxs.append(max(result_samples, key=abs))
    up_avg = sum(up_maxs) / len(up_maxs)
    
    for file_name in down_signals:
        down_indices, down_samples = read_lines(file_name)
        result_samples = perform_corr(samples, down_samples)
        down_maxs.append(max(result_samples, key=abs))
    down_avg = sum(down_maxs) / len(down_maxs)
    
    if down_avg >= up_avg:
        return "Class 1 (A) - Down"
    else:
        return "Class 2 (B) - Up"
        
def read_lines(file_name):
    indices = []
    samples = []
    index = 0
    with open(file_name, 'r') as f:
        samples = [float(line.strip()) for line in f.readlines()]
    indices = list(range(len(samples)))
    return indices,samples

def read_corr_signal_one(gui):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        gui.current_indices_one, gui.current_samples_one = ReadSignalFile(file_path, 1)
        
        gui.corr_signal_one_display_text.delete(1.0, tk.END)
        gui.corr_signal_one_display_text.insert(tk.END, f"Indices: {gui.current_indices_one}\nSamples: {gui.current_samples_one}\n")
    else:
        messagebox.showerror("ERROR in Reading Signal 1 - Only Text files are allowd")

def read_corr_signal_two(gui):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        gui.current_indices_two, gui.current_samples_two = ReadSignalFile(file_path, 1)
        
        gui.corr_signal_two_display_text.delete(1.0, tk.END)
        gui.corr_signal_two_display_text.insert(tk.END, f"Indices: {gui.current_indices_two}\nSamples: {gui.current_samples_two}\n")
    else:
        messagebox.showerror("ERROR in Reading Signal 1 - Only Text files are allowd")
    

    