# for Maria 09.09.2019
# going to use IRIS to work with the netCDF file
# this is handy because it can deal with UM pp files
# and netCDF files without changing the code

import iris
import iris.plot
import matplotlib.pyplot as plt # we'll use this to adorn the plots
from matplotlib.colors import BoundaryNorm #optional see final plot
from matplotlib.ticker import MaxNLocator #optional see final plot

# if using IDL save file make sure that
# from scipy.io import readsav
# is included
# see
# https://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.io.readsav.html
# for how to read in an IDL save file into python

#
# load a pp or netCDF file
#
disk = '/Users/ptg21/' # you need to modify this to where your data sit

# load all variables if more than one into a list of data cubes
# if netCDF contains multiple variables this will create several data cubes
# mlso3 = iris.load(disk+'OMI_RAL1.5_ozone_ts.nc')
# take the first cube from the cube list
# mlso3 = mlso3[0]

# if you just want one variable, you would use the load_cube method
# can also just load one level, one time slice etc
# see https://scitools.org.uk/iris/docs/latest/userguide/loading_iris_cubes.html

mlso3 = iris.load_cube(disk+'OMI_RAL1.5_ozone_ts.nc', \
            'Tropospheric O3 (OMI-RAL; surface to 450hPa)')

# if you require info on the cube
print(mlso3)

#
# CALCULATE THE mean
#

# calculate mean tropospheric column over the time series by collapsing
# the cube along a given direction
mlso3_mean = mlso3.collapsed('t', iris.analysis.MEAN)

# plot the mean on a map
# if you need the coords of the cube use
# lat = mlso3_mean.coords('latitude')
# see https://scitools.org.uk/iris/docs/v1.9.0/html/iris/iris/cube.html

#
# PLOT
#

# if required, clear figure for next plotting
plt.clf()

# PLOT 1

# using a color 'mesh' without interpolation
iris.plot.pcolormesh(mlso3_mean, vmin=0, vmax=40.)
# Add coastlines to the map created by contourf.
plt.gca().coastlines()
# add a colorbar - hopefully self-explanatory
plt.colorbar(orientation='horizontal', extend='both')


# PLOT 2 using filled contours
plt.figure(num=2, figsize=(12,6), dpi=200)
iris.plot.contourf(mlso3_mean, levels=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
# Add coastlines to the map created by contourf.
plt.gca().coastlines()
plt.colorbar(orientation='horizontal', shrink=0.5)
# same trick as before
figures_disk = '/Users/ptg21/Desktop/'
plt.savefig(figures_disk+'test_contour.png')

# PLOT 3 using an SVG output format with colormesh and more options set
plt.figure(num=3)
# setting the number of levels in a colormesh is not as easy
levels = MaxNLocator(nbins=15).tick_values(0,40)
cmap = plt.get_cmap('viridis')
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
# now can plot using our custom 'norm' for scaling the  colormesh
iris.plot.pcolormesh(mlso3_mean,cmap=cmap, norm=norm)
plt.gca().coastlines()
plt.colorbar(orientation='horizontal', extend='both', shrink=0.85)
plt.savefig('/Users/ptg21/Desktop/test.svg')

# if you want to see all plots made in the current session
#plt.show()

# I'd advise using an IPython session to run code within
# you would start a session using the incantation
# ipython --pylab
# and then run the code using
# %run for_maria.py
# within ipython
# (luke can advise)
