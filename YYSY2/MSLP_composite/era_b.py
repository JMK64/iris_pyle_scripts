#-----------------BEGIN HEADERS-----------------
from netCDF4 import Dataset as NetCDFFile
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from mpl_toolkits.basemap import Basemap, addcyclic, cm
from scipy.ndimage.filters import minimum_filter, maximum_filter
from netCDF4 import Dataset
import time
#-----------------END HEADERS-----------------




#----------------------------------BEGIN FUNCTIONS----------------------------------
#-----------------BEGIN FUNCTION 1-----------------
def ONIinput(ONI):
    data_y_string = list(book)
    for i in range(len(data_y_string)):
    	ONI.append(float(data_y_string[i]))

    return ONI
#-----------------END FUNCTION 1-----------------


#-----------------BEGIN FUNCTION 2-----------------
def maindataread():
    data_hold = []

    for i in range((end_year-start_year)*4):
        data_hold.append(data.variables[variable_type][i,:,:])

    data_hold_clean = np.array(data_hold)
    del(data_hold)

    return data_hold_clean
#-----------------END FUNCTION 2-----------------


#-----------------BEGIN FUNCTION 3-----------------
def writeprmsl():
    prmsl_la_unclean = 0
    prmsl_el_unclean = 0
    prmsl_ne_unclean = 0
    counter_el = 0
    counter_la = 0
    counter_ne = 0

    for i in range(len(ONI)/4):
    	if ONI[4*i] == 1:
            prmsl_el_unclean = data_hold_clean[i] + prmsl_el_unclean
            counter_el += 1
        elif ONI[4*i] == -1:
    	    prmsl_la_unclean = data_hold_clean[i] + prmsl_la_unclean
            counter_la += 1
        elif ONI[4*i] == 0:
    	    prmsl_ne_unclean = data_hold_clean[i] + prmsl_ne_unclean
            counter_ne += 1

    prmsl_el = np.array(prmsl_el_unclean)
    prmsl_la = np.array(prmsl_la_unclean)
    prmsl_ne = np.array(prmsl_ne_unclean)
    del(prmsl_el_unclean)
    del(prmsl_la_unclean)
    del(prmsl_ne_unclean)

    prmsl_el = prmsl_el/(counter_el)
    prmsl_la = prmsl_la/(counter_la)
    prmsl_ne = prmsl_ne/(counter_ne)

    prmsl_el = 0.01*prmsl_el
    prmsl_la = 0.01*prmsl_la
    prmsl_ne = 0.01*prmsl_ne
    prmsl_abs = prmsl_el - prmsl_la

    return (prmsl_abs, counter_el, counter_la, counter_ne)
#-----------------END FUNCTION 3-----------------


#-----------------BEGIN FUNCTION 4-----------------
#HIGHLIGHTING ASL AND NINO3.4 REGION
def highlight():
    for i in range(len(prmsl_abs)):
        for j in range(len(prmsl_abs[0])):
            prmsl_abs[i,j] = 0

    nino_highlight = prmsl_abs[:]
    ASL_highlight = prmsl_abs[:]

    for i in range(600,660):
        for j in range(680,1160):
            ASL_highlight[i,j] = 1000000.0

    for i in range(340,380):
        for j in range(760,960):
            nino_highlight[i,j] = 1000000.0

    return (ASL_highlight, nino_highlight)
#-----------------END FUNCTION 4-----------------
#----------------------------------END FUNCTIONS----------------------------------




#----------------------------------BEGIN BODY----------------------------------
#-----------------INPUT VARIABLES-----------------
book = open('/home/scottyiu/Desktop/work/code/teleconnections_upscale/surfaceT/code/era.dat', 'r')
start_year = 1986
end_year = 2011+1
data = (NetCDFFile('/home/scottyiu/Desktop/work/data/era/MSLP/slp.nc'))
variable_type = 'msl'
plottitle = 'ERA 86-11 MSLP composite: '
filename = 'shera.png'
cbarunits = 'hPa'
blat = 20
#-----------------END INPUT VARIABLES-----------------


#-----------------CALLING FUNCTION 1-----------------
ONI = []
ONIinput(ONI);
#-----------------END CALLING FUNCTION 1-----------------


#-----------------CALLING FUNCTION 2-----------------
data_hold_clean = maindataread();
#-----------------END CALLING FUNCTION 2-----------------


#-----------------CALLING FUNCTION 3-----------------
prmsl_abs, counter_el, counter_la, counter_ne = writeprmsl();
#-----------------END CALLING FUNCTION 3-----------------


#-----------------BEGIN PLOT-----------------
# read lats,lons.
lats = data.variables['latitude'][:]
lons1 = data.variables['longitude'][:]
nlats = len(lats)
nlons = len(lons1)

# create Basemap instance.
m =\
Basemap(projection='spstere',boundinglat=blat,lon_0=165,resolution='l')

# add wrap-around point in longitude.
prmsl_abs, lons = addcyclic(prmsl_abs, lons1)

# find x,y of map projection grid.
lons, lats = np.meshgrid(lons, lats)
x, y = m(lons, lats)

# create figure.
fig=plt.figure(figsize=(8,4.5))
ax = fig.add_axes([0.05,0.05,0.9,0.85])
levels = [-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0.0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
orig_cmap = plt.cm.coolwarm
cs = m.contourf(x,y,prmsl_abs,levels,cmap=orig_cmap)

#amundsen_low = np.max(prmsl_abs[600:660,680:1160])
#-----------------END PLOT-----------------


#-----------------CALLING FUNCTION 4-----------------
#ASL_highlight, nino_highlight = highlight();
#-----------------END CALLING FUNCTION 4-----------------


#-----------------BEGIN HIGHLIGHT-----------------
#m.contour(x,y,ASL_highlight,1,colors='b')
#m.contour(x,y,nino_highlight,1,colors='r')

m.drawcoastlines(linewidth=1.25)
#m.fillcontinents(color='0.8')
m.drawparallels(np.arange(-80,81,20),labels=[1,1,0,0])
m.drawmeridians(np.arange(0,360,60),labels=[0,0,0,1])

# add colorbar.
cbar = m.colorbar(cs,pad="15%")
cbar.set_label(cbarunits, rotation=0)

#plt.title(str(plottitle) + str(amundsen_low) + ', ' + str(counter_el) + ', ' + str(counter_la) + ', ' + str(counter_ne))
plt.savefig(filename)
#plt.show()
#---------------------------------END BODY----------------------------------
