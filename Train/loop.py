#!/usr/bin/env python
#https://github.com/jameslyons/python_speech_features
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import sys
import re
import numpy as np
import numpy
i=1
with open('testwav.txt') as fp:
    for line in fp:
        #print line
        line2=line[:-1]
        label=line2[55]
        (rate,sig) = wav.read(line2)
        #print rate
        mfcc_feat = mfcc(sig,rate,winlen=0.025,winstep=0.01,numcep=13,nfilt=26,nfft=512,lowfreq=0,highfreq=8000,preemph=0.97,appendEnergy=False)
        num_rows, num_cols=mfcc_feat.shape
        lis=[]
        for i in range(0,num_rows):
            for j in range(0,num_cols):
                if mfcc_feat[(i,j)]==0.0:
                    lis=lis+[i]
			
        uniq=np.unique(lis)
        rowsuniq=uniq.size

        mfcc_feat2=numpy.delete(mfcc_feat,uniq,0)

        #print(mfcc_feat2.shape)
        num_rows2, num_cols2=mfcc_feat2.shape
        lines = []
        with open('all.txt', 'a') as f:
            for i in range(0,num_rows2-40 ):
                sel=mfcc_feat2[i:i+41,:]
                a=sel.reshape((1,533))
                q=""
                for s in sel:
                    p= " ".join(map(str,s))
                    q=q+" "+p
    #sys.stdout = open("all.txt", "a")
        
    #print(type(q))
                lines.append( label+q )
            print(lines)
            f.write('\n'.join(lines))
