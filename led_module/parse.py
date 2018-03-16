import re
import urllib.request
import urllib.parse
from urllib.request import urlopen
from urllib.parse import urlsplit
import requests 
import sys

def parseFile(input):

#retrieve(url[, filename[, reporthook[, data]]])

    
    #uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    cmd = re.compile(".*(turn on|turn off|switch)\s*(\d+)\s*,\s*(\d+)\s*through\s*(\d+)\s*,\s*(\d+).*")
    uri = sys.argv[2]
    print(uri)
    #uri = ''.join(uri)
    print(uri)
    filename = ''
    if uri.startswith('http'):
        print(uri)
        req = urllib.request.urlopen(uri)
        req1 = req.read()
        req1
        
        response = requests.get(uri)
        print(response.content)
        data = response.content.decode('utf-8')
        N = int(data.split('\n', 1)[0])
        data = data.split('\n')
        print(data)
        instructions = []
        for line in data:
            instructions.extend(re.findall(cmd, line))
        
        return N, instructions
        

        
    elif uri.startswith('r'):
        filename = "rawinput.txt"
        with open(filename, 'rt') as file:
            instructions = []
            N = int(file.readline())
            for line in file.readlines():
                instructions.extend(re.findall(cmd, line))
            return N, instructions
        
    else:
        return uri
                
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

