#!/usr/bin/env python
#https://github.com/jameslyons/python_speech_features
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import sys
import re
import os
import numpy
import scipy
import numpy as np
#os.remove("test.txt")
#os.remove("all.txt")
#os.remove("output.txt")

(rate,sig) = wav.read("44.wav")
mfcc_feat = mfcc(sig,rate,winlen=0.025,winstep=0.01,numcep=13,nfilt=26,nfft=512,lowfreq=0,highfreq=8000,preemph=0.97,appendEnergy=False)
num_rows, num_cols=mfcc_feat.shape

lis=[]
#print(mfcc_feat[(1,1)])
for i in range(0,num_rows):
    for j in range(0,num_cols):
        if mfcc_feat[(i,j)]==0.0:
            lis=lis+[i]
			
uniq=np.unique(lis)
rowsuniq=uniq.size

mfcc_feat2=numpy.delete(mfcc_feat,uniq,0)

print(mfcc_feat2.shape)
num_rows2, num_cols2=mfcc_feat2.shape
lines = []
with open('all.txt', 'w') as f:
    for i in range(0,num_rows2-40 ):
        sel=mfcc_feat2[i:i+41,:]
        a=sel.reshape((1,533))
        q=""
        for s in sel:
            p= " ".join(map(str,s))
            q=q+" "+p
    #sys.stdout = open("all.txt", "a")
        
    #print(type(q))
        lines.append( "4"+q )
    print(lines)
    f.write('\n'.join(lines))

#with open ('all.txt') as f,open('new.txt','w')as new:
#    for line in f:
#        if not  "0.0 " in line :
#            new.write(line)
	
#bad_words=['0.0 0.0']
#with open ('all.txt') as old,open ('new.txt','w') as new:
#    for line in old:
#        if not any(bad|_word in line for bad_word in bad_words):
#            new.write(line)
#print(lis)
#print(uniq.shape)
#print(rowsuniq)
#print(uniq)
print(mfcc_feat)
print(mfcc_feat2.shape)
#print(mfcc_feat.shape)
#print(uniq[10])
#print(type(mfcc_feat))
#print(rowsuni)
#print(uniq[10])
#print(index)