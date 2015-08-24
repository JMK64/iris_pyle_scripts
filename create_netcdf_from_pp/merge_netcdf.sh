#!/bin/bash
#################################################################### 
# Script called from within generate_netcdf.py 
# Merges the individual outputfiles.
# Ines Heimann, May 2015
#################################################################### 

jobid=$1
echo $jobid

dir=$2
echo $dir

name=${@:3}
for i in ${name}; do
    echo $i
    ncrcat $dir$jobid*$i'.nc' $dir$jobid$i'.nc'
    mv $dir$jobid$i'.nc' '/tacitus/ih280/um/'$jobid'/'
done

