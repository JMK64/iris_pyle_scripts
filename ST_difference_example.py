import netCDF4
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt
import calendar
import matplotlib.cm as cm
import matplotlib.colors as clrs
import numpy as np
import ukca_peer
import colors_peer
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid
import sys, getopt
import scipy.stats
plt.close("all")
plt.clf()
plt.rc('font', family='sans-serif', serif='cm10')#,weight='bold')
sys.stdout.flush()
plot_name = 'ST_seasonal_diff_G1_chem_min_nochem_dotted'
path1 = '/group_workspaces/jasmin2/ukca/pjnowack/data/xjcgc/seasonal_data/ps_data/'
path2 = '/group_workspaces/jasmin2/ukca/pjnowack/data/xikvl_xikvo/seasonal_data/aps/'
# path1 = '/group_workspaces/jasmin2/ukca/pjnowack/data/xjcga/seasonal_data/ps_data/'
# path2 = '/group_workspaces/jasmin2/ukca/pjnowack/data/xikva/monthly_data/ps_data/'
# path1 = '/group_workspaces/jasmin2/ukca/pjnowack/data/joined_xihzn_xizgv/monthly_data/ps_data/'
# path2 = '/group_workspaces/jasmin2/ukca/pjnowack/data/xikvl_xikvo/seasonal_data/aps/'
# fname1 = 'data_ps_xihzn_xizgv_2.nc'
# fname2 = 'data_ps_xikvl_xikvo_2.nc'
# fname1 = 'data_ps_xjcga_2.nc'
# fname2 = 'data_ps_xikva_2.nc'
fname1 = 'data_ps_xjcgc_2.nc'
fname2 = 'data_ps_xikvl_xikvo_2.nc'
run1_loc=path1+fname1
run2_loc=path2+fname2
units = r'$\Delta$T (K)'
run1_data=netCDF4.Dataset(run1_loc,'r')
run2_data=netCDF4.Dataset(run2_loc,'r')
lon0=run1_data.variables['longitude'][:]
nt = len(run1_data.variables['t'][:])
lat=run2_data.variables['latitude'][:]
nr_lat = len(lat)
nr_lon = len(lon0)
run1_master=run1_data.variables['temp'][:,0,:,:]
run2_master=run2_data.variables['temp'][:,0,:,:]
#shape:(time,lat,lon)

# calc mean for each season
run1_mean = np.empty((4,nr_lat,nr_lon))
run2_mean = np.empty((4,nr_lat,nr_lon))
run1_std = np.empty((4,nr_lat,nr_lon))
run2_std = np.empty((4,nr_lat,nr_lon))
i=0
while i < 4:
   run1_mean[i,:,:]=np.mean(run1_master[i:nt:4,:,:],axis=0,dtype=np.float64)
   run2_mean[i,:,:]=np.mean(run2_master[i:nt:4,:,:],axis=0,dtype=np.float64)
   run1_std[i,:,:]=np.std(run1_master[i:nt:4,:,:],axis=0,dtype=np.float64)
   run2_std[i,:,:]=np.std(run2_master[i:nt:4,:,:],axis=0,dtype=np.float64)
   i = i+1
diff_mean=run2_mean-run1_mean
#############################
###STATS
#############################
masked_mean=np.ma.masked_array(diff_mean, mask=False, dtype=np.float64)
zeros = np.zeros(diff_mean.shape)
masked_dummy = np.ma.masked_array(zeros,mask=False,dtype=np.int)

#for t-test:
P_test=0.05
k=0
while k < 4:
    T_vals,P_vals=scipy.stats.ttest_ind(run1_master[k:nt:4,:,:],run2_master[k:nt:4,:,:],axis=0,equal_var=False)   
    i=0
    print P_vals.shape
    while i < len(lat):
       j=0
       while j < len(lon0):
          if P_vals[i,j] > P_test:
             masked_mean.mask[k,i,j] = True
             masked_dummy.data[k,i,j] = 1
          j = j+1
       i = i+1
    k = k+1
######################################
######################################
######################################

plot_nr = 0
while plot_nr < 4:
   if plot_nr==0:
      season = 'DJF'
   if plot_nr==1:
      season = 'MAM'
   if plot_nr==2:
      season = 'JJA'
   if plot_nr==3:
      season = 'SON'
   # make cyclic for plotting
   lat=run2_data.variables['latitude'][:]
   diff,lon = addcyclic(diff_mean[plot_nr,:,:],lon0)
   diff,lon = shiftgrid(180.,diff,lon,start=False)
   masked,lon = addcyclic(masked_mean[plot_nr,:,:],lon0)
   masked,lon = shiftgrid(180.,masked,lon,start=False)
   masked_dum,lon = addcyclic(masked_dummy[plot_nr,:,:],lon0)
   masked_dum,lon = shiftgrid(180.,masked_dum,lon,start=False)
   # set up grid for plotting
   lon, lat = np.meshgrid(lon, lat)
   # cmap = cm.bwr_r
   cmap = colors_peer.colors_peer('grads')
   cnorm=clrs.Normalize(cmap,clip=False)
   # cmap.set_under(color=cmap(0.0),alpha=1.0)
   # cmap.set_over(color=cmap(1.0),alpha=1.0)
   # fig = plt.figure()
   # ax1 = fig.add_subplot(1,1,1)
   map = Basemap(projection='cyl',lon_0=0)
   x, y = map(lon,lat)
   print x.shape,y.shape
   clevs = np.linspace(-3.0,3.0,61)
   #cblevs = np.arange(-15,15+1,5)
   #cblevs = [-3.,-2.5,-2.,-1.5,-1,-0.5,0.5,1.,1.5,2.,2.5,3.] #np.linspace(-3,3,7)
   #cblevs = np.linspace(-3,3,7)
   cblevs = clevs
   cplot0=map.contourf(x,y,diff[:,:],clevs,cmap=cmap,cnorm=cnorm,boundaries=np.arange(-20,25,5),extend='both')
   n_levels = 2
   cplot=map.contourf(x,y,masked_dum[:,:],n_levels,colors='none',hatches=['','....'],extend='both')#,cmap=cmap,norm=cnorm,extend='both')
   # cplot=map.contourf(x,y,masked_dum[:,:],n_levels,colors='none',hatches=['','//'],extend='both')#,cmap=cmap,norm=cnorm,extend='both')
   # plot coastlines, draw label meridians and parallels.
   map.drawcoastlines()
   map.drawcountries()
   #map.drawstates()
   # map.drawparallels(np.arange(-90,120,30),labels=[1,0,0,0],linewidth=0,color='k')
   # map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1],linewidth=0,color='k')
   # fill continents 'coral' (with zorder=0), color wet areas 'aqua'
   map.drawmapboundary()
   cbar=map.colorbar(cplot0,location="bottom", size="5%", pad='15%', ticks=cblevs,extend='both')
   cbar.set_label(units,fontsize=14)
   #cbar.locator = mpl.ticker.FixedLocator(np.arange(-15,20,5))
   cbar.locator = mpl.ticker.FixedLocator(np.arange(-3,4,1))
   #cbar.formatter = mpl.ticker.FixedFormatter(np.arange(-15,20,5))
   cbar.formatter = mpl.ticker.FixedFormatter(np.arange(-3,4,1))
   cbar.update_ticks()  
   # xticks=np.arange(-90,120,30)
   plt.figtext(0.47,0.23,r'Latitude',color='k',size=14)
   #plt.title('')
   plt.figtext(0.28,0.815,r'$\Delta$ Chemistry (3D)',color='k',size=16)
   plt.figtext(0.53,0.815,r'4xCO2+SCR',color='r',size=16)
   plt.figtext(0.71,0.815,season,color='k',size=16)
   plt.xticks([-180,-120,-60,0,60,120,180],['180','120W','60W','0','60E','120E','180'])
   plt.yticks([-88,-60,-30,0,30,60,88],['90S','60S','30S','EQ','30N','60N','90N'])
   plt.figtext(0.05,0.61,r'Longitude',color='k',size=16,rotation='vertical')
   plt.savefig(plot_name+'_'+season+'.png')
   plt.show()
   plot_nr = plot_nr + 1

exit()
