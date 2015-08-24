''' Convert input variable names into the exact name given in UKCA
'''
#################################################################### 

def codes(v):
    if   v == 'T':
        var = 'air_temperature'
    elif v == 'P':
        var = 'air_pressure'
    elif v == 'Age':
        var = 'age_of_air'
    elif v == 'Hum':
        var = 'specific_humidity'
    elif v == 'P tropopause':
        var = 'tropopause_pressure'
    elif v == 'T tropopause':
        var = 'tropopause_temperature'
    elif v == 'Hgt tropopause':
        var = 'tropopause_height'
    elif v == 'O3':
        var = 'tracer1'
    elif v == 'NO':
        var = 'tracer2'
    elif v == 'NO3':
        var = 'tracer3'
    elif v == 'CH4':
        var = 'tracer9'
    elif v == 'CO':
        var = 'tracer10'
    elif v == 'Cl':
        var = 'field541'
    elif v == 'ClO':
        var = 'field542'
    elif v == 'Cl2O2':
        var = 'field543'
    elif v == 'N2O':
        var = 'field549'
    elif v == 'OH':
        var = 'field581'
    elif v == 'OH+CH4':
        var = 'ch4_oh_rxn_flux'
    elif v == 'CH4 influx':
        var = 'ch4_apparent_ems'
    elif v == 'CH4 ems':
        var = 'ch4_ems'
    elif v == 'field531':
        var = 'NOx surf emissions'
    elif v == 'field532':
        var = 'CH4 surf emissions'
    elif v == 'field533':
        var = 'CO surf emissions'
    elif v == 'field534':
        var = 'HCHO surf emissions'
    elif v == 'field535':
        var = 'C2H6 surf emissions'
    elif v == 'field536':
        var = 'C3H8 surf emissions'
    elif v == 'field537':
        var = 'Me2CO surf emissions'
    elif v == 'field538':
        var = 'MeCHO surf emissions'
    elif v == 'field539':
        var = 'C5H8 surf emissions'
    elif v == 'field540':
        var = 'BC fossil fuel surf emissions'
    elif v == 'field541':
        var = 'BC biofuel surf emissions'
    elif v == 'field542':
        var = 'OC fossil fuel surf emissions'
    elif v == 'field543':
        var = 'OC biofuel surf emissions'
    elif v == 'field544':
        var = 'Monoterpene surf emissions'
    elif v == 'field545':
        var = 'NVOC surf emissions'
    elif v == 'field546':
        var = 'CH4 anth surf emissions'
    elif v == 'field547':
        var = 'CH4 wetl surf emissions'
    elif v == 'field548':
        var = 'CH4 term surf emissions'
    elif v == 'field549':
        var = 'CH4 hydr surf emissions'
    elif v == 'field550':
        var = 'CH4 soil loss surf emissions'
    return var
