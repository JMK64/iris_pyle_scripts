import numpy as np
import netCDF4
import time

from netCDF4 import Dataset
"""
renames netcdf variables via reading in a netcdf file, extracting the dims and
arrays and then creating a new file with modified dimension names etc

The spaces are not PEP-8 compliant, but I thought they improved readability.
So sue me.
"""

# get file containing heights, pressures for L85 ancil
input_filename  ='N48_L60_aircraft_ems.nc'
ncfile   = netCDF4.Dataset(input_filename)

# extract useful quantities
lon        = ncfile.variables['longitude'][:]
lat        = ncfile.variables['latitude'][:]
hybrid_ht  = ncfile.variables['hybrid_ht'][:]

times      = ncfile.variables['t']
tracer20   = ncfile.variables['tracer20']

nmonths, nheights, ny, nx = np.shape(tracer20)

# create netcdf file
output_filename = 'modded_N48_L60_aircraft_ems.nc'
dataset = netCDF4.Dataset(output_filename, 'w', format='NETCDF4')

# Global Attributes
dataset.description = 'NETCDF-CF COMPLIANT SCRIPT'
dataset.history     = 'Created ' + time.ctime(time.time())
dataset.source      = '' #FILL ME
dataset.Conventions = 'CF-1.0' # HA! LOL never in a million years!!
dataset.standard_name_vocabulary='CF-1.0'

height  = dataset.createDimension('hybrid_ht', nheights)
height  = dataset.createVariable('hybrid_ht',  np.int32,   ('hybrid_ht',))

time    = dataset.createDimension('time',      None)
time    = dataset.createVariable('time',       'f8', ('time',)) # or can use np as below

lat     = dataset.createDimension('latitude',  ny)
lat     = dataset.createVariable('latitude',   np.float32, ('latitude',))

lon     = dataset.createDimension('longitude', nx)
lon     = dataset.createVariable('longitude',  np.float32, ('longitude',))

dataout = dataset.createVariable('tracer', np.float32, ('time','hybrid_ht','latitude', 'longitude',))

# write out the output datafile lat,lon,height,time
lon[:]    = lon[:]
lat[:]    = lat[:]
height[:] = hybrid_ht[:]
time[:]   = times[:]

# write out 4D data, need to do a copy
dataout[:,:,:,:] = tracer20[:,:,:,:]

# Boilerplate for the netcdf file
# Variable Attributes
lat.standard_name = 'latitude'
lat.units = 'degrees_north'
lat.cartesian_axis = "Y"
lat.axis = 'Y'
lat.actual_range = -90.0, 90.0

lon.standard_name = 'longitude'
lon.units = 'degrees_east'
lon.cartesian_axis = "X"
lon.axis = "X"
lat.actual_range = 0.0, 360.0

dataout.units = 'MMR kg kg-1'
dataout.standard_name='Tracer_20_MMR'

height.units = 'm'
height.axis='Z'
height.positive='up'
height.standard_name = 'hybrid_pressure_levels'


time.standard_name = 'time'
time.long_name = 'time'
time.units = 'days since 1999-12-01 00:00:00'
time.calendar = '360_day'
time.axis = 'T'
print ('success')
dataset.close()
