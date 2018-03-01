import re


class LightTester:
    lights = None

    def __init__(self, N):
        size = 1000
        self.lights = [[False] * size for _ in size]

    
    def apply(cmd):
        cmd = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s *,\s * ([+-]?\d+)\s * through\s * ([+-]?\d+)\s *,\s * ([+-]?\d+). * ")
        counter = 0
        if cmd.search("switch on"):
            counter += 1
        elif cmd.search("turn off"):
            counter -= 1
        else:
            return

    def count(self):
        count1 = apply.counter
        return count1
