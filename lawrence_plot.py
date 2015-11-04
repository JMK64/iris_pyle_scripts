#!/usr/bin/python
#**********************************************************
# Plot mass-weighted mean tropospheric OH 
# for subdomains presented in Lawrence et al., 2001, ACP
# Model data UM vn 8.4 
#
# Ines Heimann, June 2015
# based on David Wade, May 2015
# based on R script by Alex Archibald, February 2012
#**********************************************************
# Standard modules
import datetime
localtime = datetime.datetime.now().strftime("%Y_%m_%d")
import numpy as np 
import netCDF4 as ncdf
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

# Custom modules
import lawrence_oh as l_oh

#**********************************************************
jobid    = 'xjmxe'
um       = '7.3'
jobd     = ''
print jobid
nyrs     = 7 		# Allows to choose how many model years are to be averaged

Na       = 6.022E23	# Avogadro constant
kgoh     = 17E-3	# molmass of OH
#**********************************************************
# Domain analysis
# |  3  |  6  |  9  | 12  |     top hb[2]
# |  2  |  5  |  8  | 11  |     top hb[1]
# |  1  |  4  |  7  | 10  |     top hb[0]
# lb[0] lb[1] lb[2] lb[3] lb[4] lat

# lat boundaries
lb       = [-90,-30,0,30,91]
# hgt boundaries
hb       = [750,500,250]

#**********************************************************
# final vol is the volume of the gridboxes up to L63 in cm^3
if   um == '7.3':
    volfile  = ncdf.Dataset('/tacitus/ih280/um/n48_l60_geovol.nc')
    lat      = volfile.variables['Lat'][:]
    vol      = volfile.variables['vol_theta'][:]
    vol      = vol[0]*1E6   # cm-3
elif um == '8.4':
    volfile  = ncdf.Dataset('/tacitus/ih280/um/n96_l63_geovol.nc')
    lat      = volfile.variables['latitude'][:]
    vol      = volfile.variables['vol_theta'][:]
    vol      = vol*1E6   # cm-3

#**********************************************************
# OH mixing ration, pressure and airmass data from model run
(oh,P,airmass) = l_oh.lawr(jobid,nyrs)
#**********************************************************
# Tropospheric mask
pclim      = np.empty(len(lat))
l = 0
for ilat in lat:
  pclim[l] = 300 - 215 * (np.cos(ilat))**2
  l += 1

if   um == '7.3':
  mask     = np.zeros([60,73,96])
  P        = P[:,:,:]
  oh       = oh[:,:,:]
  airmass  = airmass[:,:,:]
  for ihgt in range(0,60):
    for ilat in range(0,73):
        for ilon in range(0,96):
            if P[ihgt,ilat,ilon]/100.0>= pclim[ilat]:
                mask[ihgt,ilat,ilon] = 1
elif um == '8.4':
  mask     = np.zeros([63,145,192])
  P        = P[:63,:,:]
  oh       = oh[:63,:,:]
  airmass  = airmass[:63,:,:]
  for ihgt in range(0,63):
    for ilat in range(0,145):
        for ilon in range(0,192):
            if P[ihgt,ilat,ilon]/100.0>= pclim[ilat]:
                mask[ihgt,ilat,ilon] = 1

#**********************************************************
# calculate OH in molecules cm^-3 and apply tropospheric mask
oh_box   = (Na*oh*airmass)/kgoh    # mol-1 kg(OH) kg-1(air) kg(air) / kg(OH)
oh_cm3   = oh_box/vol              # mol-1 / cm3

# Mass weighted, sub airmass for vol to become volume weighted
oh_trop  = "%.2e" %(np.sum(oh_cm3 * airmass * mask)/np.sum(airmass*mask))
print str(oh_trop)+" molec cm-3 tropospheric OH"

oh_zm    = np.mean  (oh_cm3, axis=2)
zero     = np.zeros (oh_zm.shape)
mass_zm  = np.mean  (airmass, axis=2)
pres     = np.mean  (P, axis=2)/100.0 # convert to hPa
#**********************************************************
# AVERAGE OH INTO THE BOXES
(databox, massbox, zerobox) = l_oh.boxes(pres,oh_zm,mass_zm,zero,lat,hb,lb)
# databox: OH values that fall into the individual boxes
# massbox: Airmass of those gridboxes that fall into the individual boxes
# zerobox: Boxes that have the same shape as the data boxes;
# zerobox: will contain the product of the airmass and OH

# Calculate mean OH (and sd) for each box
ohbox = np.empty(len(hb)*(len(lb)-1), dtype=np.float64)
sdbox = np.empty(len(hb)*(len(lb)-1), dtype=np.float64)

for i in range(len(hb)*(len(lb)-1)):
    zerobox[i]  = databox[i]*massbox[i]

for i in range(len(hb)*(len(lb)-1)):
    ohbox[i] = "%.2f" %np.divide (np.mean(zerobox[i]),np.mean(massbox[i])*1E-6) # air mass weighted OH in each box
    sdbox[i] = "%.2f" %np.std    (        databox[i])

#**********************************************************
# Spivakovsky [OH]GM(M) *Lawrence et al 2001, ACP
spbox=[
  0.47  #  1
, 0.72  #  2
, 0.64  #  3
, 1.44  #  4
, 2.00  #  5
, 1.43  #  6
, 1.52  #  7
, 1.99  #  8
, 1.36  #  9
, 0.76  # 10
, 0.88  # 11
, 0.64  # 12
]
#**********************************************************
# Offsets for the text boxes on the plot 
offset = [
[0.22, 0.27]
,[0.22, 0.52]
,[0.22, 0.77]
,[0.42, 0.27]
,[0.42, 0.52]
,[0.42, 0.77]
,[0.55, 0.27]
,[0.55, 0.52]
,[0.55, 0.77]
,[0.74, 0.27]
,[0.74, 0.52]
,[0.74, 0.77]
]
#**********************************************************
# Plot the results
plt.figure      (figsize=(15, 10))
plt.subplot     (1,1,1, axisbg= 'white')
plt.xticks      (np.array([0,2,3,4,6]),('90S','30S','0','30N','90N'))
plt.yticks      (np.array([-0.15,0,1,2,3,3.15])\
                ,('','1000','750','500','250',''))
plt.tick_params (axis='both', which='major', labelsize = 20, pad=10)
plt.grid        (b=True, which='major',axis = 'both'\
                , color='k', linestyle='--')
plt.xlabel      ('Latitude',fontsize=30)
plt.ylabel      ('Pressure (hPa)',fontsize=30)
plt.title       (jobd+' Mass Weighted [OH]\n',fontsize=30)
plt.figtext     (0.13, 0.915\
                , r'($10^6\ molec\ cm^{-3}$)'\
                , backgroundcolor='white',fontsize=18)
plt.figtext     (0.7, 0.0250\
		, r'$\bar{[OH]}$ = '+oh_trop+' $molec\ cm^{-3}$'\
                , backgroundcolor='white',fontsize=18)
plt.figtext     (0.75, 0.915\
                , 'Spivakovsky'\
                , color='red', backgroundcolor='white',fontsize=18)

# add the mean OH
for i in range(len(hb)*(len(lb)-1)):
  plt.figtext   (offset[i][0], offset[i][1]+0.03\
                ,ohbox[i]\
                ,color='black', backgroundcolor='white',fontsize=30)
  plt.figtext   (offset[i][0]+0.005, offset[i][1]-0.05\
                ,spbox[i]\
                ,color = 'red', backgroundcolor='white',fontsize=24)
  plt.figtext   (offset[i][0]-0.02, offset[i][1]-0.11\
                ,'('+u'\u00B1'+' '+str(sdbox[i])+')'\
                ,color = 'black', backgroundcolor='white',fontsize=24)

plt.savefig('/homes/ih280/Analysis/fixedOH/plots/'+jobid+'_lawrence.pdf')
print "Saving "+jobid+"_lawrence"
plt.show()

