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
        cube.long_name='T on theta levels in K'
        cube.attributes['name']=r'Temperature'
        cube.attributes['outputname']=r'T'
        cube.attributes['formula']=r'$\mathrm{T}$'
        cube.attributes['unit']='K'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s00i408':
        cube.standard_name='air_pressure'
        cube.long_name='P on theta levels in Pa'
        cube.attributes['name']=r'Pressure'
        cube.attributes['outputname']=r'P'
        cube.attributes['formula']=r'$\mathrm{P}$'
        cube.attributes['unit']='Pa'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i150':
        cube.var_name='age_of_air'
        cube.long_name='Age of air in s'
        cube.attributes['name']=r'Age of air'
        cube.attributes['outputname']=r'Age_of_air'
        cube.attributes['formula']=r'$\mathrm{Age\ of\ air}$'
        cube.attributes['unit']='s'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s00i010':
        cube.standard_name='specific_humidity'
        cube.long_name='Specific humidity in kg(H2O)/kg(air)'
        cube.attributes['name']=r'Specific humidity'
        cube.attributes['outputname']=r'Spec_humidity'
        cube.attributes['formula']=r'$\mathrm{H_{2}O}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=0.621
        cube.attributes['molmass']=18

    if cube.attributes['STASH'] == 'm01s30i451':
        cube.var_name='tropopause_pressure'
        cube.long_name='P at Tropopause Level in Pa'
        cube.attributes['name']=r'Pressure at Tropopause'
        cube.attributes['outputname']=r'P_tropopause'
        cube.attributes['formula']=r'$\mathrm{P_{Tropopause}}$'
        cube.attributes['unit']='Pa'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s30i452':
        cube.var_name='tropopause_temperature'
        cube.long_name='T at Tropopause Level'
        cube.attributes['name']=r'Temperature at Tropopause'
        cube.attributes['outputname']=r'T_tropopause'
        cube.attributes['formula']=r'$\mathrm{T_{Tropopause}}$'
        cube.attributes['unit']='K'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s30i453':
        cube.var_name='tropopause_height'
        cube.long_name='z at Tropopause Level'
        cube.attributes['name']=r'Height at Tropopause'
        cube.attributes['outputname']=r'Height_tropopause'
        cube.attributes['formula']=r'$\mathrm{z_{Tropopause}}$'
        cube.attributes['unit']='m'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1
#--------------------------------------------------------------
# Tracers UKCA
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i001':
        cube.standard_name='mass_fraction_of_ozone_in_air'
        cube.long_name='O3 MMR in kg(O3)/kg(air)'
        cube.attributes['name']=r'Ozone'
        cube.attributes['outputname']=r'O3'
        cube.attributes['formula']=r'$\mathrm{O_{3}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=1.657
        cube.attributes['molmass']=48

    if cube.attributes['STASH'] == 'm01s34i002':
        cube.standard_name='mass_fraction_of_nitrogen_monoxide_in_air'
        cube.long_name='NO MMR in kg(NO)/kg(air)'
        cube.attributes['name']=r'Nitrogen monoxide'
        cube.attributes['outputname']=r'NO'
        cube.attributes['formula']=r'$\mathrm{NO}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=1.036
        cube.attributes['molmass']=30

    if cube.attributes['STASH'] == 'm01s34i003':
        cube.var_name='mass_fraction_of_NO3_in_air'
        cube.long_name='NO3 MMR in kg(NO3)/kg(air)'
        cube.attributes['name']=r'NO3'
        cube.attributes['outputname']=r'NO3'
        cube.attributes['formula']=r'$\mathrm{NO_{3}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=2.14
        cube.attributes['molmass']=62

    if cube.attributes['STASH'] == 'm01s34i009':
        cube.standard_name='mass_fraction_of_methane_in_air'
        cube.long_name='CH4 MMR in kg(CH4)/kg(air)'
        cube.attributes['name']=r'Methane'
        cube.attributes['outputname']=r'CH4'
        cube.attributes['formula']=r'$\mathrm{CH_{4}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=0.552
        cube.attributes['molmass']=16

    if cube.attributes['STASH'] == 'm01s34i010':
        cube.standard_name='mass_fraction_of_carbon_monoxide_in_air'
        cube.long_name='CO MMR in kg(CO)/kg(air)'
        cube.attributes['name']=r'Carbon monoxide'
        cube.attributes['outputname']=r'CO'
        cube.attributes['formula']=r'$\mathrm{CO}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=0.967
        cube.attributes['molmass']=28

    if cube.attributes['STASH'] == 'm01s34i017':
        cube.standard_name='mass_fraction_of_peroxyacetyl_nitrate_in_air'
        cube.long_name='PAN MMR in kg(PAN)/kg(air)'
        cube.attributes['name']=r'PAN'
        cube.attributes['outputname']=r'PAN'
        cube.attributes['formula']=r'$\mathrm{PAN}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=4.177
        cube.attributes['molmass']=121

    if cube.attributes['STASH'] == 'm01s34i041':
        cube.var_name='mass_fraction_of_chlorine_in_air'
        cube.long_name='Cl MMR in kg(Cl)/kg(air)'
        cube.attributes['name']=r'Chlorine'
        cube.attributes['outputname']=r'Cl'
        cube.attributes['formula']=r'$\mathrm{Cl}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=1.225
        cube.attributes['molmass']=35.5

    if cube.attributes['STASH'] == 'm01s34i042':
        cube.standard_name='mass_fraction_of_chlorine_monoxide_in_air'
        cube.long_name='ClO MMR in kg(ClO)/kg(air)'
        cube.attributes['name']=r'Chlorine monoxide'
        cube.attributes['outputname']=r'ClO'
        cube.attributes['formula']=r'$\mathrm{ClO}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=1.778
        cube.attributes['molmass']=51.5

    if cube.attributes['STASH'] == 'm01s34i043':
        cube.standard_name='mass_fraction_of_dichlorine_peroxide_in_air'
        cube.long_name='Cl2O2 MMR in kg(Cl2O2)/kg(air)'
        cube.attributes['name']=r'Dichlorine peroxide'
        cube.attributes['outputname']=r'Cl2O2'
        cube.attributes['formula']=r'$\mathrm{Cl_{2}O_{2}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=3.555
        cube.attributes['molmass']=103

    if cube.attributes['STASH'] == 'm01s34i044':
        cube.standard_name='mass_fraction_of_chlorine_dioxide_in_air'
        cube.long_name='OClO MMR in kg(OClO)/kg(air)'
        cube.attributes['name']=r'Chlorine dioxide'
        cube.attributes['outputname']=r'ClO2'
        cube.attributes['formula']=r'$\mathrm{OClO}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=2.330
        cube.attributes['molmass']=67.5

    if cube.attributes['STASH'] == 'm01s34i049':
        cube.standard_name='mass_fraction_of_nitrous_oxide_in_air'
        cube.long_name='N2O MMR in kg(N2O)/kg(air)'
        cube.attributes['name']=r'Nitrous oxide'
        cube.attributes['outputname']=r'N2O'
        cube.attributes['formula']=r'$\mathrm{N_{2}O}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=1.519
        cube.attributes['molmass']=44

    if cube.attributes['STASH'] == 'm01s34i081':
        cube.standard_name='mass_fraction_of_hydroxyl_radical_in_air'
        cube.long_name='OH MMR in kg(OH)/kg(air)'
        cube.attributes['name']=r'Hydroxyl radical'
        cube.attributes['outputname']=r'OH'
        cube.attributes['formula']=r'$\mathrm{OH}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=0.587
        cube.attributes['molmass']=17

    if cube.attributes['STASH'] == 'm01s34i082':
        cube.standard_name='mass_fraction_of_hydroperoxyl_radical_in_air'
        cube.long_name='HO2 MMR in kg(HO2)/kg(air)'
        cube.attributes['name']=r'Hydroperoxyl radical'
        cube.attributes['outputname']=r'HO2'
        cube.attributes['formula']=r'$\mathrm{HO_{2}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=1.139
        cube.attributes['molmass']=33

    if cube.attributes['STASH'] == 'm01s34i149':
        cube.var_name='mass_fraction_of_passive_ozone_in_air'
        cube.long_name='passive O3 MMR in kg(O3)/kg(air)'
        cube.attributes['name']=r'Passive ozone'
        cube.attributes['outputname']=r'O3_passive'
        cube.attributes['formula']=r'$\mathrm{O_{3}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=1.657
        cube.attributes['molmass']=48

    if cube.attributes['STASH'] == 'm01s34i151':
        cube.var_name='mass_fraction_of_singlett_oxygen_in_air'
        cube.long_name='O(1D) MMR in kg(O1D)/kg(air)'
        cube.attributes['name']=r'Singlett Oxygen'
        cube.attributes['outputname']=r'O1D'
        cube.attributes['formula']=r'$\mathrm{O(^{1}D)}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=0.552
        cube.attributes['molmass']=16

    if cube.attributes['STASH'] == 'm01s34i152':
        cube.standard_name='mass_fraction_of_nitrogen_dioxide_in_air'
        cube.long_name='NO2 MMR in kg(NO2)/kg(air)'
        cube.attributes['name']=r'Nitrogen dioxide'
        cube.attributes['outputname']=r'NO2'
        cube.attributes['formula']=r'$\mathrm{NO_{2}}$'
        cube.attributes['unit']='1'
        cube.attributes['conversion_factor']=1.588
        cube.attributes['molmass']=46
#--------------------------------------------------------------
#?# unit Dobson? conversion factor
    if cube.attributes['STASH'] == 'm01s34i172':
        cube.var_name='Ozone_column'
        cube.long_name='O3 column in Dobson'
        cube.attributes['name']=r'Ozone column'
        cube.attributes['outputname']=r'O3_column'
        cube.attributes['formula']=r'$\mathrm{O_{3}^{column}}}$'
        cube.attributes['unit']='Dobson'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=48
#--------------------------------------------------------------
# Reaction fluxes
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i301':
        cube.var_name='ox_prod_HO2_NO'
        cube.long_name='Ox PROD: HO2+NO'
        cube.attributes['name']=r'H02+NO'
        cube.attributes['outputname']=r'HO2+NO'
        cube.attributes['formula']=r'$\mathrm{HO_{2}\ +\ NO}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i302':
        cube.var_name='ox_prod_MeOO_NO'
        cube.long_name='Ox PROD: MeOO+NO'
        cube.attributes['name']=r'MeOO+NO'
        cube.attributes['outputname']=r'MeOO+NO'
        cube.attributes['formula']=r'$\mathrm{MeOO\ +\ NO}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i303':
        cube.var_name='ox_prod_NO_RO2'
        cube.long_name='Ox PROD: NO+RO2'
        cube.attributes['name']=r'NO+RO2'
        cube.attributes['outputname']=r'NO+RO2'
        cube.attributes['formula']=r'$\mathrm{NO\ +\ RO_{2}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i304':
        cube.var_name='ox_prod_OH_inorgAcid'
        cube.long_name='Ox PROD: OH+INORGANIC ACID'
        cube.attributes['name']=r'OH+inorganic acid'
        cube.attributes['outputname']=r'OH+inorganic_acid'
        cube.attributes['formula']=r'$\mathrm{OH\ +\ acid_{inorg}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i305':
        cube.var_name='ox_prod_OH_orgNitrate'
        cube.long_name='Ox PROD: OH+ORGANIC NITRATE'
        cube.attributes['name']=r'OH+organic nitrate'
        cube.attributes['outputname']=r'OH+organic_nitrate'
        cube.attributes['formula']=r'$\mathrm{OH\ +\ nitrate_{org}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i306':
        cube.var_name='ox_prod_orgNitrate_photol'
        cube.long_name='Ox PROD: ORGANIC NITRATE PHOTOLYSIS'
        cube.attributes['name']=r'Organic nitrate photolysis'
        cube.attributes['outputname']=r'Org_nitrate_photol'
        cube.attributes['formula']=r'$\mathrm{nitrate_{org}^{photolysis}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i307':
        cube.var_name='ox_prod_OH_PANrxns'
        cube.long_name='Ox PROD: OH + PAN-TYPE REACTIONS'
        cube.attributes['name']=r'OH+PAN-type reactions'
        cube.attributes['outputname']=r'OH+PAN-type'
        cube.attributes['formula']=r'$\mathrm{OH\ +\ PAN_{type}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i311':
        cube.var_name='ox_loss_O1D_H2O'
        cube.long_name='Ox LOSS: O(1D)+H2O'
        cube.attributes['name']=r'O(1D)+H2O'
        cube.attributes['outputname']=r'O(1D)+H2O'
        cube.attributes['formula']=r'$\mathrm{O(^{1}D)\ +\ H_{2}O}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i312':
        cube.var_name='ox_loss_minor_rxns'
        cube.long_name='Ox LOSS: MINOR LOSS REACTIONS'
        cube.attributes['name']=r'Ox minor loss reactions'
        cube.attributes['outputname']=r'Ox_minor_loss'
        cube.attributes['formula']=r'$\mathrm{Ox loss_{minor}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i313':
        cube.var_name='ox_loss_HO2_O3'
        cube.long_name='Ox LOSS: HO2+O3'
        cube.attributes['name']=r'HO2+O3'
        cube.attributes['outputname']=r'O3+HO2'
        cube.attributes['formula']=r'$\mathrm{HO_{2}\ +\ O_{3}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i314':
        cube.var_name='ox_loss_OH_O3'
        cube.long_name='Ox LOSS: OH+O3'
        cube.attributes['name']=r'OH+O3'
        cube.attributes['outputname']=r'O3+OH'
        cube.attributes['formula']=r'$\mathrm{OH\ +\ O_{3}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i315':
        cube.var_name='ox_loss_O3_alkene'
        cube.long_name='Ox LOSS: O3+ALKENE'
        cube.attributes['name']=r'O3+alkene'
        cube.attributes['outputname']=r'O3+alkene'
        cube.attributes['formula']=r'$\mathrm{O_{3}\ +\ alkene}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i316':
        cube.var_name='ox_loss_N2O5_H2O'
        cube.long_name='Ox LOSS: N2O5+H2O'
        cube.attributes['name']=r'N2O5+H2O'
        cube.attributes['outputname']=r'N2O5+H2O'
        cube.attributes['formula']=r'$\mathrm{N_{2}O_{5}\ +\ H_{2}O}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i317':
        cube.var_name='ox_loss_NO3_chemloss'
        cube.long_name='Ox LOSS: NO3 CHEMICAL LOSS'
        cube.attributes['name']=r'NO3 chemical loss'
        cube.attributes['outputname']=r'NO3_chem_loss'
        cube.attributes['formula']=r'$\mathrm{NO_{3}^{chemical\ loss}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=62

    if cube.attributes['STASH'] == 'm01s34i321':
        cube.var_name='ozone_dry_dep_3D'
        cube.long_name='Ox BUDGET: O3 DRY DEPOSITION (3D)'
        cube.attributes['name']=r'Ozone dry deposition'
        cube.attributes['outputname']=r'O3_dry_dep'
        cube.attributes['formula']=r'$\mathrm{O_{3}\ dry\ deposition}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=48

    if cube.attributes['STASH'] == 'm01s34i322':
        cube.var_name='noy_dry_dep_3D'
        cube.long_name='Ox BUDGET: NOy DRY DEPOSITION (3D)'
        cube.attributes['name']=r'NOy dry deposition'
        cube.attributes['outputname']=r'NOy_dry_dep'
        cube.attributes['formula']=r'$\mathrm{NO_{y}\ dry\ deposition}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i331':
        cube.var_name='noy_wet_dep_3D'
        cube.long_name='Ox BUDGET: NOy WET DEPOSITION (3D)'
        cube.attributes['name']=r'NOy wet deposition'
        cube.attributes['outputname']=r'NOy_wet_dep'
        cube.attributes['formula']=r'$\mathrm{NO_{y}\ wet\ deposition}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i341':
        cube.var_name='ch4_oh_rxn_flux'
        cube.long_name='CH4 + OH reaction flux in mol/gridcell/s'
        cube.attributes['name']=r'CH4+OH'
        cube.attributes['outputname']=r'CH4+OH'
        cube.attributes['formula']=r'$\mathrm{CH_{4}\ +\ OH}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i351':
        cube.var_name='STE_ozone'
        cube.long_name='Stratosphere-Troposphere-Exchange of ozone'
        cube.attributes['name']=r'STE Ozone'
        cube.attributes['outputname']=r'O3_STE'
        cube.attributes['formula']=r'$\mathrm{STE\ O_{3}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=48

    if cube.attributes['STASH'] == 'm01s34i352':
        cube.var_name='tendency_ozone_troposphere'
        cube.long_name='Tendency ozone in troposphere'
        cube.attributes['name']=r'Tendency ozone troposphere'
        cube.attributes['outputname']=r'O3_tendency_tropos'
        cube.attributes['formula']=r'$\mathrm{Tendency\ O_{3}^{troposphere}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=48

    if cube.attributes['STASH'] == 'm01s34i354':
        cube.var_name='tendency_ozone_atm'
        cube.long_name='Tendency ozone in whole atmosphere'
        cube.attributes['name']=r'Tendency ozone atmosphere'
        cube.attributes['outputname']=r'O3_tendency_atmos'
        cube.attributes['formula']=r'$\mathrm{Tendency\ O_{3}^{atmosphere}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=48
# ?unit
    if cube.attributes['STASH'] == 'm01s34i353':
        cube.var_name='tropos_ozone'
        cube.long_name='Tropospheric ozone'
        cube.attributes['name']=r'Trospopheric ozone'
        cube.attributes['outputname']=r'O3_tropos'
        cube.attributes['formula']=r'$\mathrm{O_{3}^{troposphere}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=48

    if cube.attributes['STASH'] == 'm01s34i361':
        cube.var_name='air_mass_trop'
        cube.long_name='Air mass of troposphere'
        cube.attributes['name']=r'Air mass troposphere'
        cube.attributes['outputname']=r'Air_mass_tropos'
        cube.attributes['formula']=r'$\mathrm{Air\ mass^{troposphere}}$'
        cube.attributes['unit']='kg gridcell-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i363':
        cube.var_name='air_mass_atm'
        cube.long_name='Air mass of whole atmosphere'
        cube.attributes['name']=r'Air mass atmosphere'
        cube.attributes['outputname']=r'Air_mass_atmos'
        cube.attributes['formula']=r'$\mathrm{Air\ mass^{atmosphere}}$'
        cube.attributes['unit']='kg gridcell-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1

    if cube.attributes['STASH'] == 'm01s34i362':
        cube.var_name='tropospheric_mask'
        cube.long_name='Tropospheric mask'
        cube.attributes['name']=r'Tropospheric mask'
        cube.attributes['outputname']=r'Tropos_Mask'
        cube.attributes['formula']=r'$\mathrm{Tropospheric mask}$'
        cube.attributes['unit']='1:tropos,0:other'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=1
#--------------------------------------------------------------
# Emissions
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i451':
        cube.var_name='ch4_apparent_ems'
        cube.long_name='CH4 forced surf ems flux in mol/gridcell/s'
        cube.attributes['name']=r'CH4 surf emissions forced'
        cube.attributes['outputname']=r'CH4_surfems_forced'
        cube.attributes['formula']=r'$\mathrm{CH_{4}\ surface\ emissions^{forced}}$'
        cube.attributes['unit']='mol gridcell-1 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=16

    if cube.attributes['STASH'] == 'm01s00i302':
        cube.var_name='ch4_ems'
        cube.long_name='CH4 ems flux in kg/m-2/s'
        cube.attributes['name']=r'CH4 surf emissions'
        cube.attributes['outputname']=r'CH4_surfems'
        cube.attributes['formula']=r'$\mathrm{CH_{4}\ surface\ emissions}$'
        cube.attributes['unit']='kg m-2 s-1'
        cube.attributes['conversion_factor']=1
        cube.attributes['molmass']=16



