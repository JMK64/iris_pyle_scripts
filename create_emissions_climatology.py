#!/usr/bin/python
#********************************************************************************************************
# Python Script to scale emissions 
# Emission data: Fung et al. 1991

# grid is N96L95 resolution
# longitude(x): 192 points; Start   0.0; spacing 1.875 degrees
# latitude(y) : 145 points; Start -90.0; spacing 1.25 degrees 

# Ines Heimann, Apr 2015
#********************************************************************************************************
import numpy as np
import netCDF4 as ncdf
import time
#********************************************************************************************************
# INPUT INFORMATION
#********************************************************************************************************
jobid    = 'xlgac'
var      = 'o3'
file1    = '/tacitus/dcw32/um/'+jobid+'/'+jobid+'_'+var+'.nc'
file2    = '/tacitus/dcw32/um/'+jobid+'/'+jobid+'_P-theta.nc'
outname  = '/scratch/ih280/um/'+jobid+'_'+var+'_clim.nc'
#file1    = '/tacitus/ih280/um/ancils/archer/xkjgja_methane.nc'
#outname  = '/tacitus/ih280/um/ancils/archer/xkjgja_'+var+'_methane.nc'
#********************************************************************************************************
# READ IN DATA
#********************************************************************************************************
ncbase    = ncdf.Dataset(file1,'r')

#var1    = []
#for i in ncbase.variables.items():
#    var1.append(str(i[0]))

data_in   = ncbase.variables[str(ncbase.variables.items()[0][0])]#[:]#v
lon_um    = ncbase.variables['longitude']#[:]
lat_um    = ncbase.variables['latitude']#[:]
hgt_um    = ncbase.variables['level_height']#[:]
t_um      = ncbase.variables['time']#[:]#t

ncpres    = ncdf.Dataset(file2,'r')
p_in      = ncpres.variables[str(ncpres.variables.items()[0][0])]#[:]#v

#********************************************************************************************************
# Create climatology 
#********************************************************************************************************
# Select data that should be averaged. 
# E.g. remove spin-up
# Start climatology on January
data_spin = data_in[:]
p_spin    = p_in   [:]

# Create average climatology
data_out = np.zeros((12,len(hgt_um),len(lat_um),len(lon_um)))
p_out    = np.zeros((12,len(hgt_um),len(lat_um),len(lon_um)))
for i in range(12):
    data_out[i] = np.mean(data_spin [i::12], axis=0)
    p_out[i]    = np.mean(p_spin    [i::12], axis=0)

#********************************************************************************************************
# Write out data
#********************************************************************************************************
print 'WRITE OUT NETCDF'
dataset = ncdf.Dataset(outname, 'w', format='NETCDF3_CLASSIC')

# Global Attributes
dataset.description = '12 months climatology'
dataset.history = 'Created ' + time.ctime(time.time())
dataset.source = 'UM-UKCA '+jobid 
dataset.Conventions = 'CF-1.0'
dataset.standard_name_vocabulary='CF-1.0'

#print dataset

#create output dimensions and variables
longitude    = dataset.createDimension('longitude',len(lon_um))
longitude    = dataset.createVariable('longitude','f4',('longitude'))

latitude     = dataset.createDimension('latitude',len(lat_um))
latitude     = dataset.createVariable('latitude','f4',('latitude'))

hybrid_ht    = dataset.createDimension('hybrid_ht',len(hgt_um))
hybrid_ht    = dataset.createVariable('hybrid_ht','f4',('hybrid_ht'))

t    = dataset.createDimension('t',12)
t    = dataset.createVariable('t','f4',('t'))

# copy lons, lats etc into netCDF variables
longitude[:] = lon_um[:]
latitude[:]  = lat_um[:]
hybrid_ht[:] = hgt_um[:]
t[:]         = t_um[:12]

# create the output dataset
source       = dataset.createVariable(var,'f4',('t','hybrid_ht','latitude','longitude'))
source[:]    = data_out[:]
pres         = dataset.createVariable('p','f4',('t','hybrid_ht','latitude','longitude'))
pres[:]      = p_out[:]

# Variable Attributes
latitude.standard_name   = 'latitude'
latitude.units           = 'degrees_north'
latitude.cartesian_axis  = "Y"
latitude.axis            = 'Y'
latitude.actual_range    = -90.0, 90.0

longitude.standard_name  = 'longitude'
longitude.units          = 'degrees_east'
longitude.cartesian_axis = "X"
longitude.axis           = "X"
longitude.actual_range   = 0.0, 360.0

hybrid_ht.standard_name  = 'hybrid_ht'
hybrid_ht.long_name      = 'Hybrid height'
hybrid_ht.units          = 'positive'
hybrid_ht.actual_range   = 0,85

t.standard_name          = 'time'
t.long_name              = 't'
t.units                  = 'days since 1984-09-01 00:00:00'
t.calendar               = '360_day'
t.axis                   = 'T'

source.units             = 'kg kg-1'
source.standard_name     = str(ncbase.variables.items()[0][0]) 
source.source            = 'UM-UKCA: '+jobid 
source.long_name         = var+' MASS MIXING RATIO'
source.missing_value     = 2.e+20
source.FillValue         = 2.e+20
source.valid_min         = 1.57685e-08
source.valid_max         = 9.67002e-07

pres.units               = 'Pa'
pres.standard_name       = 'air_pressure'
pres.source              = 'UM-UKCA: '+jobid
pres.long_name           = 'Air pressure'
pres.missing_value       = 2.e+20
pres.FillValue           = 2.e+20

#print dataset
print ('success')
dataset.close()

