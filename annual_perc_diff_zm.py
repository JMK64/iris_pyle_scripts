#!/usr/bin/python
#********************************************************************************************************
# Plot annual mean, zonal mean % change 
# Input = time series of zonal mean variable; full 3D field tropopause height (first run only)
# If more than one variable given, sums up vmrs (e.g. OH + HO2 to HOx)
# AB 2015

#********************************************************************************************************
import numpy as np
import netCDF4 as ncdf
import tracer_var_codes as vcode
import jobs 
import masks
import cspecies
import model_params as mprms
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib import rcParams
import matplotlib.cm as cm
import matplotlib.colors as colors
import custom_colors as ccol

#********************************************************************************************************
# Supply some information
# jobids
modnames = ['xhkqh','xhkqk']
nyrs     = 10		# length of run
pval     = 2.10		# Manual t-testing; df=18 for nyrs=10
varnames = ['o3']
filenames= ['o3']
pltname  = 'o3'	

# plot parameters
title    = 'O3'
xlab     = 'Latitude'
ylab     = 'Altitude / km'
clab     = '%'
lim      = 20		# shading limits
by       = 2
clim     = 20		# contour limits	
cby      = 4
lid      = 20 		# y axis limit / km
cdp      = 0
yby      = 5
ytcks    = np.arange(0,lid+yby,yby)
levs     = np.arange(-lim,lim+by,by)
clevs    = np.arange(-clim,clim+by,cby)
cols     = ccol.custom_colors('grads')
outdir   = '/home/ab728/python/output/'

#********************************************************************************************************
# Fetch job attributes and files
nrun=len(modnames)
nvar=len(varnames)

# get job labels
modmetas = []
for modname in modnames:
   meta = jobs.metas[jobs.jobid.index(modname)]
   modmetas.append(meta)

# find netcdf files
# in format: [[mod1var1,mod1var2,...],[mod2var1,mod2var2,...],...]
ncmods = []
for i in range(nrun):
   ncmods.append([])
   for j in range(nvar):
      moddisk   = jobs.disks[jobs.jobid.index(modnames[i])]
      ncpath    = '/'+moddisk+'/ab728/'+modnames[i]+'/'+modnames[i]+'_zm_'+filenames[j]+'.nc'
      #print ncpath
      ncmod     = ncdf.Dataset(ncpath,'r')
      ncmods[i].append(ncmod)
   if len(ncmods)==1:
      tpath  = '/'+moddisk+'/ab728/'+modnames[i]+'/'+modnames[i]+'_trophgt.nc'
      nctrop = ncdf.Dataset(tpath,'r')

#********************************************************************************************************
# VAR_PROC calculates zonal mean (as input), climatological annual mean and variance
def var_proc(ncmod):

   # extract dimensions
   global lat, hgt, tim
   lat=ncmod[0].variables['latitude'][:]
   hgt=ncmod[0].variables['hybrid_ht'][:]
   tim=ncmod[0].variables['t'][:]

   tvars=[]
   vvars=[]
   for j in range(nvar):
      # variable code and mmr-vmr conversion factor
      code = vcode.codes[varnames[j]]
      cspc = cspecies.cspec[varnames[j]]
      print code, cspc

      # get variable
      var = np.array(ncmod[j].variables[code], dtype=np.float64)[:,:,:,0]/cspc

      # time mean
      tvar = np.mean(var, axis=0, dtype=np.float64)
      tvars.append(tvar)

      # yearly mean
      yvar = np.empty((nyrs,len(hgt),len(lat)))
      for i in range(0,nyrs):  
         jan = 12*i
         yvar[i,:,:] = np.mean(var[jan:jan+12,:,:], axis=0, dtype=np.float64)

      # variance 
      vvar=np.var(yvar, axis=0, dtype=np.float64)
      vvars.append(vvar)

   # sum up (no effect if only one variable)
   tvar = sum(tvars)
   vvar = sum(vvars)
   
   return(tvar,vvar)

#********************************************************************************************************
# TROP_HGT calculates zonal mean tropopause height
def trop_hgt():

   # get tropopause height
   trophgt    = np.array(nctrop.variables['ht'], dtype=np.float64)[:,0,:,:]	# metres
   zttrophgt  = trophgt.mean(axis=2, dtype=np.float64).mean(axis=0, dtype=np.float64)

   return(zttrophgt)

#********************************************************************************************************	
# Calculate mean, t-statistics and tropopause height
base = var_proc(ncmods[0])
mod1 = var_proc(ncmods[1])

# Means
mbase = base[0]
mmod1 = mod1[0]

# Variances
vbase = base[1]
vmod1 = mod1[1]

# Mean difference 
diff = mmod1 - mbase 
pdiff = diff / mbase * 100
# T-test with n=10, df=18, pvalue=0.05, tvalue=2.10
tvals = abs(diff)/np.sqrt(vbase/nyrs+vmod1/nyrs)

# Tropopause height of base run
trophgt  = trop_hgt()

#********************************************************************************************************
# Plot
# some stuff copied from contourf_demo.py
# contour / contourf return ContourSet objects
CS  = plt.contourf(lat, hgt/1000, pdiff, levels=levs, cmap=cols, extend='both')
CS2 = plt.contour(lat, hgt/1000, pdiff, levels=clevs, colors='black', hold='on', linewidths=0.5)
plt.plot(lat,trophgt/1000,color='darkgreen', linewidth=2)
plt.title('Zonal mean difference in '+title+'\n'+modmetas[1]+'-'+modmetas[0]+', Annual Mean', fontsize=22)
plt.clabel(CS2, fontsize=16, fmt='%.'+str(cdp)+'f')
plt.xlabel(xlab,fontsize=22)
plt.ylabel(ylab,fontsize=22)
plt.tick_params(axis='both', which='major', labelsize=22)
plt.xticks(np.arange(-90,120,30), ['90S','60S','30S','EQ','30N','60N','90N'])
plt.yticks(ytcks)
plt.ylim((0,lid))
# Make a colorbar for the ContourSet returned by the contourf call.
cbar = plt.colorbar(CS, orientation='horizontal')
cbar.ax.set_xlabel(clab, fontsize=22)
cbar.ax.tick_params(labelsize=22)

# Shade OUT non-significance
for h in range(0,len(hgt)-1):
   for l in range(0,len(lat)-1):
      if(tvals[h,l]<pval):
         x1 = lat[l]
         x2 = lat[l+1]
         y1 = hgt[h]/1000
         y2 = hgt[h+1]/1000
         plt.fill([x1,x2,x2,x1],[y1,y1,y2,y2],edgecolor='grey',fill=False,hatch='//',linewidth=0)
         plt.fill([x1,x2,x2,x1],[y1,y1,y2,y2],edgecolor='grey',fill=False,hatch='\\',linewidth=0) 

plt.savefig(outdir+pltname+'_annual_'+modnames[1]+'-'+modnames[0]+'.png', bbox_inches='tight')


