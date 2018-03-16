Parsing:
#    filename = 'rawinput.txt'
#    with open(filename, 'r' ) as f:
 #       N = int(f.readline())
  #      for line in f.readlines():
   #         instructions.append(line)
    #        values = line.strip().split()
    
        lel = np.copy(self.leds)
        for i in range(len(instructions)):
            print(values)
            onOff = [int(s) for s in instructions[i] if s.isdigit()]
            print(onOff)
            x1, y1, x2, y2 = int(onOff[0]), int(onOff[1]), int(onOff[2]), int(onOff[3])
            print(x1, x2, y1, y2)

            lel[x1:x2,y1:y2] = True
            pprint(lel)
            print(np.sum(lel))
            
        return np.sum(lel)
    
    
    filename='rawinput.txt'
    with open(filename, 'rt') as file:
        instructions = []
        N=int(file.readline())
        for line in file.readlines():
            instructions.extend(re.findall(cmd, line))
    # haven't written the code yet...
    return N, instructions