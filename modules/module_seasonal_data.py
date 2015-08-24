''' Calculate seasonal data
'''
#################################################################### 
#################################################################### 
import netCDF4 as ncdf
import numpy as np
import jobs

def season(ncbase,jobid, var):
    data = ncbase.variables[var][jobs.spinup(jobid)[0]:jobs.spinup(jobid)[1]]
    for y in range(0,len(data)/12-1):
       mam = np.mean(data[2+y*12:5+y*12],axis=0)
       jja = np.mean(data[5+y*12:8+y*12],axis=0)
       son = np.mean(data[8+y*12:12+y*12],axis=0)
       d   = np.mean(data[12+y*12:13+y*12],axis=0)
       jf  = np.mean(data[0+y*12:2+y*12],axis=0)
       djf = np.mean([d,jf],axis=0)
    return djf,mam,jja,son

def month(ncbase, var):
    var=word
    ncbase=netCDF
    data = ncbase.variables[var][jobs.spinup(jobid)[0]:jobs.spinup(jobid)[1]]
    for y in range(0,len(data)/12-1):
       mam = np.mean(data[2+y*12:5+y*12],axis=0)
       jja = np.mean(data[5+y*12:8+y*12],axis=0)
       son = np.mean(data[8+y*12:12+y*12],axis=0)
       d   = np.mean(data[12+y*12:13+y*12],axis=0)
       jf  = np.mean(data[0+y*12:2+y*12],axis=0)
       djf = np.mean([d,jf],axis=0)
    return djf,mam,jja,son

