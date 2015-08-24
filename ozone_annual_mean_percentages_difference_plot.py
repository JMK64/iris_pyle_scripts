import numpy.ma as ma
import numpy as np
import netCDF4
import scipy
import scipy.stats
import pylab
#from pylab import *
#import ImageDraw
import ukca_peer
import colors_peer
import matplotlib as mpl
import matplotlib
import matplotlib.pyplot as plt
import calendar
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib import rcParams
import math
import sys, getopt
import iris
import iris.plot as iplt
import iris.quickplot as qplt
import iris.analysis.cartography
plt.close("all")
# plt.clf()
# #plt.rcParams['text.usetex'] = True
# plt.rc('font', family='sans-serif', serif='cm10')#,weight='bold')
# sys.stdout.flush()
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.serif'] = ['Helvetica']
# matplotlib.rcParams['eps.fonttype'] = 'truetype'

substance = 'O3'
# script assumes zonal mean data (indexing last dimension by null) -> to change if other data is used
pic=substance+'_D_min_A_amean_perc_75yrs_paper2'
#units=r'Years'
lev_min=0
lev_max=60
nr_levs = lev_max-lev_min
nr_lat = 73
nr_lon = 1 
nr_years = 50
#s to years
t_yr_ins=60*60*24*360
#colormap
cmap = colors_peer.colors_peer('grads')
#path_control = '/group_workspaces/jasmin2/ukca/pjnowack/data/xihzn/monthly_data/pe_data/'
path_A = '/group_workspaces/jasmin2/ukca/pjnowack/data/joined_xihzn_xizgv/monthly_data/pe_data/pe_data/'
# path_D = '/group_workspaces/jasmin2/ukca/pjnowack/data/xikva/monthly_data/pe_data/'
path_D = '/group_workspaces/jasmin2/ukca/pjnowack/data/xikvl_xikvo/monthly_data/pe_data/'
fname_A = 'chem_diags_xihzn_xizgv_1to49_zm.nc'
# fname_D = 'chemistry_xikva_ext_yrs_25_214.nc'
fname_D = 'chemistry_xikvl_xikvo.nc'
path_A_th = '/group_workspaces/jasmin2/ukca/pjnowack/data/joined_xihzn_xizgv/monthly_data/pm_data/'
# path_D_th = '/group_workspaces/jasmin2/ukca/pjnowack/data/xikva/monthly_data/pm_data/all_75_years/'
path_D_th = '/group_workspaces/jasmin2/ukca/pjnowack/data/xikvl_xikvo/monthly_data/pm_data/'

fname_A_th = 'data_pm_xihzn_xizgv_2.nc'
# fname_D_th = 'data_pm_xikva_cont_2.nc'
fname_D_th = 'tropopause_height_xikvoxikvl_last50years_zm.nc'

A=netCDF4.Dataset(path_A+fname_A,'r')
D=netCDF4.Dataset(path_D+fname_D,'r')

A_st = 0
A_end = 600
D_st = 0
D_end = 600
D_st_th = 300
D_end_th = 900
A_th=netCDF4.Dataset(path_A_th+fname_A_th,'r')
D_th=netCDF4.Dataset(path_D_th+fname_D_th,'r')
A_th = np.array(A_th.variables['ht'][A_st:A_end,0,:,:])
D_th = np.array(D_th.variables['ht'][D_st_th:D_end_th,0,:,:])
A_th = np.mean(A_th[:,:,:],axis=2,dtype=np.float64)/1000.0
D_th = np.mean(D_th[:,:,:],axis=2,dtype=np.float64)/1000.0
A_th = np.mean(A_th[:,:],axis=0,dtype=np.float64)
D_th = np.mean(D_th[:,:],axis=0,dtype=np.float64)
print A_th.shape
print D_th.shape
orange='#FFA500'
blue1='#000099'
green1='#006600'
pink1='#FF00FF'
violet='#8000FF'



var_name = 'tracer1'
fac_chem = 1e6/1.657
# units = r'$\Delta$ Ozone mass mixing ratio (%)'
units = r'$\Delta$ ozone mmr (%)'
A = np.array(A.variables[var_name][A_st:A_end,:,:,:])
A = np.mean(A[:,:,:,:],axis=3,dtype=np.float64)
D = np.array(D.variables[var_name][D_st:D_end,:,:,:])
D = np.mean(D[:,:,:,:],axis=3,dtype=np.float64)

A_mean = np.mean(A[:,:,:],axis=0,dtype=np.float64)
D_mean = np.mean(D[:,:,:],axis=0,dtype=np.float64)

diff = D_mean - A_mean
diff_perc = diff*100.0/A_mean

#calculate monthly mean climatologies                                                                                                 
#base/control              
A_am = np.empty((len(A[:,0,0])/12,nr_levs,nr_lat),dtype=np.float64)
D_am = np.empty((len(D[:,0,0])/12,nr_levs,nr_lat),dtype=np.float64)
nr_months = len(A[:,0,0])
i=0
while i<nr_months:
      A_am[i/12,:,:] = np.mean(A[i:i+12,:,:],axis=0,dtype=np.float64)
      D_am[i/12,:,:] = np.mean(D[i:i+12,:,:],axis=0,dtype=np.float64)
      i = i+12

P_test=0.05
T_vals,P_vals=scipy.stats.ttest_ind(A_am[:,:,:],D_am[:,:,:],axis=0)# equal_var=False)
sig_mask = np.ma.masked_array(np.zeros((nr_lat,nr_levs)),mask=False,dtype=np.float64)
zeros = np.zeros((nr_levs,nr_lat))
masked_dummy = np.ma.masked_array(zeros,mask=False,dtype=np.int)
i=0
while i < nr_levs:
   j=0
   while j < nr_lat:
      if P_vals[i,j] > P_test:
         sig_mask.mask[j,i] = True
         masked_dummy.data[i,j] = 1
      j=j+1
   i=i+1

# generate pressure data for y2 axis
# rather complicated - essentially interpolate the hybrid_ht levels to
# the mean pressure column to get the correct heights for the required pressure levels 
# (900-0.01 hPa) and then plot these as ticks, giving the correct labeling
p_master = ukca_peer.UM('/group_workspaces/jasmin2/ukca/pjnowack/data/xihzn/yearly_files/p_at_theta_50yrs_xihzn.nc',variable='p')
p_master = p_master.field['p'][:,:,:,:]
p_tmp1 = np.mean(p_master[:,:,:,:],axis=3,dtype=np.float64)
print p_tmp1.shape,"p_tmp1" 
p_tmp2 = np.mean(p_tmp1[:,:,:],axis=0,dtype=np.float64) 
p_col = np.mean(p_tmp2[:,:],axis=1,dtype=np.float64)/100.0 

# these are the minor ticks

p_ticks=np.array([900,800,700,600,500,400,300,200,100,90,80,70,60,50,40,30,20,10,9,8,7,6,5,4,3,2,1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.09,0.08,0.07,0.06,0.05,0.04,0.03,0.02,0.01],dtype=np.float64)
ht_ticks=np.zeros(p_ticks.shape,dtype=np.float64)
master = netCDF4.Dataset(path_A+fname_A,'r')
lat = np.array(master.variables['latitude'][:])
zlev = np.array(master.variables['hybrid_ht'][:])/1000.0
ht = zlev
i=0
while i < len(p_ticks):
    ptarg=np.log(p_ticks[i],dtype=np.float64)
    j=1
    while j < len(p_col):
        p1=np.log(p_col[j-1],dtype=np.float64)
        p2=np.log(p_col[j],dtype=np.float64)
        if ((p1 > ptarg) and (p2 <= ptarg)):
            pfactor=((ptarg-p1)/(p2-p1))
            ht_ticks[i] = ht[j-1] + (ht[j]-ht[j-1])*pfactor
        j=j+1
    i=i+1

def adjustFigAspect(fig,aspect=1):
    '''
    Adjust the subplot parameters so that the figure has the correct
    aspect ratio.
    '''
    xsize,ysize = fig.get_size_inches()
    minsize = min(xsize,ysize)
    xlim = .4*minsize/xsize
    ylim = .4*minsize/ysize
    if aspect < 1:
        xlim *= aspect
    else:
        ylim /= aspect
    fig.subplots_adjust(left=.5-xlim,
                        right=.5+xlim,
                        bottom=.5-ylim,
                        top=.5+ylim)


bounds = np.linspace(-35,35,29)
levs = bounds
# levs_cont = [0]
# for i in range(1,20):
#      levs_cont.append(0+i)
# print levs_cont

# levs_cont_2 = [0]
# for i in range(1,20):
#      levs_cont_2.append(0+i)
# print levs_cont
levs_cont = np.linspace(-35,35,15)
levs_cont_2 = bounds
cnorm = colors.BoundaryNorm(bounds,cmap.N)
cmap.set_under(color=cmap(0.0),alpha=1.0)
cmap.set_over(color=cmap(1.0),alpha=1.0)
blue1='#000099'
green1='#006600'
orange1='#FF4000'
pink1='#FF00FF'
violet='#8000FF'
#Set up figures
#f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
plt_nr = 0
while plt_nr < 1:
   if plt_nr == 0:
      season = 'DJF'
   if plt_nr == 1:
      season = 'MAM'
   if plt_nr == 2:
      season = 'JJA'
   if plt_nr == 3:
      season = 'SON'
   fig = plt.figure(plt_nr) 
   ax1 = fig.add_subplot(1,1,1)
#Plot DJF=0,MAM=1,JJA=2,SON=3
   adjustFigAspect(fig,aspect=0.8)
   CS1=plt.contourf(lat,zlev,\
                    diff_perc[:,:],\
                    levels=levs,interpolation='nearest',cmap=cmap,norm=cnorm,\
                    boundaries=bounds,extend='both')
   plt.plot(lat,A_th,linestyle='-',color='k',linewidth=3)
   plt.plot(lat,D_th,linestyle='-',color='r',linewidth=3)
#create a colorbar
   CD = plt.colorbar(CS1, shrink=1.0, orientation='horizontal', extend='both',\
   pad=0.1,aspect=30)
   n_levels = 2
   cplot=plt.contourf(lat,zlev,masked_dummy,n_levels,colors='none',hatches=['','\\\\'],extend='both',linewidth=16)#,cmap=cmap,norm=cnorm,extend='both') 
   cplot=plt.contourf(lat,zlev,masked_dummy,n_levels,colors='none',hatches=['','//'],extend='both',linewidth=16)#,cmap=cmap,norm=cnorm,extend='both')         
   CD.set_label(units,fontsize=15)
   # CD.locator = mpl.ticker.FixedLocator([-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5])
   # CD.formatter = mpl.ticker.FixedFormatter([-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5])
   CD.locator = mpl.ticker.FixedLocator(np.arange(-30,40,10))
   CD.formatter = mpl.ticker.FixedFormatter(np.arange(-30,40,10))
   CD.update_ticks()
#plot base run results as contour lines on top 
   CS2=plt.contour(lat,zlev,diff_perc[:,:],\
                   levels=levs_cont_2,colors='k',linewidths=1.0)
   clabels=plt.clabel(CS2,levs_cont,inline=True,fmt='%d',fontsize=12,
                          use_clabeltext=True,rotation='horizontal')
   plt.setp(clabels,rotation=0)

   xticks=np.arange(-90,120,30)
   yticks=np.arange(10,90,10)
   ylabels=str(yticks)
   xlabels = ['90S','60S','30S','EQ','30N','60N','90N']
   # xlabels=[]
   # i=0
   # while i < xticks.shape[0]:
   #    if np.int(xticks[i]) < 0:
   #       xlabels.append(str(xticks[i])+'S')
   #    elif np.int(xticks[i]) > 0:
   #       xlabels.append(str(xticks[i])+'N')
   #    else:
   #       xlabels.append('EQ')
   #    i+=1
   ax1.set_ylim([0.5,50])
   y1, y2=ax1.get_ylim()
   x1, x2=ax1.get_xlim()
   ax2=ax1.twinx()
   ax2.set_yticks(ht_ticks,minor=True)
# major ar at 300,100,10,1,0.3
   ax2.set_yticks([ht_ticks[6],ht_ticks[8],ht_ticks[17],ht_ticks[26],ht_ticks[33]],minor=False)
# convert these ticks to strings for the labels
   p_ticks_new=np.array([300,100,10,1.0,0.3])
#ax2.set_yticklabels(p_ticks[8::9].astype('|S10'))
   ax2.set_yticklabels(p_ticks_new.astype('|S10'))
   ax2.set_ylabel('Pressure (hPa)',size=15)
   ax2.set_xlim(x1, x2)
# need to set ylimits *after* setting the ticks, otherwise tick settings over-ride this
   ax2.set_ylim(y1, y2)                 
   plt.xticks(xticks,xlabels)
   plt.xlabel('Latitude',size=12)
   # ax2.set_ylabel(r'Pressure (hPa)'),size=15)
   ax1.set_xlabel(r'Latitude',size=15)
   yticksax=np.array([10,20,30,40,50])
   ylabelsax=str(yticksax)
   ax1.set_yticks(yticksax,ylabelsax)
   ax1.set_ylabel(r'Altitude (km)',size=15)
   # plt.figtext(0.42,0.915,'(D - A)x100/A',color='k',size=15)
   plt.figtext(0.265,0.915,'b',color='k',size=15,fontweight='bold')
   plt.figtext(0.34,0.915,r'4xCO2+SCR', color='r',size=16)
   plt.figtext(0.514,0.912,r'-', color='k',size=28)
   plt.figtext(0.535,0.915,r'piControl', color='k',size=16)
   # plt.figtext(0.30, 0.915, r'D', color=blue1,size=16)
   # plt.figtext(0.33, 0.915,'minus A:',color='k',size=16)
   # plt.figtext(0.416,0.915,r'$\Delta$', color='k',size=16)
   # plt.figtext(0.46,0.915,r'D', color=blue1,size=19)
   # plt.figtext(0.4925,0.912,r'-', color='k',size=30)
   # plt.figtext(0.5218,0.915,r'C1', color=green1,size=19)
#plt.title(title,fontsize=18)
#   plt.show()
#plt.close(1)
   plt.savefig(pic+'.eps',dpi=1200)
   plt.show()
   print plt_nr,season
   plt_nr = plt_nr+1
   # plt.savefig(pic+'.pdf',dpi=600)
plt.show()
