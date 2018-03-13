import re
import pprint
pprint=pprint.pprint
import numpy as np
import math
from parse import parseFile

class LightTester:
    lights = np.array([])
    prac = np.array([])
    

    def __init__(self, N):

        self.lights = [[False]*N for _ in range(N)]
        self.leds = np.array(self.lights)
        self.prac = np.copy(self.lights)
        
    def apply(self, instructions):
        N, instructions = parseFile(input)
        
        prac = np.copy(self.leds)
        for i in range(len(instructions)):
            print(instructions)
            instruction = instructions[i] ## Tuple instruction changes for each loop (where i = line number in file)
            command, x1, y1, x2, y2 = instruction ## Unpacking tuple and assigning each element
            print(instruction)
            x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
            print(command, x1, y1, x2, y2)
            if (command == 'turn on'):
                prac[x1:x2,y1:y2] = True
                print(prac)
                
            elif (command == 'turn off'):
                prac[x1:x2,y1:y2] = False
                print(prac)
            elif (command == 'switch'):
                prac[x1:x2,y1:y2] = np.logical_not(prac[x1:x2,y1:y2]) #opposite values for t/f
                print(prac)
            else:
                return 0
        print(prac)        
        print('#Occupied: ',np.sum(prac)) #prints number of True values (lights on)
            
        #if cmd.search("switch"):


    
