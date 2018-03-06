'''
Created on 6 Mar 2018

@author: synq
'''
import re
pat = re.compile(".* (\d+),(\d+)")
m = pat.match("switch 5,5")
x1 = m
print(m)