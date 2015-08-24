#!/usr/bin/python
#************************************************************
# zonal mean of variable
# INPUT: Full 3D field
#************************************************************
import os
import datetime
localtime = datetime.datetime.now().strftime("%Y_%m_%d")

import netCDF4 as ncdf
import numpy as np

import pylab
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as clrs
import custom_colors as ccol

#import calc_area
import tropmask_84
#import convert_time
import jobs2
import convert_unit
#import calc_budget
import variables_attributes
#import data_range
#import dims
import plots
#import names
#import units
#************************************************************
# Set up
#************************************************************
disk      = 'tacitus'
jobid     = 'xleos'
plottitle = jobid
stash     = '_oh'
var       = jobs2.variable[jobs2.stash.index(stash)]
unit      = 'pptv'
frmat     = '%2.2f'
latbounds = [90,90]
nyrs	  = 0		# length of run in years
xx	  = -12*nyrs 	# (until end in months)
l         = False 
levs      = np.arange(0,25,1)

outdir    ='/home/ih280/Analysis/fixedOH/plots/zonal_mean/individual_plots/'
if not os.path.exists(outdir):
    os.makedirs(outdir)

# labels
ylab	  = r'Height / km'
ylim      = [0,20]

# labels 
label=plots.labels()

# Colours
c=ccol.custom_colors('grads')
cmap = cm.bwr
cnorm=clrs.Normalize(cmap,clip=False)
cmap.set_under(color=cmap(0.0),alpha=1.0)
cmap.set_over(color=cmap(1.0),alpha=1.0)

#************************************************************
# TROPOPAUSE
trophgt	    = ncdf.Dataset('/'+disk+'/ih280/um/'+jobid+'/'+jobid+'_trophgt.nc','r')	
tropheight  = trophgt.variables['tropopause_height'] #time,lat,lon
trop        = np.mean(np.mean(\
              tropheight[xx:,:,:]\
              , axis=2, dtype=np.float64)\
              , axis=0, dtype=np.float64)
tropstd     = np.std(np.mean(\
              tropheight[xx:,:,:]\
              , axis=2, dtype=np.float64)\
              , axis=0, dtype=np.float64)
tropmin	    = np.min(np.mean(\
              tropheight[xx:,:,:]\
              , axis=2, dtype=np.float64)\
              , axis=0)
tropmax	    = np.max(np.mean(\
              tropheight[xx:,:,:]\
              , axis=2)\
              , axis=0)

#***********************************************************
# TROPOSPHERIC MASK: 1 for troposphere, 0 other                         
#INPUT: 
#ncfile = file containing tropopause height
#LTROP  = 1 for troposphere (i.e. mask out stratosphere); 0 otherwise
#tmean  = 0 (no time meaning),
#         1 (climatological monthly mean), 
#         2 (full time mean), 
#         in order of most to least expensive!
#         5 (no time dimension)
#nyrs   = length of run in years (if nyrs = 0: entire run)

# VN 7.3:
#nchgt      = ncdf.Dataset('/'+disk+'/ih280/um/'+jobid+'/'+jobid+'_trophgt.nc','r')
#mask       = tropmask.mask(nchgt,1,0,nyrs)

# VN 8.4:
nctrop     = ncdf.Dataset('/'+disk+'/ih280/um/'+jobid+'/'+jobid+'_troppres.nc','r')
ncpres     = ncdf.Dataset('/'+disk+'/ih280/um/'+jobid+'/'+jobid+'_P-theta.nc','r')
#mask       = mask(nctrop,ncpres,1,0,nyrs)
mask       = tropmask_84.mask(nctrop,ncpres,1,0,nyrs)

#print 'Completed calculating mask'
#del mask, nchgt, nctrop, ncpres 

#************************************************************
# DATA
# Read in files
file1     = '/'+disk+'/ih280/um/'+jobid+'/'+jobid+stash+'.nc'
ncbase    = ncdf.Dataset(file1,'r')
# time,model_level_number,latitude,longitude

# dimensions
lat       = np.array(ncbase.variables['latitude'],dtype=np.float64)[:]
hgt       = np.array(ncbase.variables['level_height'],dtype=np.float64)[:]

data	= ncbase.variables[var]
print data

#import numpy.ma as ma
#new_data = np.ma.masked_where(np.ma.getmask(mask), data)

# attributes
attributes = variables_attributes.attributes(var)
name       = attributes[0]
formula    = attributes[2]
# Convert unit 
conversion = convert_unit.convert(unit,var)
data       = data[:]*conversion
data       = data[:]*mask[:]

#data_m     = data[:]
#np.ma.set_fill_value(data_m,0.)
#data_m[data_m.mask] = data_m.fill_value

# Zonal mean
data1 = np.mean(np.mean(\
	data[:,:,:,:]\
	, axis=3, dtype=np.float64)\
	, axis=0, dtype=np.float64)
#sd1   = np.std(np.mean(\
#	data[:,:,:,:]\
#	, axis=3, dtype=np.float64)\
#	, axis=0, dtype=np.float64)

#************************************************************
# PLOT Data
plotname 	= jobid+stash+'_contour_'+localtime+'.png'
# size
plt.figure	(figsize=(11.69,8.27), dpi=100) #A4 figure(figsize=(8.27, 11.69), dpi=100)
plt.subplots_adjust(left=0.075, bottom=0.2,\
		    right=0.975, top=0.95,\
		    wspace=0.15, hspace=0.23)

plt.subplot	(1,1,1, axisbg=	'#CCCCCC')

plt.plot  	(lat, trop[:]*1E-3	 , 'g-', lw=3, label='Tropopause')
plt.plot  	(lat, (trop[:]+tropstd[:])*1E-3, 'g--', lw=3)
plt.plot  	(lat, (trop[:]-tropstd[:])*1E-3, 'g--', lw=3)
plt.legend	(loc = 'upper right', frameon = False, fontsize = 24)

if l:
  CS =	 	plt.contour(lat[:], np.array(hgt[:])*1E-3, data1[:]\
		, levs, inline=1, fontsize=18, colors='k')
  plt.clabel	(CS, fmt=frmat, inline=1, fontsize=18)
  CS =		plt.contourf(lat[:], np.array(hgt[:])*1E-3, data1[:]\
		, levs, inline=1, fontsize=18, cmap=c)
else:
  CS =            plt.contour(lat[:], np.array(hgt[:])*1E-3, data1[:]\
                , inline=1, fontsize=18, colors='k')
  plt.clabel      (CS, fmt=frmat, inline=1, fontsize=18)
  CS =            plt.contourf(lat[:], np.array(hgt[:])*1E-3, data1[:]\
                , inline=1, fontsize=18, cmap=c)

plt.ylim	(ylim)

plt.ylabel	(ylab      , fontdict = label[3])
plt.xlabel	('Latitude', fontdict = label[3])

plt.title	(plottitle, fontdict = label[0])
plt.xticks	(np.arange(-90,120,30),\
		['90S','60S','30S','EQ','30N','60N','90N'])
plt.tick_params	(axis='both', which='major'\
		, labelsize=24, pad=10, direction='in', length=8)

cax = 		pylab.axes([0.2, 0.09, 0.6, 0.015]) 
cbar = 		plt.colorbar(cax=cax,orientation='horizontal')
#cbar.set_ticks(clevs[0][xx].tolist())
cbar.set_label	(formula+' /'+unit,fontdict=label[0])
cbar.ax.tick_params(labelsize=24)

plt.savefig	(outdir+plotname)
plt.show	()

#************************************************************
# PLOT SD
#plotname 	= jobid+stash+'_sd_contour_'+localtime+'.png'
# size
#plt.figure	(figsize=(15,12))
#plt.subplots_adjust(left=0.075, bottom=0.2,\
#		    right=0.975, top=0.95,\
#		    wspace=0.15, hspace=0.23)

#plt.subplot	(1,1,1)

#plt.plot  	(lat, trop[:]*1E-3	 , 'g-' , lw=3, label='Tropopause')
#plt.plot  	(lat, (trop[:]+tropstd[:])*1E-3, 'g--', lw=3)
#plt.plot  	(lat, (trop[:]-tropstd[:])*1E-3, 'g--', lw=3)
#plt.legend	(loc = 'upper right', frameon = False, fontsize = 24)

#CS = 		plt.contour(lat[:], np.array(hgt[:])*1E-3, sd1[:]\
#		, inline=1, fontsize=15, colors='k')
#plt.clabel	(CS,fmt = '%.3f',inline=1, fontsize=18)
#plt.clabel(CS,fmt = '%.1e',inline=1, fontsize=18)
#CS =		plt.contourf(lat[:], np.array(hgt[:])*1E-3, sd1[:]\
#		, inline=1, fontsize=15, cmap=c)

#plt.ylim	(ylim)

#plt.ylabel	(ylab	     , fontdict = label[3])
#plt.xlabel	('Latitude', fontdict = label[3])

#plt.tick_params	(axis='both', which='major'\
#		, labelsize=24, pad=10, direction='in', length=8)
#plt.title	(plottitle, fontdict = label[0])

#cax = 		pylab.axes([0.2, 0.09, 0.6, 0.015]) 
#cbar = 		plt.colorbar(cax=cax,orientation='horizontal')
#cbar.set_ticks(clevs[0][xx].tolist())
#cbar.set_label	('SD '+formula,fontdict=label[0])
#cbar.ax.tick_params(labelsize=24)

#plt.savefig	(outdir+plotname)
#plt.show	()


