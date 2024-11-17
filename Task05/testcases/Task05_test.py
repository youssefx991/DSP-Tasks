def compare_signals(file_name,Your_Indices, Your_Samples, window_size=0):
    if window_size == 3:
        file_name="MovingAvg_out1.txt"
    elif window_size == 5:
        file_name="MovingAvg_out2.txt"
    expectedIndices=[]
    expectedSamples=[]
    with open(file_name, 'r') as f:
        print("Reading signal file")
        expectedIndices=[]
    expectedSamples=[]
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
                expectedIndices.append(V1)
                expectedSamples.append(V2)
                line = f.readline()
            else:
                break
        print("Finished reading signal file")
        print("Expected Indices: ", expectedIndices)
        print("Expected Samples: ", expectedSamples)
    if len(Your_Indices)!=len(expectedIndices):
        print("Test case failed, your signal indices have different length from the expected one")
        print("Expected Indices: ", expectedIndices)
        print("Your Indices: ", Your_Indices)
        return
    if len(Your_Samples)!=len(expectedSamples):
        print("Test case failed, your signal samples have different length from the expected one")
        print("Expected: ", expectedSamples)
        print("Your: ", Your_Samples)
        return
    for i in range(len(Your_Indices)):
        if(Your_Indices[i]!=expectedIndices[i]):
            print("Test case failed, your signal have different indicies from the expected one") 
            return
        
    for i in range(len(expectedSamples)):
        if abs(Your_Samples[i] - expectedSamples[i]) < 0.01:
            continue
        else:
            print("Test case failed, your Samples have different values from the expected one") 
            return
    print("Test case passed successfully")