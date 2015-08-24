#!/usr/bin/python
#************************************************************
# Plot map of tropospheric component of a 3D variable
# Average in time
# Input: Full 3D field
# Ines Heimann, May 2015`
#************************************************************
import os
import datetime
localtime = datetime.datetime.now().strftime("%Y_%m_%d")

import netCDF4 as ncdf
import numpy as np
import numpy.ma as ma

import pylab
import matplotlib.pyplot as plt
import mpl_toolkits.basemap as basemap
import matplotlib.cm as cm
import matplotlib.colors as clrs
import matplotlib.pyplot as plt

import custom_colors as ccol

import scipy.optimize as sciopt

import convert_time
import variables_attributes
import convert_unit
import jobs2
import plots

import tropmask      # for VN 7.3
import tropmask_84   # for VN 8.4
#************************************************************
# File and names
disk      = 'tacitus'
jobid     = 'xjmxe'
stash     = '_ch4'
unit      = 'ppbv'
nyrs      = 0   # entire run length
plottitle = jobs2.metas[jobs2.jobid.index(jobid)]
var       = jobs2.variable[jobs2.stash.index(stash)]

# range for contour limits 
#levs	= np.arange(1.65,1.95,0.025)

plotname  = jobid+stash+'_'+localtime+'.png'
outdir    = 'xx'
if not os.path.exists(outdir):
    os.makedirs(outdir)

#************************************************************
# label format 
fmtlab    = plots.labels()

# Colours
c=ccol.custom_colors('grads')
cmap = cm.bwr
cnorm=clrs.Normalize(cmap,clip=False)
cmap.set_under(color=cmap(0.0),alpha=1.0)
cmap.set_over(color=cmap(1.0),alpha=1.0)
#************************************************************
# Read in files
# time,model_level_number,latitude,longitude

file1     = '/'+disk+'/ih280/um/'+jobid+'/'+jobid+stash+'.nc'
ncbase    = ncdf.Dataset(file1,'r')

data       = ncbase.variables[var]
print data

# attributes
attributes = variables_attributes.attributes(var)
varname       = attributes[0]
formula    = attributes[2]

# convert to unit
conversion = convert_unit.convert(unit,var)
data       = data[:]*conversion

#***********************************************************
# Tropospheric mask: 1 for troposphere, 0 other				
#INPUT: 
#ncfile	= file containing tropopause height
#LTROP  = 1 for troposphere (i.e. mask out stratosphere); 0 otherwise
#tmean  = 0 (no time meaning),
#	  1 (climatological monthly mean), 
#	  2 (full time mean), 
#	  in order of most to least expensive!
#         5 (no time dimension)
#nyrs	= length of run in years (if nyrs = 0: entire run)

# VN 7.3:
nchgt      = ncdf.Dataset('/'+disk+'/ih280/um/'+jobid+'/'+jobid+'_trophgt.nc','r')
mask       = tropmask.mask(nchgt,1,0,nyrs)

# VN 8.4:
#nctrop     = ncdf.Dataset('/'+disk+'/ih280/um/'+jobid+'/'+jobid+'_troppres.nc','r')
#ncpres     = ncdf.Dataset('/'+disk+'/ih280/um/'+jobid+'/'+jobid+'_P-theta.nc','r')
#mask       = tropmask_84.mask(nctrop,ncpres,1,5,nyrs)

data       = data[:]*mask[:]
print 'Completed calculating mask'
#del mask, nchgt, nctrop, ncpres 

#************************************************************
base       = np.mean(np.mean(\
             data[:,:,:,:]\
           , axis=1, dtype=np.float64)\
           , axis=0, dtype=np.float64)

lat        = np.array(ncbase.variables['latitude'],dtype=np.float64)[:]
lon        = np.array(ncbase.variables['longitude'],dtype=np.float64)[:]

#************************************************************
# Plot
plt.figure	(figsize=(10,8), facecolor='0.75')
plt.title       (plottitle, fontdict=fmtlab[0])

# lat lon cyclic
base,lon   = basemap.addcyclic(base,lon)
base,lon   = basemap.shiftgrid(180.,base,lon,start=False)
lon, lat   = np.meshgrid      (lon, lat)

map 	   = basemap.Basemap(projection='cyl',lon_0=0)
x, y 	   = map	(lon,lat)
map.drawcoastlines	()
# map.drawcountries()
map.drawmapboundary	()

map.drawmeridians	(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1], fontdict=fmtlab[1], yoffset=8)
map.drawparallels	(np.arange(-90,120,30),labels=[1,0,0,0], fontdict=fmtlab[1])

cplot=map.contourf      (x,y,base[:,:], extend='both', cmap=c)
#cplot=map.contourf	(x,y,base[:,:], levs, extend='both', cmap=c) 

# Overall colour bar
cax        = pylab.axes	([0.2, 0.1, 0.6, 0.02])
cbar       = pylab.colorbar(cax=cax, orientation='horizontal', extend='both', format = '%.0f')
#cbar       = pylab.colorbar(cax=cax, orientation='horizontal', ticks=levs[::2], extend='both')
cbar.set_label          (formula+' / '+unit, fontdict=fmtlab[1])
cbar.ax.tick_params     (labelsize=18, pad=5)

#plt.savefig	        (outdir+plotname)
plt.show 	        ()


