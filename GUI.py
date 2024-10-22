import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Task01.Task01 import *

class DSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DSP App")

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
        else:
            messagebox.showerror("ERROR in Adding -- Signals not valid for adding")

    def subtract_signal(self):
        if self.current_indices_one and self.current_samples_one and self.current_indices_two and self.current_samples_two:
            self.current_indices_result, self.current_samples_result = subtract_signal(self.current_indices_one, self.current_samples_one, self.current_indices_two, self.current_samples_two)
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in subtracting -- Signals not valid for subtracting")
    
    def multiply_signal(self):
        if self.current_indices_one and self.current_samples_one:
            factor = float(self.multiply_signal_entry.get())
            self.current_indices_result = self.current_indices_one
            self.current_samples_result = multiply_signal(self.current_samples_one, factor)
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in multiplying --- Current Signal not valid for multiplying")

    def shift_signal(self):
        if self.current_indices_one and self.current_samples_one:
            shift = int(self.shift_signal_entry.get())
            self.current_indices_result = shift_signal(self.current_indices_one, shift)
            self.current_samples_result = self.current_samples_one
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in shifting --- Current Signal not valid for shift")

    def reverse_signal(self):
        if self.current_indices_one and self.current_samples_one:
            self.current_indices_result, self.current_samples_result = reverse_signal(self.current_indices_one, self.current_samples_one)
            self.display_signal_result_text(self.current_indices_result, self.current_samples_result)
        else:
            messagebox.showerror("ERROR in reversing --- Current Signal not valid for reverse")


if __name__ == "__main__":
    root = tk.Tk()
    app = DSPApp(root)
    root.mainloop()
