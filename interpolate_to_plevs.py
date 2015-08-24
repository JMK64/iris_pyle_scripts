import numpy as np
import netCDF4 as ncdf

#*****************************************************************************************************************
# Module containing functions to interpolate from theta to pressure levels
# ...and pressure to pressure levels
# AB 2015

#*****************************************************************************************************************
""" 
INPUT(S):
vtheta	= variable to interpolate
ptheta  = pressure on theta levels
ptarget = pressures to interpolate onto
lats    = latitudes

OUTPUT(S):
vpres
"""

def interpolate_theta_to_p(vtheta,ptheta,ptarget,lats):
   len_ptarget = len(ptarget)
   len_ptheta  = len(ptheta)
   len_lats    = len(lats)

   # empty array for output
   vpres = np.empty([len_ptarget,len_lats])		

   # log-pressure
   lptheta  = np.log(ptheta)
   lptarget = np.log(ptarget)

   for ilat in range(len_lats):
      for ip in range(len_ptarget):
         for ihgt in range(len_ptheta-1):
            if ptarget[ip]<ptheta[ihgt,ilat] and ptarget[ip]>ptheta[ihgt+1,ilat]:
               vpres[ip,ilat] = vtheta[ihgt,ilat] + \
                                ((lptarget[ip]-lptheta[ihgt,ilat])/(lptheta[ihgt+1,ilat]-lptheta[ihgt,ilat]))*(vtheta[ihgt+1,ilat]-vtheta[ihgt,ilat])

   return vpres

""" 
INPUT(S):
vpres1	= variable to interpolate
pin     = pressures to interpolate from
pout    = pressures to interpolate onto

OUTPUT(S):
vpres2
"""

def interpolate_p_to_p(vpres1,pin,pout,lats):
   len_pin  = len(pin)
   len_pout = len(pout)
   len_lats = len(lats)

   # empty array for output
   vpres2 = np.empty([len_pout,len_lats])		

   # log-pressure
   lpin  = np.log(pin)
   lpout = np.log(pout)

   for ilat in range(len_lats):
      for ip in range(len_pout):
         for ihgt in range(len_pin-1):
            if pout[ip]==pin[ihgt]:
               vpres2[ip,ilat] = vpres1[ihgt,ilat]
               continue
            if pout[ip]<pin[ihgt] and pout[ip]>pin[ihgt+1]:
               vpres2[ip,ilat] = vpres1[ihgt,ilat] + \
                                ((lpout[ip]-lpin[ihgt])/(lpin[ihgt+1]-lpin[ihgt]))*(vpres1[ihgt+1,ilat]-vpres1[ihgt,ilat])

   return vpres2
