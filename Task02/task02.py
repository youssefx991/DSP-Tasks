import numpy as np

def generate_signal(self):
    # amplitude * cos(2*pi*F*t + phase shift)
    amp = float(self.amplitude_txb.get())
    phase_shift = float(self.phase_shift_txb.get())
    freq = float(self.frequency_txb.get())
    fs = float(self.fs_txb.get())

    t = np.linspace(0, 1, 1000)

    samples_per_second = int(fs) # number of samples per second
    n = np.arange(samples_per_second) # creates an array from 0 -> samples_per_second - 1 
    t_disc = n / fs # normailze the values of x-axis to be from 0 to 1 like t
    
    if fs < 2*freq:
        messagebox.showerror(message="fs < f, this will cause aliasing")

    if self.display_opt.get() == "Sin":
        print("Sin")
        signal = amp * np.sin(2*np.pi*freq*t + phase_shift)
        signal_disc = amp * np.sin(2 * np.pi * freq * (n/fs) + phase_shift)
    elif self.display_opt.get() == "Cos":
        print("Cos")
        signal = amp * np.cos(2*np.pi*freq*t + phase_shift)
        signal_disc = amp * np.cos(2 * np.pi * freq * (n/fs) + phase_shift)

    print('signal:', signal)
    print('time:', t)
    return signal, t, signal_disc, t_disc