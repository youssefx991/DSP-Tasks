

def DFT(gui):
    gui.dft_real, gui.dft_imaginary = [1,2,3], [4,5,6]
    print(f"in DFT {gui.dft_real}")
    print(f"in DFT {gui.dft_imaginary}")

def IDFT(gui):
    print(f"in IDFT {gui.dft_real}")
    print(f"in IDFT {gui.dft_imaginary}")

def plot_freq_amplitude(gui):
    pass