#!/bin/bash

JOBID=u-bc097
# make a location on MASS to put data
# note single-copy should be used unless good reasons

moo mkset -v  --single-copy moose:crum/${JOBID} -p project-ukca

# get contents of the archived climate mean data
moo ls moose:crum/{JOBID}/apm.pp/

# archive specific Files (-f) from monthly mean PP stream
# with VeryVerbose output in UMPP format 
moo put -f -vv -c=umpp {JOBID}a.pml{3,4,5}*  moose:crum/{JOBID}/apm.pp/
