import re
import requests 
import sys

def parseFile(input):


    
    cmd = re.compile(".*(turn on|turn off|switch)\s*(\d+)\s*,\s*(\d+)\s*through\s*(\d+)\s*,\s*(\d+).*")
    uri = sys.argv[2]
    filename = ''
    if uri.startswith('http'):

        response = requests.get(uri)
        data = response.content.decode('utf-8')
        N = int(data.split('\n', 1)[0])
        data = data.split('\n')[1:]
        print(data)
        instructions = []
        for line in data:
            instructions.extend(re.findall(cmd, line))
        return N, instructions
        
    else:
        filename = uri
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

