''' 
EDGAR vn4.2
Codes and naming conventions
'''
#################################################################### 
def edgar(v):
    if   v == 'animals':
        index = ['4A']
    elif v == 'rice':
        index = ['4C_4D']
    elif v == 'coal':
        index = ['1B1']
    elif v == 'gas':
        index = ['1B2a','1B2b']
    elif v == 'landfills':
        index = ['6A_6C']
    elif v == 'sewage':
        index = ['6B']
#    elif v == 'manure':
#        index = ['4B']
#    elif v == 'residential':
#        index = ['1A4']
    elif v == 'otheranth':
        index = ['1A1_1A2','2','1A3b','1A3a_c_d_e','4B','1A4']
    elif v == 'bioburn':
        index = ['4F','7A','5A_C_D_F_4E']
    return index


