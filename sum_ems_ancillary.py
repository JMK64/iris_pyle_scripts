#!/usr/bin/python
#******************************************************
# Script to sum emissions from an ancillary file
# Print the sums to the screen
# 12 month of monthly data
# emissions in kg/m2/s

# Ines Heimann. May 2015
#******************************************************

import netCDF4 as ncdf
import calc_budget
import numpy as np
#******************************************************
# File and names
file1   = '/scratch/ih280/ancils/fixedOH_UM_8.4/2D_ancils/AR5_aero_2000_ih3.nc'
ncbase1 = ncdf.Dataset(file1,'r')		
print ncbase1

var1    = []
for i in ncbase1.variables.items():
    var1.append(str(i[0]))

for i in range(4,len(var1)):
    print var[i-4],var1[i],calc_budget.budget_anc(ncbase1, var1[i])[0]

