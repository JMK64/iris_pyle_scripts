''' 
Return vertical profile
Meaned, SD, function of height.
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

def vertdata(ncbase,jobid,z,var,latbounds):
    lat = np.array(ncbase.variables['latitude'],dtype=np.float64)[:]
    lon = np.array(ncbase.variables['longitude'],dtype=np.float64)[:]
    hgt = np.array(ncbase.variables['level_height'],dtype=np.float64)[:]
    mon1 = np.array(ncbase.variables['time'],dtype=np.float64)
    mon1 = mon1[jobs.spinup(jobid)[0]:jobs.spinup(jobid)[1]]
    mon = mon1[:]
    high = np.where(hgt>=z[1]*1E3)[0][0]+1
    low = np.where(hgt>=z[0]*1E3)[0][0]
    south = np.where(lat==latbounds[0])[0][0]
    north = np.where(lat==latbounds[1])[0][0]+1
#    attributes=variables_attributes.attributes(var)
    # Convert unit
    unit1=units.diagnostic(var)
    if unit1=='':
        unit1 = data.unit
    conversion = convert_unit.convert(unit1,var)
    # DATA
    data = ncbase.variables[var][jobs.spinup(jobid)[0]:jobs.spinup(jobid)[1]]    
    data = data[:]*conversion
    # Vertical profile
    years=[]
    for y in range(0,len(data)/12):
        years.append(np.mean(np.mean(np.mean(data[y*12:(y+1)*12,low:high,south:north,:], axis=3, dtype=np.float64), axis=2, dtype=np.float64), axis=0, dtype=np.float64))
    data1 = np.mean(years, axis=0, dtype=np.float64)
    sd = np.std(years, axis=0, dtype=np.float64)
    # Standard deviation
    sdbelow = data1[:]-sd[:]
    sdabove = data1[:]+sd[:]
    return data1,sdbelow,sdabove

