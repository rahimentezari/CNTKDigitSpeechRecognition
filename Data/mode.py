#!/usr/bin/env python
#https://github.com/jameslyons/python_speech_features


from collections import Counter

import sys
import re
import os

f=open('C:\src\cntk\Examples\Other\Sourena\Output\SimpleOutput.PosteriorProb',"r")
lines=f.readlines()
result=[]
for x in lines:
    result.append(x.split(' ')[0][:1])
f.close()

print(type(result))
print(result)
#data = Counter(result)
#print(data.most_common())   # Returns all unique items and their counts
#print(data.most_common(2))  # Returns the highest occurring item



sys.stdout = open("output.txt", "w")
print(max(set(result), key=result.count))