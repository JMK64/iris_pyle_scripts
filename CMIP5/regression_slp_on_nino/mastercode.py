#-----------------BEGIN HEADERS-----------------
from netCDF4 import Dataset as NetCDFFile
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from mpl_toolkits.basemap import Basemap, addcyclic, cm
from scipy.ndimage.filters import minimum_filter, maximum_filter
from netCDF4 import Dataset
from scipy.stats.stats import pearsonr
from scipy import stats
import sys
#-----------------END HEADERS-----------------




#----------------------------------BEGIN FUNCTIONS----------------------------------
#-----------------BEGIN FUNCTION 1-----------------
def ONIinput():
    ONI = []
    ONIclean = []

    data_y_string = list(book)
    for i in range(len(data_y_string)):
        ONI.append(float(data_y_string[i]))

    for i in range(len(ONI)/4):
        if ONI[4*i+3] == seasons:
            ONIclean.append(ONI[4*i+1])

    return (ONI, ONIclean)
#-----------------END FUNCTION 1-----------------


#-----------------BEGIN FUNCTION 2-----------------
def maindataread():
    data_hold = []

    for i in range((end_year-start_year)*4/4):
        data_hold.append(data.variables[variable_type][4*i+seasons,:,:])

    clean_data = np.array(data_hold)
    del(data_hold)

    return clean_data
#-----------------END FUNCTION 2-----------------


#-----------------BEGIN FUNCTION 3-----------------
def corr():
    lenlat = len(data.variables['latitude'])
    lenlong = len(data.variables['longitude'])

    correlated_data_gradient = [[0 for x in xrange(lenlong)] for x in xrange(lenlat)]
    correlated_data_intercept = [[0 for x in xrange(lenlong)] for x in xrange(lenlat)]
    #correlated_data_r_value = [[0 for x in xrange(lenlong)] for x in xrange(lenlat)]
    #correlated_data_p_value = [[0 for x in xrange(lenlong)] for x in xrange(lenlat)]
    #correlated_data_std_err = [[0 for x in xrange(lenlong)] for x in xrange(lenlat)]

    for j in range(0,lenlat):
    	for k in range(0,lenlong):
            gradient, intercept, r_value, p_value, std_err = stats.linregress(ONIclean, clean_data[:,j,k])
            correlated_data_gradient[j][k] = gradient
	    correlated_data_intercept[j][k] = intercept
	    #correlated_data_r_value[j][k] = r_value
	    #correlated_data_p_value[j][k] = p_value
	    #correlated_data_std_err[j][k] = std_err

    #correlated_clean = np.array()
    clean_data_gradient = np.array(correlated_data_gradient)*0.01
    clean_data_intercept = np.array(correlated_data_intercept)*0.01
    #clean_data_r_value = np.array(correlated_data_r_value)
    #clean_data_p_value = np.array(correlated_data_p_value)
    #clean_data_std_err = np.array(correlated_data_std_err)
    del(correlated_data_gradient)
    del(correlated_data_intercept)
    #del(correlated_data_r_value)
    #del(correlated_data_p_value)
    #del(correlated_data_std_err)

    return (clean_data_gradient, clean_data_intercept) #, clean_data_r_value, clean_data_p_value, clean_data_std_err) 
    #return clean_data_r_value
#-----------------END FUNCTION 3-----------------


#-----------------BEGIN FUNCTION 4-----------------
#HIGHLIGHTING ASL AND NINO3.4 REGION
def highlight():
    for i in range(len(correlated_clean)):
        for j in range(len(correlated_clean[0])):
            correlated_clean[i,j] = 0

    nino_highlight = correlated_clean[:]
    ASL_highlight = correlated_clean[:]

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
book = open(sys.argv[1], 'r')
start_year = 1980
end_year = 2005+1
data = (NetCDFFile(sys.argv[2]))
variable_type = sys.argv[3]
seasons = int(sys.argv[4])
plottitle = sys.argv[6] 
filename = sys.argv[5]
cbarunits = 'hPa/K'
blat = -20
#-----------------END INPUT VARIABLES-----------------


#-----------------CALLING FUNCTION 1-----------------
ONI, ONIclean = ONIinput();
#-----------------END CALLING FUNCTION 1-----------------


#-----------------CALLING FUNCTION 2-----------------
clean_data = maindataread();
#-----------------END CALLING FUNCTION 2-----------------


#-----------------CALLING FUNCTION 3-----------------
clean_data_gradient, clean_data_intercept = corr();
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
clean_data_gradient, lons = addcyclic(clean_data_gradient, lons1)
clean_data_intercept, lons = addcyclic(clean_data_intercept, lons1)

# find x,y of map projection grid.
lons, lats = np.meshgrid(lons, lats)
x, y = m(lons, lats)

# create figure.
fig=plt.figure(figsize=(8,4.5))
ax = fig.add_axes([0.05,0.05,0.9,0.85])
levels = [-4.2, -4.0, -3.8, -3.6, -3.4, -3.2, -3.0, -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0,  -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2]
orig_cmap = plt.cm.coolwarm
cs = m.contourf(x,y,clean_data_gradient,levels,cmap=orig_cmap,extend='both')
#cs = m.contourf(x,y,clean_data_gradient,15)

#amundsen_low = np.max(correlated_clean[600:660,680:1160])
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
#plt.gcf().subplots_adjust(bottom=0.55)
#cd = fig.add_axes([0.05,0.05,0.9,0.85])
cbar = m.colorbar(cs,location="bottom",pad="10%")
cbar.set_label(cbarunits, rotation=0)

plt.title(str(plottitle) + ' SLP regression')# + ' gradient:')# + str(amundsen_low))
plt.savefig(filename)
#plt.show()

# create figure.
fig=plt.figure(figsize=(8,4.5))
ax = fig.add_axes([0.05,0.05,0.9,0.85])
levels = [970, 975, 980, 985, 990, 995, 1000, 1005, 1010, 1015, 1020, 1025, 1030]
orig_cmap = plt.cm.coolwarm
cs = m.contourf(x,y,clean_data_intercept,20,cmap=orig_cmap)
#cs = m.contourf(x,y,clean_data_intercept,15)

m.drawcoastlines(linewidth=1.25)
#m.fillcontinents(color='0.8')
m.drawparallels(np.arange(-80,81,20),labels=[1,1,0,0])
m.drawmeridians(np.arange(0,360,60),labels=[0,0,0,1])

# add colorbar.
cbar = m.colorbar(cs,pad="15%")
cbar.set_label(cbarunits, rotation=0)

plt.title(str(plottitle)  + ' intercept:')# + str(amundsen_low))
plt.savefig(filename + '_intercept.png')
#---------------------------------END BODY----------------------------------
