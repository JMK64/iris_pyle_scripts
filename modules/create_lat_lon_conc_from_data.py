''' 
Return data as a function of lat and lon
'''

import netCDF4 as ncdf
import numpy as np

import jobs
import units
import variables_attributes
import convert_unit

import calc_area
import convert_time
import calc_budget

def mapdata(ncbase,jobid,z,var):
# ncbase = time,model_level_number,latitude,longitude
    lat = np.array(ncbase.variables['latitude'],dtype=np.float64)[:]
    lon = np.array(ncbase.variables['longitude'],dtype=np.float64)[:]
    hgt = np.array(ncbase.variables['level_height'],dtype=np.float64)[:]
    mon = np.array(ncbase.variables['time'],dtype=np.float64)\
                  [jobs.spinup(jobid)[0]:jobs.spinup(jobid)[1]]
    high = np.where(hgt>=z[1]*1E3)[0][0]+1
    low = np.where(hgt>=z[0]*1E3)[0][0]
    # Airmass
    file1 = '/scratch/ih280/um/'+jobid+'/pm_'+jobid+'_oh.nc'
    ncbase1 = ncdf.Dataset(file1,'r')
    airmass = np.array(ncbase1.variables['field643'], dtype=np.float64)[:]
    # Convert unit
    unit1=units.diagnostic(var)
    conversion = convert_unit.convert2(unit1,var,airmass)
    # DATA
    data = ncbase.variables[var][jobs.spinup(jobid)[0]:jobs.spinup(jobid)[1]]
    if np.shape(conversion)>(1,):
        conversion = np.resize(conversion,(len(data), 60, 73, 96))
    data = data[:]*conversion
    # Map
    years=[]
    for y in range(0,len(data)/12):
        years.append(np.mean(np.mean(data[y*12:(y+1)*12,low:high,:,:], axis=1, dtype=np.float64), axis=0, dtype=np.float64))
    data1 = np.mean(years, axis=0, dtype=np.float64)
    sd = np.std(years, axis=0, dtype=np.float64)
    sdbelow = data1[:]-sd[:]
    sdabove = data1[:]+sd[:]
    return data1,sdbelow,sdabove

