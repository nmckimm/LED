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
        for i in range(len(instructions)+1):
            instruction = instructions[i-1] ## Tuple instruction changes for each loop (where i = line number in file)
            command, y1, x1, y2, x2 = instruction ## Unpacking tuple and assigning each element
            x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
            y1, x1 = y1-1, x1-1
            # if len x1 < N/10 or N/100 oe N=1000
            #x1, x2, y1, y2 = x1-1, x2-1, y1-1, y2-1
            if (command == 'turn on'):
                print(instruction)                
                prac[y1:y2,x1:x2] = True
                print(np.sum(prac))
            elif (command == 'turn off'):
                print(instruction)
                prac[y1:y2,x1:x2] = False
                print(np.sum(prac))
            elif (command == 'switch'):
                print(instruction)
                if (y2 < y1) or (x2 < x1):
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
                    prac[y1:y2,x1:x2] = np.logical_not(prac[y1:y2,x1:x2]) 
                else:
                    prac[y1:y2,x1:x2] = np.logical_not(prac[y1:y2,x1:x2]) #opposite values for t/f
                print(np.sum(prac))
            else:
                continue
            print(prac)
        print(prac)
        print('#Occupied: ',np.sum(prac)) #prints number of True values (lights on)
        
        
        #4,4 6,6 interpreted as 4,6 4,6
        
        #if cmd.search("switch"):
        #is it parsing the file correctly? ignore line with incorrect spelling of word


    
