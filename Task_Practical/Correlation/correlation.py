from Task_Practical.Correlation.Correlation_Task_Files.Point1_Correlation.CompareSignal import *

def correlation(gui):
    samples_one = gui.current_samples_one
    samples_two = gui.current_samples_two
    n = len(samples_one)
    result_samples = []
    
    for shift in range(n):
        current_sum = 0
        for i in range(n):
            current_sum += samples_one[i] * samples_two[ (i+shift) % n ]
        result_samples.append(current_sum/n)
    
    print("result_samples = ", result_samples)
    norm_factor = 1/n * (sum(x**2 for x in samples_one) * sum(x**2 for x in samples_two))**0.5
    print("norm_fractor = ", norm_factor)
    result_samples = [x / norm_factor for x in result_samples]
    
    gui.current_indices_result, gui.current_samples_result = gui.current_indices_one, result_samples
    gui.display_signal_result_text(gui.current_indices_result, gui.current_samples_result, 1)
    Compare_Signals("CorrOutput.txt", gui.current_indices_result, gui.current_samples_result)

def time_delay(gui):
    pass

def signal_class(gui):
    pass
