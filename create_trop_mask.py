import numpy as np
import netCDF4 as ncdf
import cspecies

#*****************************************************************************************************************
# Module to create tropospheric/stratospheric mask
# AB 2015

#*****************************************************************************************************************
""" 
Trop/strat mask defined by UM diagnosed thermal tropopause 
STASH 30453, Height at Tropopause Level
Defined by 2Kkm-1 lapse rate threshold [WMO, 1957]

INPUT(S):
ncmod	= file containing tropopause height
L_TROP  = 1 for troposphere (i.e. mask out stratosphere); 0 otherwise
tmean   = 0 (no time meaning), 1 (climatological monthly mean), 2 (full time mean), <- in order of most to least expensive!
zmean   = 0 (no zonal meaning), 1 (zonal meaning)
nyrs    = length of run in years

OUTPUT(S):
mask

CONDITION(S):
if tmean==2, requires global variable nyrs
"""
def trop_mask(ncmod,L_TROP,tmean,zmean,nyrs):
   # get tropopause height
   trophgt = np.array(ncmod.variables['ht'],dtype=np.float64)[:,0,:,:]	# metres

   # get dimensions
   lon = ncmod.variables['longitude'][:]
   lat = ncmod.variables['latitude'][:]
   tim = ncmod.variables['t'][:]
   #hgt = ncmod.variables['hybrid_ht'][:]
   hgt = range(60)
   #print "Hybrid height levels not found in netcdf\nFetching from /homes/pjt50/plotting/idl/newncfiles/ukca_geovol.nc"
   nchgt   = ncdf.Dataset('/homes/pjt50/plotting/idl/newncfiles/ukca_geovol.nc','r')
   truehgt = nchgt.variables['geop_theta'][0,:,:,:]

   # no zonal meaning
   if not zmean:
      if tmean==0:
         # no time meaning
         mask = np.empty([len(tim),len(hgt),len(lat),len(lon)],dtype=np.float64)
         for ilat in range(len(lat)):
            for ilon in range(len(lon)):
               for ihgt in range(len(hgt)):
                  for itim in range(len(tim)):
                     if truehgt[ihgt,ilat,ilon]<=trophgt[itim,ilat,ilon]:
                        mask[itim,ihgt,ilat,ilon] = L_TROP
                     else:
                        mask[itim,ihgt,ilat,ilon] = 1-L_TROP
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
                     if truehgt[ihgt,ilat,ilon]<=trophgt_mean[itim,ilat,ilon]:
                        mask[itim,ihgt,ilat,ilon] = L_TROP
                     else:   
                        mask[itim,ihgt,ilat,ilon] = 1-L_TROP
      elif tmean==2:
         # full time mean
         trophgt_mean = np.mean(trophgt,axis=0,dtype=np.float64)
         mask = np.empty([len(hgt),len(lat),len(lon)],dtype=np.float64)
         for ilat in range(len(lat)):
            for ilon in range(len(lon)):
               for ihgt in range(len(hgt)):
                  if truehgt[ihgt,ilat,ilon]<=trophgt_mean[ilat,ilon]:
                     mask[ihgt,ilat,ilon] = L_TROP
                  else:
                      mask[ihgt,ilat,ilon] = 1-L_TROP

   # zonal meaning
   elif zmean:
      ztrophgt = np.mean(trophgt, axis=2, dtype=np.float64)
      ztruehgt = np.mean(truehgt, axis=2, dtype=np.float64)

      if tmean==0:
         # no time meaning
         mask = np.empty([len(tim),len(hgt),len(lat)],dtype=np.float64)
         for ilat in range(len(lat)):
            for ihgt in range(len(hgt)):
               for itim in range(len(tim)):
                  if ztruehgt[ihgt,ilat]<=ztrophgt[itim,ilat]:
                     mask[itim,ihgt,ilat] = L_TROP
                  else:
                     mask[itim,ihgt,ilat] = 1-L_TROP
      elif tmean==1:
         # climatological, monthly mean
         ztrophgt_mean = np.empty([12,len(lat)],dtype=np.float64)
         for it in range(12):
            jt = range(it,nyrs*12,12)
            ztrophgt_mean[it,:] = np.mean(ztrophgt[jt,:],axis=0)
         mask = np.empty([12,len(hgt),len(lat)],dtype=np.float64)
         for ilat in range(len(lat)):
            for ihgt in range(len(hgt)):
               for itim in range(12):
                  if ztruehgt[ihgt,ilat]<=ztrophgt_mean[itim,ilat]:
                     mask[itim,ihgt,ilat,] = L_TROP
                  else:   
                     mask[itim,ihgt,ilat] = 1-L_TROP
      elif tmean==2:
         # full time mean
         ztrophgt_mean = np.mean(ztrophgt,axis=0,dtype=np.float64)
         mask = np.empty([len(hgt),len(lat)],dtype=np.float64)
         for ilat in range(len(lat)):
            for ihgt in range(len(hgt)):
               if ztruehgt[ihgt,ilat]<=ztrophgt_mean[ilat]:
                  mask[ihgt,ilat] = L_TROP
               else:
                  mask[ihgt,ilat] = 1-L_TROP

   mmask = np.ma.masked_where(mask==0,mask)

   nchgt.close()

   return mmask

# chemical mask defined by 150 ppbv ozone contour (Prather et al., 2001)
def ozone_mask(ncmod,L_TROP,tmean,nyrs):
   # get tropopause height
   trophgt = np.array(ncmod.variables['tracer1'],dtype=np.float64)*1E9/cspecies.cspec['o3']	# ppbv

   # get dimensions
   lon = ncmod.variables['longitude'][:]
   lat = ncmod.variables['latitude'][:]
   tim = ncmod.variables['t'][:]
   hgt = ncmod.variables['hybrid_ht'][:]
   #hgt = range(60)

   if tmean==0:
      # no time meaning
      mask = np.empty([len(tim),len(hgt),len(lat),len(lon)],dtype=np.float64)
      for ilat in range(len(lat)):
         for ilon in range(len(lon)):
            for itim in range(len(tim)):
               for ihgt in range(len(hgt)):
                  if trophgt[itim,ihgt,ilat,ilon] <= 150:
                     mask[itim,ihgt,ilat,ilon] = L_TROP
                  else:
                     mask[itim,ihgt,ilat,ilon] = 1-L_TROP
   mmask = np.ma.masked_where(mask==0,mask)

   return mmask

#*****************************************************************************************************************

