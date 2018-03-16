'''
Created on 6 Mar 2018

@author: synq
'''
from parse import parseFile
from urllib.parse import urlsplit
import re
pat = re.compile(".* (\d+),(\d+)")
m = pat.match("switch 5,5")
x1 = m
print(m)


url='http://google.com/'
scheme = urlsplit(url).scheme
print(scheme)

N, instructions = parseFile(input)
#pattern = re.findall("(\d+),(\d+)", instructions)
cmd = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
filename='rawinput.txt'
with open(filename, 'rt') as file:
    instructions = []
    N=int(file.readline())
    for line in file.readlines():
        instructions.extend(re.findall(cmd, line))
    print('a',numArray)
#int_list = [int(s) for s in re.findall("(\d+),(\d+)", instructions)]
#tuple unpacking x = (1,2) -> a, b = x-> a >>1 b>>2
#each array element is a tuple
'''
0 is command
1 is x1
2 is y1
3 is x1
4 is y1
'''
