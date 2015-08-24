import netCDF4 as ncdf
import numpy as np

#UNITS
def diagnostic(var):
#    var=word
    if var == 'specific_humidity':
        unit='ppmv'
    elif var == 'mass_fraction_of_hydroxyl_radical_in_air':
#        unit='pptv'
        unit = r'$\mathrm{molecules\ cm^{-3}}$'	# molecules.cm-3
    elif var == 'mass_fraction_of_ozone_in_air':
        unit='ppbv'
    elif var == 'mass_fraction_of_methane_in_air':
        unit='ppmv'
    elif var == 'mass_fraction_of_nitrous_oxide_in_air':
        unit='ppbv'
    elif var == 'mass_fraction_of_carbon_monoxide_in_air':
        unit='ppmv'
    elif var == 'mass_fraction_of_nitrogen_monoxide_in_air':
        unit='pptv'
    # mol.gridcell-1.s-1
    elif var =='ch4_apparent_ems' or var=='ch4_ems':
        unit=r'$\mathrm{kg\ m^{-2} h^{-1}}$'	# kg.m-2.h-1
    elif var=='ch4_oh_rxn_flux': 
        unit=r'$\mathrm{kg(CH_{4})\ m^{-2} h^{-1}}$'	# kg.m-2.h-1
    elif var =='age_of_air':			# s
        unit=r'days'
    else:
        unit=''
    return unit


