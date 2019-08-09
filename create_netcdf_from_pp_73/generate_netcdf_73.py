#!/usr/local/shared/ubuntu-12.04/x86_64/python2.7/bin/python
#################################################################### 
# Script to write netCDF files from pp files
# UM-UKCA vn 7.3
# 
# Only use for files with more than one timestep:
# Iris does not output a dimension if it contains only one step.
#
# Ines Heimann, May 2015 
#################################################################### 
import iris
import definitions_STASH
import os
#################################################################### 
jobid='xjmxo'

decades = [
#['k',range(0,10)]
#,
['l',range(9,10)]
,
['m',range(0,7)]
]

inputdir='/tacitus/ih280/um/'+jobid+'/'+jobid+'_output/'

outputdir='/tacitus/ih280/um/'+jobid+'/tracers/'
if not os.path.exists(outputdir):
    os.makedirs(outputdir)


#################################################################### 
# Which STASH numbers to take for the netCDF file

# Do not use 00 as section indicator. 00010 = 8 ?!
#################################################################### 
lst=[
	# T on theta levels
['_T-theta',[16004]]
	# P on theta levels
,['_P-theta',[408]]
	# Tropopause Height 
,['_trophgt',[30453]]
	# Air mass whole atmosphere
,['_airmass',[34363]]
	# O3, CH4, N2O, Age of air
,['_o3_ch4_n2o_ageair',[34001,34009,34049,34150]]
	# O3
,['_o3',[34001]]
	# CH4
,['_ch4',[34009]]
	# N2O
,['_n2o',[34049]]
	# OH
,['_oh',[34081]]
	# O1D
,['_o1d',[34151]]
	# CO
,['_co',[34010]]
	# CH4+OH
,['_ch4+oh',[34341]]
	# CH4 surf ems flux*2
,['_ch4_ems',[34451,302]]
	# O3 tendency
,['_o3-tend',[34354]]
	# Ox production
#,['_ox-prod',[34301,34302,34303,34304,34305,34306,34307]]
	# Ox loss
#,['_ox-loss',[34301,34302,34303,34304,34305,34306,34307]]
]

name = []
stash_list = []
for i in lst:
    name.append(i[0])
    stash_list.append(i[1])

#################################################################### 
# loop over decades and years
#################################################################### 
for d in decades:
    for y in d[1]:
        print '\n'+jobid+'\npm'+d[0]+str(y)
        # prepare STASH codes
        path_to_files=inputdir+'*pm'+d[0]+str(y)+'*'
        filepath=iris.sample_data_path(path_to_files)
        for z in range(0,len(stash_list)):
            stash=[]
            field_constr=[]
            for i in stash_list[z]:
                def ret_stash_string(i):
                    isec=i/1000
                    sec="{:02d}".format(isec)
                    it="{:03d}".format(i-(1000*isec))
                    return 'm01s'+sec+'i'+it
                stash.append(ret_stash_string(i))
                field_constr.append(iris.AttributeConstraint(STASH=ret_stash_string(i)))
            print 'stash : '
            print stash
        # load pp files and output netCDF
            outfile=outputdir+jobid+'_pm'+d[0]+str(y)+name[z]+'.nc'
            field=iris.load(filepath,field_constr,callback=definitions_STASH.UKCA_callback)
            print field
            iris.save(field, outfile, netcdf_format="NETCDF3_CLASSIC")


#################################################################### 
# Shell script to merge files
#################################################################### 
import subprocess

subprocess.call(["/bin/bash", "/homes/ih280/scripts/netCDF/merge_netcdf.sh"] + [jobid] + [outputdir] + name)

