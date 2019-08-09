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

    if cube.attributes['STASH'] == 'm01s00i002':
        cube.var_name='u_wind'

    if cube.attributes['STASH'] == 'm01s00i004':
        cube.var_name='theta'

    if cube.attributes['STASH'] == 'm01s00i408':
        cube.standard_name='air_pressure'

    if cube.attributes['STASH'] == 'm01s16i004':
        cube.standard_name='air_temperature'

    if cube.attributes['STASH'] == 'm01s00i010':
        cube.standard_name='specific_humidity'

    if cube.attributes['STASH'] == 'm01s30i451':
        cube.var_name='tropopause_pressure'

    if cube.attributes['STASH'] == 'm01s30i452':
        cube.var_name='tropopause_temperature'

    if cube.attributes['STASH'] == 'm01s30i453':
        cube.var_name='tropopause_height'


#--------------------------------------------------------------
# Tracers UKCA
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i001':
        cube.standard_name='mass_fraction_of_ozone_in_air'

    if cube.attributes['STASH'] == 'm01s34i002':
        cube.standard_name='mass_fraction_of_nitrogen_monoxide_in_air'

    if cube.attributes['STASH'] == 'm01s34i003':
        cube.var_name='mass_fraction_of_NO3_in_air'

    if cube.attributes['STASH'] == 'm01s34i004':
        cube.var_name='mass_fraction_of_NOy_in_air'

    if cube.attributes['STASH'] == 'm01s34i006':
        cube.var_name='mass_fraction_of_HO2NO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i007':
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
        cube.var_name='mass_fraction_of_EtCHO_in_air'

    if cube.attributes['STASH'] == 'm01s34i022':
        cube.var_name='mass_fraction_of_Me2CO_in_air'

    if cube.attributes['STASH'] == 'm01s34i023':
        cube.var_name='mass_fraction_of_MeCOCH2OOH_in_air'

    if cube.attributes['STASH'] == 'm01s34i024':
        cube.var_name='mass_fraction_of_PPAN_in_air'

    if cube.attributes['STASH'] == 'm01s34i027':
        cube.var_name='mass_fraction_of_C5H8_in_air'

    if cube.attributes['STASH'] == 'm01s34i037':
        cube.var_name='mass_fraction_of_MeCO3H_in_air'

    if cube.attributes['STASH'] == 'm01s34i038':
        cube.var_name='mass_fraction_of_MeCO2H_in_air'

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

    if cube.attributes['STASH'] == 'm01s34i047':
        cube.var_name='mass_fraction_of_BrCl_in_air'

    if cube.attributes['STASH'] == 'm01s34i048':
        cube.var_name='mass_fraction_of_BrONO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i049':
        cube.standard_name='mass_fraction_of_nitrous_oxide_in_air'

    if cube.attributes['STASH'] == 'm01s34i050':
        cube.var_name='mass_fraction_of_HCl_in_air'

    if cube.attributes['STASH'] == 'm01s34i051':
        cube.var_name='mass_fraction_of_HOCl_in_air'

    if cube.attributes['STASH'] == 'm01s34i052':
        cube.var_name='mass_fraction_of_HBr_in_air'

    if cube.attributes['STASH'] == 'm01s34i053':
        cube.var_name='mass_fraction_of_HOBr_in_air'

    if cube.attributes['STASH'] == 'm01s34i054':
        cube.var_name='mass_fraction_of_ClONO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i055':
        cube.var_name='mass_fraction_of_CFCl3_in_air'

    if cube.attributes['STASH'] == 'm01s34i056':
        cube.var_name='mass_fraction_of_CF2Cl2_in_air'

    if cube.attributes['STASH'] == 'm01s34i057':
        cube.var_name='mass_fraction_of_MeBr_in_air'

    if cube.attributes['STASH'] == 'm01s34i058':
        cube.var_name='mass_fraction_of_N_in_air'

    if cube.attributes['STASH'] == 'm01s34i059':
        cube.var_name='mass_fraction_of_O3P_in_air'

    if cube.attributes['STASH'] == 'm01s34i060':
        cube.var_name='mass_fraction_of_BuOOH_in_air'

    if cube.attributes['STASH'] == 'm01s34i061':
        cube.var_name='mass_fraction_of_2C4ONO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i062':
        cube.var_name='mass_fraction_of_sBuONO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i063':
        cube.var_name='mass_fraction_of_23C5OONO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i064':
        cube.var_name='mass_fraction_of_3M2C4NO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i065':
        cube.var_name='mass_fraction_of_nBuO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i066':
        cube.var_name='mass_fraction_of_sBuO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i067':
        cube.var_name='mass_fraction_of_iPeO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i068':
        cube.var_name='mass_fraction_of_nPeO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i067':
        cube.var_name='mass_fraction_of_iPeO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i082':
        cube.var_name='mass_fraction_of_hydroperoxyl_radical_in_air'

    if cube.attributes['STASH'] == 'm01s34i083':
        cube.var_name='mass_fraction_of_methyl_peroxy_radical_in_air'

    if cube.attributes['STASH'] == 'm01s34i084':
        cube.var_name='mass_fraction_of_ethyl_peroxy_radical_in_air'

    if cube.attributes['STASH'] == 'm01s34i085':
        cube.var_name='mass_fraction_of_MeCO3_peroxy_radical_in_air'

    if cube.attributes['STASH'] == 'm01s34i086':
        cube.var_name='mass_fraction_of_n_propyl_peroxy_radical_in_air'

    if cube.attributes['STASH'] == 'm01s34i087':
        cube.var_name='mass_fraction_of_i_propyl_peroxy_radical_in_air'

    if cube.attributes['STASH'] == 'm01s34i091':
        cube.var_name='mass_fraction_of_iC4H10_in_air'

    if cube.attributes['STASH'] == 'm01s34i092':
        cube.var_name='mass_fraction_of_iC5H12_in_air'

    if cube.attributes['STASH'] == 'm01s34i093':
        cube.var_name='mass_fraction_of_nC5H12_in_air'

    if cube.attributes['STASH'] == 'm01s34i094':
        cube.var_name='mass_fraction_of_methanol_in_air'

    if cube.attributes['STASH'] == 'm01s34i095':
        cube.var_name='mass_fraction_of_MACRO2_in_air'

    if cube.attributes['STASH'] == 'm01s34i096':
        cube.var_name='mass_fraction_of_etono2_in_air'

    if cube.attributes['STASH'] == 'm01s34i097':
        cube.var_name='mass_fraction_of_prono2_in_air'

    if cube.attributes['STASH'] == 'm01s34i098':
        cube.var_name='mass_fraction_of_nC4H10_in_air'

##    #if cube.attributes['STASH'] == 'm01s34i099':
##    #    cube.standard_name='mass_concentration_of_brox_expressed_as_bromine_in_air'
##
##    if cube.attributes['STASH'] == 'm01s34i098':
##        cube.var_name='mass_concentration_of_clno2_in_air'
##
##    if cube.attributes['STASH'] == 'm01s34i099':
##        cube.var_name='mass_concentration_of_brno2_in_air'

    if cube.attributes['STASH'] == 'm01s34i149':
        cube.var_name='mass_fraction_of_passive_ozone_in_air'

    if cube.attributes['STASH'] == 'm01s34i150':
        cube.var_name='age_of_air'

    if cube.attributes['STASH'] == 'm01s34i151':
        cube.var_name='mass_fraction_of_singlet_oxygen_in_air'

    if cube.attributes['STASH'] == 'm01s34i152':
        cube.standard_name='mass_fraction_of_nitrogen_dioxide_in_air'

    if cube.attributes['STASH'] == 'm01s34i153':
        cube.standard_name='mass_fraction_of_bromine_monoxide_in_air'

    if cube.attributes['STASH'] == 'm01s34i154':
      cube.var_name='mass_fraction_of_hydrogen_chloride_in_air'

    if cube.attributes['STASH'] == 'm01s34i155':
      cube.var_name='mass_fraction_of_cly_as_hydrogen_chloride_in_air'
#--------------------------------------------------------------

    if cube.attributes['STASH'] == 'm01s34i171':
        cube.var_name='NAT'

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

    #if cube.attributes['STASH'] == 'm01s34i322':
    #    cube.var_name='noy_dry_dep_3D'

    #if cube.attributes['STASH'] == 'm01s34i331':
    #    cube.var_name='noy_wet_dep_3D'

    if cube.attributes['STASH'] == 'm01s50i022':
        cube.var_name='noy_dry_dep_3D'

    if cube.attributes['STASH'] == 'm01s50i023':
        cube.var_name='noy_wet_dep_3D'

    if cube.attributes['STASH'] == 'm01s34i341':
        cube.var_name='ch4_oh_rxn_flux'

    if cube.attributes['STASH'] == 'm01s34i351':
        cube.var_name='STE_ozone'

    if cube.attributes['STASH'] == 'm01s34i352':
        cube.var_name='trop_BrO_quote_column_quote'

    if cube.attributes['STASH'] == 'm01s34i353':
        cube.var_name='tropos_ozone'

    if cube.attributes['STASH'] == 'm01s34i354':
        cube.var_name='tendency_ozone_atm'
# ?unit
        cube.var_name='tropos_ozone'

    if cube.attributes['STASH'] == 'm01s34i361':
        cube.var_name='air_mass_trop'

    #if cube.attributes['STASH'] == 'm01s34i362':
    #    cube.var_name='tropospheric_mask'

    if cube.attributes['STASH'] == 'm01s50i062':
        cube.var_name='tropospheric_mask'

    #if cube.attributes['STASH'] == 'm01s34i363':
    #    cube.var_name='air_mass_atm'

    if cube.attributes['STASH'] == 'm01s50i063':
        cube.var_name='air_mass_atm'

    if cube.attributes['STASH'] == 'm01s34i381':
        cube.var_name='lightning_NOx'
#--------------------------------------------------------------
# Strat diags
#--------------------------------------------------------------

    if cube.attributes['STASH'] == 'm01s00i002':
        cube.var_name='u_comp_of_wind'

    if cube.attributes['STASH'] == 'm01s00i003':
        cube.var_name='v_comp_of_wind'

    if cube.attributes['STASH'] == 'm01s00i004':
        cube.var_name='theta'

    if cube.attributes['STASH'] == 'm01s00i010':
        cube.var_name='spec_hum'

    if cube.attributes['STASH'] == 'm01s00i012':
        cube.var_name='qcf'

    if cube.attributes['STASH'] == 'm01s00i101':
        cube.var_name='so2_mmr'

    if cube.attributes['STASH'] == 'm01s00i102':
        cube.var_name='DMS'

    if cube.attributes['STASH'] == 'm01s00i407':
        cube.var_name='pressure_on_rho_levels'

    if cube.attributes['STASH'] == 'm01s00i408':
        cube.var_name='pressure_on_theta_levels'

    if cube.attributes['STASH'] == 'm01s00i409':
        cube.var_name='surface_pressure'

    if cube.attributes['STASH'] == 'm01s16i004':
        cube.var_name='temp_on_theta_levels'

#    if cube.attributes['STASH'] == 'm01s34i151':
#        cube.var_name='temp_on_theta_levels'

    if cube.attributes['STASH'] == 'm01s34i391':
        cube.var_name='Strat_OH_Prod'

    if cube.attributes['STASH'] == 'm01s34i392':
        cube.var_name='Strat_OH_Loss'

    if cube.attributes['STASH'] == 'm01s34i401':
      cube.var_name='strat_ox_prod_O2_PHOTON'

    if cube.attributes['STASH'] == 'm01s34i411':
      cube.var_name='strat_ox_loss_Cl2O2_PHOTON'

    if cube.attributes['STASH'] == 'm01s34i412':
      cube.var_name='strat_ox_loss_bro_clo'

    if cube.attributes['STASH'] == 'm01s34i413':
      cube.var_name='strat_ox_loss_ho2_o3'

    if cube.attributes['STASH'] == 'm01s34i414':
      cube.var_name='strat_o3_loss_clo_ho2'

    if cube.attributes['STASH'] == 'm01s34i415':
      cube.var_name='strat_o3_loss_bro_ho2'

    if cube.attributes['STASH'] == 'm01s34i416':
      cube.var_name='strat_o3_loss_o3p_clo'

    if cube.attributes['STASH'] == 'm01s34i417':
      cube.var_name='strat_o3_loss_o3p_no2'

    if cube.attributes['STASH'] == 'm01s34i418':
      cube.var_name='strat_o3_loss_o3p_bro'

    if cube.attributes['STASH'] == 'm01s34i419':
      cube.var_name='strat_o3_loss_o3p_ho2'

    if cube.attributes['STASH'] == 'm01s34i420':
      cube.var_name='strat_o3_loss_o3_h'

    if cube.attributes['STASH'] == 'm01s34i421':
      cube.var_name='strat_o3_loss_no3_photolysis'

    if cube.attributes['STASH'] == 'm01s34i422':
      cube.var_name='strat_o3_loss_o3p_o3'

    if cube.attributes['STASH'] == 'm01s34i441':
      cube.var_name='no2_photolysis'

    if cube.attributes['STASH'] == 'm01s34i442':
      cube.var_name='o3_to_o1d_photolysis'

    if cube.attributes['STASH'] == 'm01s34i443':
      cube.var_name='n2o_photolysis'

    if cube.attributes['STASH'] == 'm01s34i450':
      cube.var_name='psc_diag_type1_psc'

    if cube.attributes['STASH'] == 'm01s34i451':
      cube.var_name='psc_diag_type2_psc'

    if cube.attributes['STASH'] == 'm01s34i452':
      cube.var_name='psc_diag_nat'

    if cube.attributes['STASH'] == 'm01s34i453':
      cube.var_name='psc_diag_ice'

    if cube.attributes['STASH'] == 'm01s34i454':
      cube.var_name='psc_diag_sad_type_1'

    if cube.attributes['STASH'] == 'm01s34i455':
      cube.var_name='psc_diag_sad_type_2'

    if cube.attributes['STASH'] == 'm01s34i456':
      cube.var_name='psc_diag_sad_so4'

    if cube.attributes['STASH'] == 'm01s34i457':
      cube.var_name='GAMMA1'

    if cube.attributes['STASH'] == 'm01s34i458':
      cube.var_name='GAMMA2'

    if cube.attributes['STASH'] == 'm01s34i459':
      cube.var_name='GAMMA3'

    if cube.attributes['STASH'] == 'm01s34i461':
      cube.var_name='tio2_diag_sad'

    if cube.attributes['STASH'] == 'm01s34i462':
      cube.var_name='tio2_diag_mass'

    if cube.attributes['STASH'] == 'm01s34i463':
      cube.var_name='tio2_diag_mmr'

    if cube.attributes['STASH'] == 'm01s34i464':
      cube.var_name='flux_clono2_h2o'

    if cube.attributes['STASH'] == 'm01s34i465':
      cube.var_name='flux_clono2_hcl'

    if cube.attributes['STASH'] == 'm01s34i466':
      cube.var_name='flux_hocl_hcl'

    if cube.attributes['STASH'] == 'm01s34i467':
      cube.var_name='flux_n2o5_h2o'

    if cube.attributes['STASH'] == 'm01s34i468':
      cube.var_name='flux_n2o5_hcl'

    if cube.attributes['STASH'] == 'm01s34i469':
      cube.var_name='flux_clono2_hbr'

    if cube.attributes['STASH'] == 'm01s34i470':
      cube.var_name='flux_hocl_hbr'

    if cube.attributes['STASH'] == 'm01s34i471':
      cube.var_name='flux_hobr_hcl'

    if cube.attributes['STASH'] == 'm01s34i472':
      cube.var_name='flux_brono2_hcl'

    if cube.attributes['STASH'] == 'm01s34i473':
      cube.var_name='flux_brono2_h2o'

    if cube.attributes['STASH'] == 'm01s34i474':
      cube.var_name='flux_hobr_hbr'

    if cube.attributes['STASH'] == 'm01s34i475':
      cube.var_name='flux_brono2_hbr'

    if cube.attributes['STASH'] == 'm01s34i476':
      cube.var_name='flux_n2o5_hbr'

    if cube.attributes['STASH'] == 'm01s39i001':
      cube.var_name='STASH_39001'

    if cube.attributes['STASH'] == 'm01s39i002':
      cube.var_name='STASH_39002'

    if cube.attributes['STASH'] == 'm01s39i003':
      cube.var_name='STASH_39003'

    if cube.attributes['STASH'] == 'm01s39i004':
      cube.var_name='STASH_39004'

    if cube.attributes['STASH'] == 'm01s39i005':
      cube.var_name='STASH_39005'

    if cube.attributes['STASH'] == 'm01s39i006':
      cube.var_name='STASH_39006'

    if cube.attributes['STASH'] == 'm01s39i007':
      cube.var_name='STASH_39007'

    if cube.attributes['STASH'] == 'm01s39i008':
      cube.var_name='STASH_39008'

    if cube.attributes['STASH'] == 'm01s39i009':
      cube.var_name='STASH_39009'
