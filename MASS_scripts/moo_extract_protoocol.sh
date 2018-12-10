# best practice

JOBID=u-bc097
# on JASMIN group_workspace/${USER}
# consider also doing this on the /work/scratch directory see
# https://help.jasmin.ac.uk/article/112-how-to-allocate-resources
# for why this may be advantageous
DISK=/group_workspaces/jasmin2/ukca/vol2/${USER}/

mkdir -p ${DISK}/${JOBID}
cd ${DISK}/${JOBID}

# make a directory for the pp_files to be extracted (probably can delete these after a while)
mkdir pp_files
# make a directory for the netcdf (these you'll likely concatenate)
mkdir netcdf

cd pp_files

##
# COPY THE BIT BELOW INTO ITS OWN FILE (called below stash_request.dat) into pp_files directory
## 

##### BEGIN SCRIPT ###############################
# UNCOMMENT LINES BELOW
# begin
#  # extracted species
#  # check STASHMASTER file of job for these
#  # NB extract fails silently - if STASH is not in archived PP file on MASS, it won't throw an error
#  stash=(2,3,4,10,12,39,49,408,16004,30201,30202)
#  # extracted years 
#  # if using single year, drop [] brackets
#  year=[2005..2015]
# end
# UNCOMMENT LINES ABOVE
##### END SCRIPT #################################

# and call it with

moo select stash_request.dat moose:crum/${JOBID}/apm.pp/ ./