''' 

'''
#################################################################### 
#cspecies=M(var)/M(air)=M(var)/28.97g.mol-1

def cspec(v):
    if   v == 'T':
        cspecies=1
    elif v == 'P':
        cspecies=1
    elif v == 'Age':
        cspecies=1
    elif v == 'Hum':
        cspecies=0.621
    elif v == 'P tropopause':
        cspecies=1
    elif v == 'T tropopause':
        cspecies=1
    elif v == 'Hgt tropopause':
        cspecies=1
    elif v == 'O3':
        cspecies=1.657
    elif v == 'NO':
        cspecies=1.036
    elif v == 'NO3':
        cspecies=2.14
    elif v == 'CH4':
        cspecies=0.552
    elif v == 'CO':
        cspecies=0.967
    elif v == 'Cl':
        cspecies=1.225
    elif v == 'ClO':
        cspecies=1.778
    elif v == 'Cl2O2':
        cspecies=3.555
    elif v == 'N2O':
        cspecies=1.519
    elif v == 'OH':
        cspecies=0.587
    elif v == 'OH+CH4':
        cspecies=1
    elif v == 'CH4 influx':
        cspecies=1
    elif v == 'CH4 ems':
        cspecies=1
    return cspecies
