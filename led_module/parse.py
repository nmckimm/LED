def parseFile(input):


    N, instructions = None, []
    filename = 'rawinput.txt'
    with open(filename) as f:
        N = int(f.readline())
        for line in f.readlines():
            instructions.append(line)
            values = line.strip().split()
        

    # haven't written the code yet...
    return N, instructions
    