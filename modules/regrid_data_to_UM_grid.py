''' 
Python Script to regrid data to the UM grid
output: data_um,lat_um,lon_um

N96L85 resolution
longitude(x): 192 points; Start   0.0; spacing 1.875 degrees
latitude(y) : 145 points; Start -90.0; spacing 1.25 degrees 

Ines Heimann, Feb 2015
'''
#********************************************************************************************************
import numpy as np

def newgrid(lat,lon,data_high):
  print 'REGRIDDING'
  lon_um = np.arange(0,360,1.875)
  lat_um = np.arange(-90.,90.+1,1.25)
  print 'lat (UM):',len(lat_um),'; lon (UM):',len(lon_um)
  data_um = np.zeros([len(lat_um),len(lon_um)],dtype=np.float64)
  for la in range(len(lat_um)-1):
    if lat_um[la+1] == 90:
      data_set = sum(\
	data_high[\
	np.where((lat[:]>=lat_um[la]))[0]\
	])
    else:
      data_set = sum(\
	data_high[\
	np.where((lat[:]>=lat_um[la]) & (lat[:]<lat_um[la+1]))[0]\
	])
    for lo in range(len(lon_um)):
      if lon_um[lo]==358.125:
        sub_set = data_set[\
	np.where(\
	(lon[:]>=lon_um[lo])\
	)[0]\
	]
        data_um[la][lo] = sum(sub_set)
      else:
        sub_set = data_set[\
	np.where(\
	(lon[:]>=lon_um[lo]) & (lon[:]<lon_um[lo+1])\
	)[0]\
	]
        data_um[la][lo] = sum(sub_set)
  del data_set, sub_set
  return data_um,lat_um,lon_um


