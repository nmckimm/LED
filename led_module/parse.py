import re
import urllib.request
import urllib.parse
from urllib.parse import urlsplit
import requests 
import sys

def parseFile(input):


    
    uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    cmd = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    filename = "rawinput.txt"
    with open(filename, 'rt') as file:
        instructions = []
        N = int(file.readline())
        for line in file.readlines():
            instructions.extend(re.findall(cmd, line))
        return N, instructions
                
 #   if scheme == 'http':
  #      req = urllib.request.urlopen(uri)
   #     r = requests.get(uri).text
    #    buffer = req.read().decode('utf-8')
     #   with urllib.request.urlopen(uri) as file:
      #      instructions = []
       #     N=int(file.readline())
        #    for line in file.readlines():
         #       instructions.extend(re.findall(cmd, buffer))
        
#    else:
 #       with open(uri, 'rt') as file:
  #          instructions = []
      #      for line in file.readlines():
#
 #               instructions.extend(re.findall(cmd, line))

    
 #   cmd = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")

