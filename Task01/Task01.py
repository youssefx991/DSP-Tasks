
def ReadSignalFile(file_name):
    expected_indices=[]
    expected_samples=[]
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
                V1=int(L[0])
                V2=float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    return expected_indices,expected_samples


def save_signal_to_file(file_name, indices, samples):
    with open(file_name, 'w') as f:
        f.write("0\n")
        f.write("0\n")
        f.write(str(len(indices)))
        f.write("\n")

        for i, j in zip(indices, samples):
            f.write(f"{i} {j}\n")


def add_signal(indices_one: list[float], samples_one : list[float], indices_two : list[float], samples_two : list[float]):
    i = j = 0
    result_indices = []
    result_samples = []

    # loop on two indices together
    while i < len(indices_one) and j < len(indices_two):
        if indices_one[i] == indices_two[j]:
            result_indices.append(indices_one[i])
            result_samples.append(samples_one[i] + samples_two[j])
            i += 1
            j += 1
        elif indices_one[i] < indices_two[j]:
            result_indices.append(indices_one[i])
            result_samples.append(samples_one[i])
            i += 1
        elif indices_one[i] > indices_two[j]:
            result_indices.append(indices_two[j])
            result_samples.append(samples_two[j])
            j += 1

    # loop on remaining indices
    while i < len(indices_one):
        result_indices.append(indices_one[i])
        result_samples.append(samples_one[i])
        i += 1

    while j < len(indices_two):
        result_indices.append(indices_two[j])
        result_samples.append(samples_two[j])
        j += 1


    return result_indices, result_samples


def multiply_signal(indices: list[float], samples: list[float], factor : float):
    result_samples = []

    for index, sample in zip(indices, samples):
        result_samples.append(sample * factor)
    return indices, result_samples


def subtract_signal(indices_one: list[float], samples_one: list[float], indices_two : list[float], samples_two : list[float]):
    indices_two, negative_samples_two = multiply_signal(indices_two, samples_two, -1)
    result_indices, result_samples = add_signal(indices_one, samples_one, indices_two, negative_samples_two)
    return result_indices, result_samples


def shift_signal(indices: list[float], samples: list[float], shift : int):
    result_indices = []

    if shift < 0: # shift right -- delay
        for index in indices:
            result_indices.append(index + 3)
    elif shift > 0: # shift left -- advance
        for index in indices:
            result_indices.append(index - 3)
    else: # shift = 0
        result_indices = indices
    return result_indices, samples


def reverse_signal(indices : list[float], samples : list[float]):
    reversed_samples = samples[::-1]
    result_indices = []

    for index in indices:
        result_indices.append(-1 * index)
    result_indices.sort()

    return result_indices, reversed_samples
    

