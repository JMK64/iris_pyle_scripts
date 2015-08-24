import numpy as np
import netCDF4 as ncdf

#*****************************************************************************************************************
# Module to extract netcdf objects containing gridbox volume and area of the model
# AB 2015

#*****************************************************************************************************************

ncvol  = ncdf.Dataset('/homes/pjt50/plotting/idl/newncfiles/ukca_geovol.nc')
ncarea = ncdf.Dataset('/homes/pjt50/plotting/idl/newncfiles/surface_area.nc')
vol    = np.array(ncvol.variables['vol_theta'],dtype=np.float64)[0,:,:,:]	# m-3, 3D (hgt, lat, lon)
area   = np.array(ncarea.variables['field'],dtype=np.float64)			# m-2, 2D (lat,lon)

