''' Convert input variable names into the exact name given in UKCA
'''
#################################################################### 

def names(v):
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
    elif v == 'airmass':
        var = 'air_mass_atm'
    elif v == 'O3':
        var = 'mass_fraction_of_ozone_in_air'
    elif v == 'NO':
        var = 'mass_fraction_of_nitrogen_monoxide_in_air'
    elif v == 'NO3':
        var = 'mass_fraction_of_NO3_in_air'
    elif v == 'CH4':
        var = 'mass_fraction_of_methane_in_air'
    elif v == 'CO':
        var = 'mass_fraction_of_carbon_monoxide_in_air'
    elif v == 'Cl':
        var = 'mass_fraction_of_chlorine_in_air'
    elif v == 'ClO':
        var = 'mass_fraction_of_chlorine_monoxide_in_air'
    elif v == 'Cl2O2':
        var = 'mass_fraction_of_dichlorine_peroxide_in_air'
    elif v == 'N2O':
        var = 'mass_fraction_of_nitrous_oxide_in_air'
    elif v == 'OH':
        var = 'mass_fraction_of_hydroxyl_radical_in_air'
    elif v == 'OH+CH4':
        var = 'ch4_oh_rxn_flux'
    elif v == 'CH4 influx':
        var = 'ch4_apparent_ems'
    elif v == 'CH4 ems' or v == 'CH4-ems':
        var = 'ch4_ems'
    return var
