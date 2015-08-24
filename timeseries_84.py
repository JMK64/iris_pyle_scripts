#!/usr/bin/python
#************************************************************
# Plot CH4 as a function of time for specified lat bands with exponential function fitted to the annual data.
# Input: Full 3D field
#************************************************************
import os
import datetime
localtime = datetime.datetime.now().strftime("%Y_%m_%d")

import netCDF4 as ncdf
import numpy as np
#import numpy.ma as ma

import matplotlib.pyplot as plt
import custom_colors as ccol
import scipy.optimize as sciopt

import convert_time
import variables_attributes
import convert_unit
import jobs2
import plots
import tropmask_84

#************************************************************
# File and names
disk      = 'tacitus'
jobid     = 'xleos'

flux      = False
#stash     = ['_o1dfix+ch4anth','_o1dfix+ch4wetl']
#stash     = ['_ch4+oh','_ohfix+ch4anth','_ohfix+ch4wetl']
stash     = ['_ch4','_ch4anth','_ch4wetl','_ch4hydr','_ch4term','_ch4soil']
var       = []
for s in stash:
  var.append(jobs2.variable[jobs2.stash.index(s)])

nyrs	  = 0 	# entire run lenght
ylabel    = r'$\mathbf{CH_{4}}$'
unit      = 'ppbv'

# lat bounds in south, north 
latbounds = [30,30]
if flux:
  title     = 'Tropospheric Average'+'\n'+str(latbounds[0])+' S, '+str(latbounds[1])+' N'
else:
  title     = 'Tropospheric Sum'+'\n'+str(latbounds[0])+' S, '+str(latbounds[1])+' N'

#title     = jobs2.metas[jobs2.jobid.index(jobid)]+'\nTropospheric Average'
plotname  = jobid+stash[0]+'_'+str(latbounds[0])+'S'+str(latbounds[1])+'N_'+localtime+'.png'

outdir    = '/home/ih280/Analysis/fixedOH/plots/time_evolution/individual_plots/'
if not os.path.exists(outdir):
    os.makedirs(outdir)

# range for y limits for the different lat bands
#ylim      = [1.72,1.82]

# axis range
#steps     = np.arange(2000,2030+5,5)
#ticks     = []
#for t in steps:
#    ticks.append(datetime.datetime(t,1,1,0,0))

# label format 
fmtlab    = plots.labels()

#************************************************************
# Tropospheric mask: 1 for troposphere, 0 other                         
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
mask       = tropmask_84.mask(nctrop,ncpres,1,0,nyrs)

#************************************************************
# Read in files
data = []
name = []
for i in range(len(stash[:])):
  file1      = '/'+disk+'/ih280/um/'+jobid+'/'+jobid+stash[i]+'.nc'
  ncbase     = ncdf.Dataset(file1,'r')
# read in data
  data_in    = ncbase.variables[var[i]]
  print data_in
# attributes
  attributes = variables_attributes.attributes(var[i])
  if stash[i] == '_ch4':
    name.append  (attributes[0]+' free running')
  else:
    name.append  (attributes[0])
# unit conversion 
  conversion = convert_unit.convert(unit,var[i])
  data_in    = data_in[:]*conversion
# dimensions 	dimensions = dims.dimensions(ncbase,jobid)
  lat        = np.array(ncbase.variables['latitude'],dtype=np.float64)[:]
  lon        = np.array(ncbase.variables['longitude'],dtype=np.float64)[:]
  hgt        = np.array(ncbase.variables['level_height'],dtype=np.float64)[:]
  mon        = np.array(ncbase.variables['time'],dtype=np.float64)[:]
# Convert time
  reftime    = str(ncbase.variables['forecast_reference_time'].units)[12:]	
  time       = convert_time.convert_time(reftime,mon)
  del reftime
# latitudianal bands
  south      = np.where(lat == -latbounds[0])[0][0]
  north      = np.where(lat ==  latbounds[1])[0][0]
# Mask out stratosphere
  data_in    = data_in[:]*mask[:]
# CALCULATION:
# data1 = FUNCTION OF TIME
  if flux:
# SUM OVER ALL LONGITUDE, SPECIFIED LATITUDES, TROPOSPHERE
    data1    = np.sum(np.sum(np.sum(\
             data_in[:,:,south:north,:]\
             , axis=3, dtype=np.float64)\
             , axis=2, dtype=np.float64)\
             , axis=1, dtype=np.float64)
  else:
# MEAN OVER ALL LONGITUDE, SPECIFIED LATITUDES, TROPOSPHERE
    data1    = np.mean(np.mean(np.mean(\
             data_in[:,:,south:north,:]\
             , axis=3, dtype=np.float64)\
             , axis=2, dtype=np.float64)\
             , axis=1, dtype=np.float64)
  data.append  (data1[:])

#************************************************************
# CALCULATION:
# ANNUAL AVERAGES, INCLUDING STANDARD DEVIATION

#avgdata    = []
#sddata     = []
#timeyear   = []
#monyear    = []
#for k in range(len(time)/12):
#    avgdata.append  (np.mean (data1[k*12:k*12+11]))
#    sddata.append   (np.std  (data1[k*12:k*12+11]))
#    timeyear.append (time[k*12+6])
#    monyear.append  (mon[k*12+6])

#sdbelow    = []
#sdabove    = []
#for k in range(len(sddata)):
#    sdbelow.append(avgdata[k]-sddata[k])
#    sdabove.append(avgdata[k]+sddata[k])

#************************************************************
# PLOT
plt.figure	(figsize=(10,8))

# ANNUAL AVERAGE
#plt.plot	(timeyear, sdbelow, color='0.75', lw=2\
#		, label = '1'+r'$\mathbf{\sigma}$'+' annual variability')
#plt.plot	(timeyear, sdabove, color='0.75', lw=2)
#plt.fill_between(timeyear, sdbelow, sdabove,facecolor='0.75')
#plt.plot	(timeyear, avgdata, 'r-', lw=2
#		, label = 'Annual average')

# MONTHLY DATA
for i in range(len(stash)):
  colour = ['r','g','b','k','m','c','y','0.75','0.5','0.25']
  plt.plot       (range(len(data[i])), data[i], color=colour[i], lw=2\
               , label = name[i])

# PLOT LABELS
plt.legend	(loc='upper right', frameon=False\
		, labelspacing = 1, fontsize = 20)
#plt.xticks	(ticks)
#plt.ylim	(ylim)

plt.xlabel	('Time step in months',fontdict=fmtlab[1])   
plt.ylabel	(ylabel+' /'+unit,fontdict=fmtlab[1])
#ax.xaxis.set_major_formatter('%2.0f')
locs,labels 	= plt.yticks()
plt.tick_params	(axis='both', which='major', labelsize=20, pad=10\
		, direction='in', length=8)
plt.title	(title, fontdict=fmtlab[0])

# OUTPUT
plt.savefig	(outdir+plotname)
plt.show        ()



