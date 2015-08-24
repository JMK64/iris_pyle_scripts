cp *.py bcc-csm1-1/
cp *.py BNU-ESM/
cp *.py CanESM2/
cp *.py CCSM4/
cp *.py CMCC-CM/
cp *.py CNRM-CM5/
cp *.py CSIRO-Mk3-6-0/
cp *.py FGOALS-g2/
cp *.py GISS-E2-R/
#cp *.py HadGEM2-A/
cp *.py inmcm4/
cp *.py IPSL-CM5A-LR/
cp *.py IPSL-CM5A-MR/
cp *.py MIROC5/
cp *.py MPI-ESM-LR/
cp *.py MPI-ESM-MR/
cp *.py MRI-CGCM3/
cp *.py NorESM1-M

cd era
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/era/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../bcc-csm1-1
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/bcc-csm1-1/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../BNU-ESM
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/BNU-ESM/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../CanESM2
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/CanESM2/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../CCSM4
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/CCSM4/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../CMCC-CM
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/CMCC-CM/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../CNRM-CM5
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/CNRM-CM5/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../CSIRO-Mk3-6-0
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/CSIRO-Mk3-6-0/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../FGOALS-g2
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/FGOALS-g2/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../GISS-E2-R
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/GISS-E2-R/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
#cd ../HadGEM2-A
#python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/HadGEM2-A/all_levels.nc > sst.dat
#python2.7 -c 'execfile("plot.py")'
cd ../inmcm4
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/inmcm4/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../IPSL-CM5A-LR
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/IPSL-CM5A-LR/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../IPSL-CM5A-MR
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/IPSL-CM5A-MR/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../MIROC5
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/MIROC5/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../MPI-ESM-LR
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/MPI-ESM-LR/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../MPI-ESM-MR
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/MPI-ESM-MR/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../MRI-CGCM3
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/MRI-CGCM3/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
cd ../NorESM1-M
python2.7 -c 'execfile("code.py")' /group_workspaces/jasmin2/ukca/scottyiu/CMIP5/coupled/SST/NorESM1-M/all_levels.nc > sst.dat
python2.7 -c 'execfile("plot.py")'
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
