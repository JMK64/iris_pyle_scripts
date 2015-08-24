''' 
Define contours, evenly spaced by 1/10 of maximum value as given in main script.
'''
#################################################################### 
#################################################################### 
import numpy as np

def levels(lim):
    levs=[]
    for l in lim:
        if l[0]:
          levs.append(np.arange(0,l[0]+l[0]*0.1,l[0]*0.1))
    return levs

def offset(lim):
    offset=[]
    for l in lim:
         if l[1] == '':
          offset.append(1)
         else:
          offset.append(float(l[1]))
    return offset

# Levels
def levels2(list):
    lim=list
    levs=[]
    for i in range(0,len(lim)):
      a=[]
      for j in range(0,len(lim[i])):
        a.append(None)
      levs.append(a)
    for i in range(0,len(levs)):
      for j in range(0,len(lim[i])):
        if lim[i][j]:
          levs[i][j]=np.arange(0,lim[i][j]+10,lim[i][j]/10.0)
    return levs

def levels_diff(list):
    lim=list
    levs=[]
    for i in range(0,len(lim)):
      a=[]
      for j in range(0,len(lim[i])):
        a.append(None)
      levs.append(a)
    for i in range(0,len(levs)):
      for j in range(0,len(lim[i])):
        if lim[i][j]:
          levs[i][j]=np.arange(-lim[i][j],lim[i][j],lim[i][j]/10.0)
    return levs

def offset2(list):
    offsettext=list
    offset=[]
    for i in range(0,len(offsettext)):
      a=[]
      for j in range(0,len(offsettext[i])):
        a.append(None)
      offset.append(a)
    for i in range(0,len(offset)):
      for j in range(0,len(offsettext[i])):
        offset[i][j]=float(offsettext[i][j])
        if offsettext[i][j]=='1':
          offsettext[i][j]=''
    return offset,offsettext

