''' 
Return Dimensions of netCDF file:
Latitude, Longitude, Height, TimeStamp
'''

import netCDF4 as ncdf
import numpy as np
import jobs

def dimensions(ncbase,jobid):
    lat = np.array(ncbase.variables['latitude'],dtype=np.float64)[:]
    lon = np.array(ncbase.variables['longitude'],dtype=np.float64)[:]
    hgt = np.array(ncbase.variables['level_height'],dtype=np.float64)[:]
    mon = np.array(ncbase.variables['time'],dtype=np.float64)\
           [jobs.spinup(jobid)[0]:jobs.spinup(jobid)[1]]
    return lat,lon,hgt,mon

