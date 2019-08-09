''' Assign information to STASH numbers.
Such as variable names, units, conversion factors.
'''
#################################################################### 
# ASSIGN INFORMATION TO STASH NUMBERS

# Standard names than iris reads can be in file in "python:> help(iris.std_names)": /usr/local/shared/ubuntu-12.04/x86_64/python2.7-iris/1.6.1/local/lib/python2.7/site-packages/Iris-1.6.1-py2.7.egg/iris/std_names.py

#-------------------------------------------------------------------

# conversion factor= cspecies=M(var)/M(air)=M(var)/28.97g.mol-1
#################################################################### 

def UKCA_callback(cube, field, filename):
    if cube.attributes['STASH'] == 'm01s16i004':
        cube.standard_name='air_temperature'

    if cube.attributes['STASH'] == 'm01s00i408':
        cube.standard_name='air_pressure'

    if cube.attributes['STASH'] == 'm01s34i150':
        cube.var_name='age_of_air'

    if cube.attributes['STASH'] == 'm01s00i010':
        cube.standard_name='specific_humidity'

    if cube.attributes['STASH'] == 'm01s30i451':
        cube.var_name='tropopause_pressure'

    if cube.attributes['STASH'] == 'm01s30i452':
        cube.var_name='tropopause_temperature'

    if cube.attributes['STASH'] == 'm01s30i453':
        cube.var_name='tropopause_height'

    if cube.attributes['STASH'] == 'm01s00i004':
        cube.var_name='theta'

    if cube.attributes['STASH'] == 'm01s00i002':
        cube.var_name='u_wind'

    if cube.attributes['STASH'] == 'm01s34i361':
        cube.var_name='air_mass_trop'

    if cube.attributes['STASH'] == 'm01s34i363':
        cube.var_name='air_mass_atm'

    if cube.attributes['STASH'] == 'm01s34i362':
        cube.var_name='tropospheric_mask'

#--------------------------------------------------------------
# Tracers UKCA
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i001':
        cube.standard_name='mass_fraction_of_ozone_in_air'

    if cube.attributes['STASH'] == 'm01s34i002':
        cube.standard_name='mass_fraction_of_nitrogen_monoxide_in_air'

    if cube.attributes['STASH'] == 'm01s34i003':
        cube.var_name='mass_fraction_of_NO3_in_air'

    if cube.attributes['STASH'] == 'm01s34i006':
        cube.var_name='mass_fraction_of_HONO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i008':
        cube.var_name='mass_fraction_of_H2O2_in_air'

    if cube.attributes['STASH'] == 'm01s34i009':
        cube.standard_name='mass_fraction_of_methane_in_air'

    if cube.attributes['STASH'] == 'm01s34i010':
        cube.standard_name='mass_fraction_of_carbon_monoxide_in_air'

    if cube.attributes['STASH'] == 'm01s34i011':
        cube.var_name='mass_fraction_of_HCHO_in_air'

    if cube.attributes['STASH'] == 'm01s34i012':
        cube.var_name='mass_fraction_of_MeOOH_in_air'

    if cube.attributes['STASH'] == 'm01s34i014':
        cube.var_name='mass_fraction_of_C2H6_in_air'

    if cube.attributes['STASH'] == 'm01s34i015':
        cube.var_name='mass_fraction_of_EtOOH_in_air'

    if cube.attributes['STASH'] == 'm01s34i016':
        cube.var_name='mass_fraction_of_MeCHO_in_air'

    if cube.attributes['STASH'] == 'm01s34i017':
        cube.standard_name='mass_fraction_of_peroxyacetyl_nitrate_in_air'

    if cube.attributes['STASH'] == 'm01s34i018':
        cube.var_name='mass_fraction_of_C3H8_in_air'

    if cube.attributes['STASH'] == 'm01s34i021':
        cube.var_name='mass_fraction_of_EtCOH_in_air'

    if cube.attributes['STASH'] == 'm01s34i022':
        cube.var_name='mass_fraction_of_Me2CO_in_air'

    if cube.attributes['STASH'] == 'm01s34i027':
        cube.var_name='mass_fraction_of_C5H8_in_air'

    if cube.attributes['STASH'] == 'm01s34i041':
        cube.var_name='mass_fraction_of_chlorine_in_air'

    if cube.attributes['STASH'] == 'm01s34i042':
        cube.standard_name='mass_fraction_of_chlorine_monoxide_in_air'

    if cube.attributes['STASH'] == 'm01s34i043':
        cube.standard_name='mass_fraction_of_dichlorine_peroxide_in_air'

    if cube.attributes['STASH'] == 'm01s34i044':
        cube.standard_name='mass_fraction_of_chlorine_dioxide_in_air'

    if cube.attributes['STASH'] == 'm01s34i045':
        cube.var_name='mass_fraction_of_Br_in_air'

    if cube.attributes['STASH'] == 'm01s34i046':
        cube.var_name='mass_fraction_of_BrO_in_air'

    if cube.attributes['STASH'] == 'm01s34i049':
        cube.standard_name='mass_fraction_of_nitrous_oxide_in_air'

    if cube.attributes['STASH'] == 'm01s34i050':
        cube.var_name='mass_fraction_of_HCl_in_air'

    if cube.attributes['STASH'] == 'm01s34i054':
        cube.var_name='mass_fraction_of_ClONO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i059':
        cube.var_name='mass_fraction_of_O3P_in_air'

    if cube.attributes['STASH'] == 'm01s34i081':
        cube.standard_name='mass_fraction_of_hydroxyl_radical_in_air'

    if cube.attributes['STASH'] == 'm01s34i082':
        cube.standard_name='mass_fraction_of_hydroperoxyl_radical_in_air'

    if cube.attributes['STASH'] == 'm01s34i149':
        cube.var_name='mass_fraction_of_passive_ozone_in_air'

    if cube.attributes['STASH'] == 'm01s34i151':
        cube.var_name='mass_fraction_of_singlett_oxygen_in_air'

    if cube.attributes['STASH'] == 'm01s34i152':
        cube.standard_name='mass_fraction_of_nitrogen_dioxide_in_air'

#--------------------------------------------------------------
#?# unit Dobson? conversion factor
    if cube.attributes['STASH'] == 'm01s34i172':
        cube.var_name='Ozone_column'
#--------------------------------------------------------------
# Reaction fluxes
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i301':
        cube.var_name='ox_prod_HO2_NO'

    if cube.attributes['STASH'] == 'm01s34i302':
        cube.var_name='ox_prod_MeOO_NO'

    if cube.attributes['STASH'] == 'm01s34i303':
        cube.var_name='ox_prod_NO_RO2'

    if cube.attributes['STASH'] == 'm01s34i304':
        cube.var_name='ox_prod_OH_inorgAcid'

    if cube.attributes['STASH'] == 'm01s34i305':
        cube.var_name='ox_prod_OH_orgNitrate'

    if cube.attributes['STASH'] == 'm01s34i306':
        cube.var_name='ox_prod_orgNitrate_photol'

    if cube.attributes['STASH'] == 'm01s34i307':
        cube.var_name='ox_prod_OH_PANrxns'

    if cube.attributes['STASH'] == 'm01s34i311':
        cube.var_name='ox_loss_O1D_H2O'

    if cube.attributes['STASH'] == 'm01s34i312':
        cube.var_name='ox_loss_minor_rxns'

    if cube.attributes['STASH'] == 'm01s34i313':
        cube.var_name='ox_loss_HO2_O3'

    if cube.attributes['STASH'] == 'm01s34i314':
        cube.var_name='ox_loss_OH_O3'

    if cube.attributes['STASH'] == 'm01s34i315':
        cube.var_name='ox_loss_O3_alkene'

    if cube.attributes['STASH'] == 'm01s34i316':
        cube.var_name='ox_loss_N2O5_H2O'

    if cube.attributes['STASH'] == 'm01s34i317':
        cube.var_name='ox_loss_NO3_chemloss'

    if cube.attributes['STASH'] == 'm01s34i321':
        cube.var_name='ozone_dry_dep_3D'

    if cube.attributes['STASH'] == 'm01s34i322':
        cube.var_name='noy_dry_dep_3D'

    if cube.attributes['STASH'] == 'm01s34i331':
        cube.var_name='noy_wet_dep_3D'

    if cube.attributes['STASH'] == 'm01s34i341':
        cube.var_name='ch4_oh_rxn_flux'

    if cube.attributes['STASH'] == 'm01s34i351':
        cube.var_name='STE_ozone'

    if cube.attributes['STASH'] == 'm01s34i352':
        cube.var_name='tendency_ozone_troposphere'

    if cube.attributes['STASH'] == 'm01s34i354':
        cube.var_name='tendency_ozone_atm'
# ?unit
    if cube.attributes['STASH'] == 'm01s34i353':
        cube.var_name='tropos_ozone'

    if cube.attributes['STASH'] == 'm01s34i381':
        cube.var_name='lightning_NOx'
#--------------------------------------------------------------
# Fixed Oxidants
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i062':
        cube.var_name='mmr_CH4anthropogenic'

    if cube.attributes['STASH'] == 'm01s34i494':
        cube.var_name='flux_OHfix_CH4anth'

    if cube.attributes['STASH'] == 'm01s34i495':
        cube.var_name='flux_O1Dfix_CH4anth'

    if cube.attributes['STASH'] == 'm01s34i496':
        cube.var_name='flux_Clfix_CH4anth'


    if cube.attributes['STASH'] == 'm01s34i063':
        cube.var_name='mmr_CH4wetlands'

    if cube.attributes['STASH'] == 'm01s34i497':
        cube.var_name='flux_OHfix_CH4wetl'

    if cube.attributes['STASH'] == 'm01s34i498':
        cube.var_name='flux_O1Dfix_CH4wetl'

    if cube.attributes['STASH'] == 'm01s34i499':
        cube.var_name='flux_Clfix_CH4wetl'


    if cube.attributes['STASH'] == 'm01s34i065':
        cube.var_name='mmr_CH4termites'

    if cube.attributes['STASH'] == 'm01s34i500':
        cube.var_name='flux_OHfix_CH4term'

    if cube.attributes['STASH'] == 'm01s34i501':
        cube.var_name='flux_O1Dfix_CH4term'

    if cube.attributes['STASH'] == 'm01s34i502':
        cube.var_name='flux_Clfix_CH4term'


    if cube.attributes['STASH'] == 'm01s34i066':
        cube.var_name='mmr_CH4hydrates'

    if cube.attributes['STASH'] == 'm01s34i503':
        cube.var_name='flux_OHfix_CH4hydr'

    if cube.attributes['STASH'] == 'm01s34i504':
        cube.var_name='flux_O1Dfix_CH4hydr'

    if cube.attributes['STASH'] == 'm01s34i505':
        cube.var_name='flux_Clfix_CH4hydr'


    if cube.attributes['STASH'] == 'm01s34i067':
        cube.var_name='mmr_CH4soilloss'

    if cube.attributes['STASH'] == 'm01s34i506':
        cube.var_name='flux_OHfix_CH4soil'

    if cube.attributes['STASH'] == 'm01s34i507':
        cube.var_name='flux_O1Dfix_CH4soil'

    if cube.attributes['STASH'] == 'm01s34i508':
        cube.var_name='flux_Clfix_CH4soil'
#--------------------------------------------------------------
# Emissions
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i451':
        cube.var_name='ch4_apparent_ems'

    if cube.attributes['STASH'] == 'm01s00i302':
        cube.var_name='ch4_ems'



