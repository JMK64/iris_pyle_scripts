'''
Tropospheric mask: 1 for troposphere, 0 for statosphere
(Creates a python mask that can be used for any calculation)
Tropospheric height (STASH 30453)
UM: 2K.km-1 lapse rate threshold [WMO, 1057]

INPUT: 
ncfile	= file containing tropopause height
LTROP  	= 1 for troposphere (i.e. mask out stratosphere); 0 otherwise
tmean	= 0 (no time meaning),
	  1 (climatological monthly mean), 
	  2 (full time mean), 
	  in order of most to least expensive!
nyrs	= length of run in years (0 if the entire data is required

OUTPUT:
mask
'''
#*****************************************************************************************************************
# Script to create masks
#*****************************************************************************************************************

import netCDF4 as ncdf
import scipy
import numpy as np
import numpy.ma as ma

#*****************************************************************************************************************
def mask(ncfile,LTROP,tmean,nyrs):
    trophgt = np.array(ncfile.variables['tropopause_height']\
	, dtype=np.float64)[-12*nyrs:]   
#
    lat  = ncfile.variables['latitude'][:]
    lon  = ncfile.variables['longitude'][:]
    hgt  = range(60)
    time = ncfile.variables['time'][-12*nyrs:]
#
    mask = np.zeros([len(time),len(hgt),len(lat),len(lon)],dtype=np.float64)
#
    volfile 	= ncdf.Dataset(\
	'/homes/pjt50/plotting/idl/newncfiles/ukca_geovol.nc','r')
    modhgt = np.array(volfile.variables['geop_theta']\
	, dtype=np.float64)[:]    
#
    if tmean==0:
      # no time meaning
      for i in range(len(time)):
          for j in range(len(hgt)):
              for k in range(len(lat)):
                  for l in range(len(lon)):
                      if modhgt[0,j,k,l] <= trophgt[i,k,l]: 
                          mask[i,j,k,l] = LTROP
#
    elif tmean==1:
      # climatological, monthly mean
      trophgt_mean = np.empty([12,len(lat),len(lon)],dtype=np.float64)
      for it in range(12):
         jt = range(it,nyrs*12,12)
         trophgt_mean[it,:,:] = np.mean(trophgt[jt,:,:],axis=0)
      mask = np.empty([12,len(hgt),len(lat),len(lon)],dtype=np.float64)
      for ilat in range(len(lat)):
         for ilon in range(len(lon)):
            for ihgt in range(len(hgt)):
               for itim in range(12):
                  if modhgt[0,ihgt,ilat,ilon]<=trophgt_mean[itim,ilat,ilon]:
                     mask[itim,ihgt,ilat,ilon] = LTROP
    elif tmean==2:
      # full time mean
      trophgt_mean = np.mean(trophgt,axis=0,dtype=np.float64)
      mask = np.empty([len(hgt),len(lat),len(lon)],dtype=np.float64)
      for ilat in range(len(lat)):
         for ilon in range(len(lon)):
            for ihgt in range(len(hgt)):
                if modhgt[0,ihgt,ilat,ilon]<=trophgt_mean[ilat,ilon]:
                   mask[ihgt,ilat,ilon] = LTROP
    elif tmean==5:
      # no time dimension
      trophgt_mean = trophgt[:]
      mask = np.empty([len(hgt),len(lat),len(lon)],dtype=np.float64)
      for ilat in range(len(lat)):
         for ilon in range(len(lon)):
            for ihgt in range(len(hgt)):
                if modhgt[0,ihgt,ilat,ilon]<=trophgt_mean[ilat,ilon]:
                   mask[ihgt,ilat,ilon] = LTROP
    mmask = np.ma.masked_where(mask==0,mask)
    return mmask

#*****************************************************************************************************************
def mask_V1(ncbase,jobid):
# Tropospheric mask: 1 for troposphere, 0 other				
    lat  = ncbase.variables['latitude'][:]
    lon  = ncbase.variables['longitude'][:]
    hgt  = range(60)
    time = ncbase.variables['time'][:]
#
    mask = np.zeros([len(time),len(hgt),len(lat),len(lon)],dtype=np.float64)
#
    volfile 	= ncdf.Dataset(\
	'/homes/pjt50/plotting/idl/newncfiles/ukca_geovol.nc','r')
    modhgt = np.array(volfile.variables['geop_theta']\
	, dtype=np.float64)[:]    
#
    hgtfile = ncdf.Dataset(\
	'/tacitus/ih280/um/'+jobid+'/'+jobid+'_trophgt.nc','r')
    trophgt = np.array(hgtfile.variables['tropopause_height']\
	, dtype=np.float64)[:]   
#
    # generate trop mask -- remove strat
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            for k in range(len(mask[i][j])):
                for l in range(len(mask[i][j][k])):
                    if modhgt[0,j,k,l] <= trophgt[i,k,l]: 
                        mask[i,j,k,l] = 1
#
    mmask = np.ma.masked_where(mask==0,mask)
    return mask

#*****************************************************************************************************************
def mask_XXXX(ncbase,jobid):
# Tropospheric mask: 1 for troposphere, 0 other				
    lat = ncbase.variables['latitude'][:]
    lon = ncbase.variables['longitude'][:]
    hgt = ncbase.variables['level_height'][:]
    time = ncbase.variables['time'][:]
#
    mask = np.empty([len(time),len(hgt),len(lat),len(lon)],dtype=np.float64)
#
    volfile 	= ncdf.Dataset(\
	'/homes/pjt50/plotting/idl/newncfiles/ukca_geovol.nc','r')
    modhgt = np.array(volfile.variables['geop_theta']\
	, dtype=np.float64)[:]    
#
    hgtfile = ncdf.Dataset(\
	'/scratch/ih280/um/'+jobid+'/'+jobid+'_trophgt.nc','r')
    trophgt = np.array(hgtfile.variables['tropopause_height']\
	, dtype=np.float64)[:]   
#
    # generate trop mask -- remove strat
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            for k in range(len(mask[i][j])):
                for l in range(len(mask[i][j][k])):
                    if modhgt[0,j,k,l] <= trophgt[i,k,l]: 
                        mask[i,j,k,l] = 0
                    else: 
                        mask[i,j,k,l] = 1
    return mask

#*****************************************************************************************************************

