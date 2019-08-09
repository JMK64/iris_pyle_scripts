

#################################################################### 
# Which STASH numbers to take for the netCDF file

# Do not use 00 as section indicator. 00010 = 8 ?!
#################################################################### 
lst=[
# Adapt for job:
['_no',[34002]]
]

name = []
stash_list = []
for i in lst:
    name.append(i[0])
    stash_list.append(i[1])


