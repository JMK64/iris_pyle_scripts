#Sorry for any bad programming, lack of comments. Can send email to yysy2@cam.ac.uk if need clarification.

#comments:
#argv1 = book for el nino sst
#argv2 = path for data
#argv3 = variable name
#argv4 = seasons (0,1,2,3)
#argv5 = plottile
#------------------------------------------------------------
#cp mastercode into folders (i call it eraseasons but it is not for era, just bad naming)
cp mastercode.py era/eraseasons.py
cp mastercode.py bcc-csm1-1/eraseasons.py
cp mastercode.py BNU-ESM/eraseasons.py
cp mastercode.py CanESM2/eraseasons.py
cp mastercode.py CCSM4/eraseasons.py
cp mastercode.py CMCC-CM/eraseasons.py
cp mastercode.py CNRM-CM5/eraseasons.py
cp mastercode.py CSIRO-Mk3-6-0/eraseasons.py
cp mastercode.py FGOALS-g2/eraseasons.py
cp mastercode.py GISS-E2-R/eraseasons.py
#cp mastercode.py HadGEM2-A/eraseasons.py
cp mastercode.py inmcm4/eraseasons.py
cp mastercode.py IPSL-CM5A-LR/eraseasons.py
cp mastercode.py IPSL-CM5A-MR/eraseasons.py
cp mastercode.py MIROC5/eraseasons.py
cp mastercode.py MPI-ESM-LR/eraseasons.py
cp mastercode.py MPI-ESM-MR/eraseasons.py
cp mastercode.py MRI-CGCM3/eraseasons.py
cp mastercode.py NorESM1-M/eraseasons.py

#------------------------------------------------------------
#Below: run for all the CMIP5 models
#the arguments are:
#1) path to sst.dat is where I saved if that season is el nino or not. You have to run code in the sst folder.
#2) path to all_levels.nc is where I saved the nc file in question
#3) the msl is the variable name
#4) choice of seasons: 0 DJF, 1 MAM, 2 JJA, 3 SON
#5) plottitle
#------------------------------------------------------------

#cd era
#nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/era/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/era/all_levels.nc msl 0 djfera.png Era &
#nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/era/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/era/all_levels.nc msl 2 jjaera.png Era &

cd bcc-csm1-1
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/bcc-csm1-1/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/bcc-csm1-1/all_levels.nc psl 0 djfera.png bcc-csm1-1 &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/bcc-csm1-1/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/bcc-csm1-1/all_levels.nc psl 2 jjaera.png bcc-csm1-1 &

cd ../BNU-ESM
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/BNU-ESM/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/BNU-ESM/all_levels.nc psl 0 djfera.png BNU-ESM &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/BNU-ESM/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/BNU-ESM/all_levels.nc psl 2 jjaera.png BNU-ESM &

cd ../CanESM2
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/CanESM2/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/CanESM2/all_levels.nc psl 0 djfera.png CanESM2 &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/CanESM2/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/CanESM2/all_levels.nc psl 2 jjaera.png CanESM2 &

cd ../CCSM4
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/CCSM4/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/CCSM4/all_levels.nc psl 0 djfera.png CCSM4 &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/CCSM4/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/CCSM4/all_levels.nc psl 2 jjaera.png CCSM4 &

cd ../CMCC-CM
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/CMCC-CM/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/CMCC-CM/all_levels.nc psl 0 djfera.png CMCC-CM &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/CMCC-CM/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/CMCC-CM/all_levels.nc psl 2 jjaera.png CMCC-CM &

cd ../CNRM-CM5
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/CNRM-CM5/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/CNRM-CM5/all_levels.nc psl 0 djfera.png CNRM-CM5 &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/CNRM-CM5/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/CNRM-CM5/all_levels.nc psl 2 jjaera.png CNRM-CM5 &

cd ../CSIRO-Mk3-6-0
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/CSIRO-Mk3-6-0/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/CSIRO-Mk3-6-0/all_levels.nc psl 0 djfera.png CSIRO-Mk3-6-0 &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/CSIRO-Mk3-6-0/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/CSIRO-Mk3-6-0/all_levels.nc psl 2 jjaera.png CSIRO-Mk3-6-0 &

cd ../FGOALS-g2
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/FGOALS-g2/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/FGOALS-g2/all_levels.nc psl 0 djfera.png FGOALS-g2 &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/FGOALS-g2/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/FGOALS-g2/all_levels.nc psl 2 jjaera.png FGOALS-g2 &

cd ../GISS-E2-R
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/GISS-E2-R/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/GISS-E2-R/all_levels.nc psl 0 djfera.png GISS-E2-R &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/GISS-E2-R/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/GISS-E2-R/all_levels.nc psl 2 jjaera.png GISS-E2-R &

#cd ../HadGEM2-A
#nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/HadGEM2-A/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/HadGEM2-A/all_levels.nc psl 0 djfera.png HadGEM2-A &
#nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/HadGEM2-A/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/HadGEM2-A/all_levels.nc psl 2 jjaera.png HadGEM2-A &

cd ../inmcm4
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/inmcm4/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/inmcm4/all_levels.nc psl 0 djfera.png inmcm4 &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/inmcm4/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/inmcm4/all_levels.nc psl 2 jjaera.png inmcm4 &

cd ../IPSL-CM5A-LR
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/IPSL-CM5A-LR/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/IPSL-CM5A-LR/all_levels.nc psl 0 djfera.png IPSL-CM5A-LR &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/IPSL-CM5A-LR/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/IPSL-CM5A-LR/all_levels.nc psl 2 jjaera.png IPSL-CM5A-LR &

cd ../IPSL-CM5A-MR
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/IPSL-CM5A-MR/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/IPSL-CM5A-MR/all_levels.nc psl 0 djfera.png IPSL-CM5A-MR &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/IPSL-CM5A-MR/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/IPSL-CM5A-MR/all_levels.nc psl 2 jjaera.png IPSL-CM5A-MR &

cd ../MIROC5
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/MIROC5/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/MIROC5/all_levels.nc psl 0 djfera.png MIROC5 &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/MIROC5/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/MIROC5/all_levels.nc psl 2 jjaera.png MIROC5 &

cd ../MPI-ESM-LR
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/MPI-ESM-LR/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/MPI-ESM-LR/all_levels.nc psl 0 djfera.png MPI-ESM-LR &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/MPI-ESM-LR/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/MPI-ESM-LR/all_levels.nc psl 2 jjaera.png MPI-ESM-LR &

cd ../MPI-ESM-MR
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/MPI-ESM-MR/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/MPI-ESM-MR/all_levels.nc psl 0 djfera.png MPI-ESM-MR &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/MPI-ESM-MR/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/MPI-ESM-MR/all_levels.nc psl 2 jjaera.png MPI-ESM-MR &

cd ../MRI-CGCM3
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/MRI-CGCM3/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/MRI-CGCM3/all_levels.nc psl 0 djfera.png MRI-CGCM3 &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/MRI-CGCM3/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/MRI-CGCM3/all_levels.nc psl 2 jjaera.png MRI-CGCM3 &

cd ../NorESM1-M
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/NorESM1-M/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/NorESM1-M/all_levels.nc psl 0 djfera.png NorESM1-M &
nice -n 19 python2.7 -c 'execfile("eraseasons.py")' /home/users/scottyiu/2015/CMIP5/coupled/surfaceT/NorESM1-M/sst.dat /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/MSLP/NorESM1-M/all_levels.nc psl 2 jjaera.png NorESM1-M &

cd ../

#bcc-csm1-1
#CanESM2
#CMCC-CM
#FGOALS-g2
#HadGEM2-ES
#IPSL-CM5A-LR
#MIROC5
#MPI-ESM-MR
#NorESM1-M
#BNU-ESM
#CCSM4
#CNRM-CM5
#CSIRO-Mk3-6-0
#GISS-E2-R
#inmcm4
#IPSL-CM5A-MR
#MPI-ESM-LR
#MRI-CGCM3
