import re
import pprint
pprint=pprint.pprint
import numpy as np
import math
from parse import parseFile

class LightTester():
    lights = None
    

    def __init__(self, N):

        self.lights = [[False]*N for _ in range(N)]
        self.leds = np.array(self.lights)
        
    def apply(self, cmd):
        cmd = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        counter = 0
        N, instructions = parseFile(input)
        
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
        #if cmd.search("switch"):


    def count(self):
        return 0
