''' 
Function to calculate surface area per gridbox
Units: m2
S = R^2*(lon2-lon1)*(sin lat2 - sin lat1)
lon in radians, R = 6371 km
'''

import numpy as np

def area_grid(lat,lon):
  Pi           = np.float128(3.141592653589793238462643383279)
  Earth_Radius = np.float128(6371.0*1.0E3)
  lat_bound    = np.float128(89.999999999999999999999999)
  lon          = np.float128(lon)
  lat          = np.float128(lat)
  rlon         = (lon[:]/np.float128(180.0))*Pi
  rlat         = (lat[:]/np.float128(180.0))*Pi
  dlat         = (rlat[1] - rlat[0])/2.0
  dlon         = (rlon[1] - rlon[0])/2.0
#
  area = np.zeros((len(rlat),len(rlon)),np.float128)
  j=0
  while j < len(rlat):
    if (lat[j] >= lat_bound):
        lat1 = rlat[j]
        lat2 = rlat[j] - dlat/2.0
    elif (lat[j] <= -1.0*lat_bound):
        lat1 = rlat[j] + dlat/2.0            
        lat2 = rlat[j] 
    else:
        lat1 = rlat[j] + dlat
        lat2 = rlat[j] - dlat
    i=0
    while i < len(rlon):
        lon1 = rlon[i] - dlon
        lon2 = rlon[i] + dlon
        area[j,i] = (Earth_Radius**2)*(abs(np.sin(lat1)-np.sin(lat2))*abs(lon1-lon2))
        i += 1
    j += 1
  return area

