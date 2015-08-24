#-------------BEGIN HEADERS-------------
from netCDF4 import Dataset as NetCDFFile
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from mpl_toolkits.basemap import Basemap, addcyclic, cm
from scipy.ndimage.filters import minimum_filter, maximum_filter
from netCDF4 import Dataset
from scipy import interpolate
import pylab as P
import sys
#-------------END HEADERS-------------

#----------------------------------BEGIN FUNCTIONS----------------------------------
#-----------------BEGIN FUNCTION 1-----------------
def maindataread():
    data_hold = []

    for i in range((end_year-start_year)*4):
        data_hold.append(np.mean(data.variables[variable_type][i,68:76,101:128]))

    data_hold_clean = np.array(data_hold)
    del(data_hold)

    return data_hold_clean
#-----------------END FUNCTION 1-----------------


#-----------------BEGIN FUNCTION 2-----------------
def myavg():
    temp_avg = []

    for i in range(0,4):
        temp_avg.append(np.mean(prmsl_abs[i::4]))

    return temp_avg
#-----------------END FUNCTION 2-----------------


#-----------------BEGIN FUNCTION 3-----------------
def myprocess():
    data_vector = []
    counter_el = 0
    counter_la = 0
    counter_ne = 0
    count_m = 0 #0 DJF, 1 MAM, 2 JJA, 3 SON
    count_y = 1980

    for i in range(len(prmsl_abs)/4):
        for j in range(len(temp_avg)):
            if (prmsl_abs[4*i+j] - temp_avg[j]) > thereshold:
                data_vector.append(1)
                data_vector.append(prmsl_abs[4*i+j] - temp_avg[j])
                data_vector.append(count_y)
                data_vector.append(count_m)

                counter_el += 1
            elif (prmsl_abs[4*i+j] - temp_avg[j]) < - thereshold:
                data_vector.append(-1)
                data_vector.append(prmsl_abs[4*i+j] - temp_avg[j])
                data_vector.append(count_y)
                data_vector.append(count_m)
                counter_la += 1
            elif abs(prmsl_abs[4*i+j] - temp_avg[j]) < thereshold:
                data_vector.append(0)
                data_vector.append(prmsl_abs[4*i+j] - temp_avg[j])
                data_vector.append(count_y)
                data_vector.append(count_m)
                counter_ne += 1
            else:
                print('Error, fourth condition')
                exit()
            count_m += 1
            if count_m == 4:
                count_m = 0
                count_y += 1

    return (data_vector,counter_el,counter_la,counter_ne)
#-----------------END FUNCTION 3-----------------
#----------------------------------END FUNCTIONS----------------------------------




#----------------------------------BEGIN BODY----------------------------------
#-----------------INPUT VARIABLES-----------------
start_year = 1980
end_year = 2005+1
data = (NetCDFFile(sys.argv[1]))
#data = (NetCDFFile('/home/scottyiu/Desktop/work/data/CMIP5_AMIP/SST/bcc-csm1-1/run.nc'))
variable_type = 'ts'
filename = 'aslera.png'
thereshold = 0.5
#-----------------END INPUT VARIABLES-----------------


#-----------------CALLING FUNCTION 1-----------------
prmsl_abs = maindataread();
#-----------------END CALLING FUNCTION 1-----------------


#-----------------CALLING FUNCTION 2-----------------
temp_avg = myavg();
#-----------------END CALLING FUNCTION 2-----------------


#-----------------CALLING FUNCTION 3-----------------
data_vector,counter_el,counter_la,counter_ne = myprocess();
#-----------------END CALLING FUNCTION 3-----------------

#Printing with a loop to look better in .dat file
for i in range(len(data_vector)):
    print(data_vector[i])
