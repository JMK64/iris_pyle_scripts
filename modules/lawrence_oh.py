''' 
Prepare fields for Lawrence plots
- 3D fields for mass weighted OH
- 3D fields for reaction flux OH+CH4

Put data into boxes that correspond to those in Lawrence et al., 2001
'''
#**********************************************************
import netCDF4 as ncdf
import numpy as np
import tracer_var_codes as vcode

def lawr(jobid,nyrs):
    ''' 
OH mass weighted
output: 3D field, time average
    '''
    file    = ncdf.Dataset('/scratch/ih280/netscratch/um/'+jobid+'/'+jobid+'_oh.nc')
    oh      = file.variables['OH'][-12*nyrs:]
    oh      = np.mean(oh,axis=0)
    file.close()
    file    = ncdf.Dataset('/scratch/ih280/netscratch/um/'+jobid+'/'+jobid+'_P-theta.nc')
    P       = file.variables['p'][-12*nyrs:]
    P       = np.mean(P,axis=0)
    file.close()
    file    = ncdf.Dataset('/scratch/ih280/netscratch/um/'+jobid+'/'+jobid+'_airmass.nc')
    airmass = file.variables['airmass_atm'][-12*nyrs:]
    airmass = np.mean(airmass,axis=0)
    return (oh,P,airmass)

def boxes(pres, data_zm, mass_zm, zero, lat, hb, lb):
    ''' 
Distribute data into boxes
creates a mean box value for data, airmass and a zero variable
    '''
    # pbox: list of 12 lists for the 12 atm boxes
    # nb of vert boxes * nb of horiz boxes
    # The first step will result in a nested array which then has to be flattened.
    pbox1    = []
    pbox2    = []
    pbox3    = []
    # boxes: list of 12 lists for the 12 atm boxes
    # nb of vert boxes * nb of horiz boxes
    # Will contain flattened data from pbox1
    databox  = pbox1[:]
    massbox  = pbox2[:]
    zerobox  = pbox3[:]
    for i in range(len(hb)*(len(lb)-1)):
      pbox1.append([])
      pbox2.append([])
      pbox3.append([])
      databox.append([])
      massbox.append([])
      zerobox.append([])
    # Devide atmosphere into vertical boxes, spanning all latitudes
    # z contains indicies as a function of latitude for all pressure levels:
    # | z[2] | hb[1] > P >= hb[2]
    # | z[1] | hb[0] > P >= hb[1]
    # | z[0] |         P >= hb[0]
    z        = [[],[],[]]
    for i in range(len(lat)):
      z[0].append (np.where(  pres[:,i]>=hb[0] )                     [0])
      z[1].append (np.where(( pres[:,i]>=hb[1] ) & (pres[:,i]<hb[0]))[0])
      z[2].append (np.where(( pres[:,i]>=hb[2] ) & (pres[:,i]<hb[1]))[0])
    # Put data into the boxes. 
    # This will result in a nested array, that then has to be flattened.
    # Use indices of z for the height boundaries.
    # Create latitude boundaries in loop.
    for i in range(len(lb)-1):              # number of lat boxes
      latlow  = np.where (lat >= lb[i]   )[0][ 0]
      lathigh = np.where (lat <  lb[i+1] )[0][-1]
      for l in range(latlow,lathigh+1):   # lat slice
        for h in range(len(hb)):        # number of vertical boxes
            pbox1[i*3+h].append (list( data_zm [z[h][l], l] ))
            pbox2[i*3+h].append (list( mass_zm [z[h][l], l] ))
            pbox3[i*3+h].append (list( zero    [z[h][l], l] ))
    # Flatten lists in pbox1
    for i in range(len(hb)*(len(lb)-1)):
      a=[]
      b=[]
      c=[]
      for k in pbox1[i]:
        for l in k:
            a.append(l)
      for k in pbox2[i]:
        for l in k:
            b.append(l)
      for k in pbox3[i]:
        for l in k:
            c.append(l)
      databox [i] = np.array( a[:] ) # OH
      massbox [i] = np.array( b[:] ) # Mass
      zerobox [i] = np.array( c[:] ) # Zeros
    del a, b, c, pbox1, pbox2, pbox3
    return (databox, massbox, zerobox)
