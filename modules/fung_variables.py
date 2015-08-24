''' 
Fung 1991
Variable names
'''
#################################################################### 
# 'animals', 'hydrates_76-84N', 'hydrates_SovietArctic', 'rice', 'soil-loss', 'termites', 'wetlands'
def fung(v):
    if   v == 'animals':
        var = 'CH4ANIMLS'
    elif v == 'hydrates_76-84N':
        var = 'CH4HYDZ'
    elif v == 'hydrates_SovietArctic':
        var = 'CH4HYDV'
    elif v == 'rice':
        var = 'CH4RICEC'
    elif v == 'soil-loss':
        var = 'CH4SOILABS'
    elif v == 'termites':
        var = 'CH4TRMITE'
    elif v == 'wetlands':
        var = 'CH4WETL'
    elif v == 'bogs':
        var = 'CH4BOGS'
    elif v == 'swamps':
        var = 'CH4SWAMPS'
    elif v == 'tundra':
        var = 'CH4TUNDRA'
    return var

def fung_transcom(v):
    if   v == 'bogs':
        var = 'CH4BOGS'
    elif v == 'swamps':
        var = 'CH4SWAMPS'
    elif v == 'tundra':
        var = 'CH4TUNDRA'
    return var

