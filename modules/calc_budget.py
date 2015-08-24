''' calculate budgets 
average year
seasonal
yearly
'''
#################################################################### 
#################################################################### 
import netCDF4 as ncdf
import numpy as np
import module_seasonal_data
import calc_area

# (year = 360 days)
# ch4_oh_rxn_flux 	in mol.cell-1.s-1
# ch4_ems		in kg.m-2.s-1
def budget(netCDF, word):
    var=word
    ncbase=netCDF
    data = ncbase.variables[var]
    if var=='ch4_oh_rxn_flux':
        budget = int(round(np.sum(np.mean(data, axis=0)*16)*3600*24*360*1E-12))
    elif var=='ch4_ems' :
        lat = np.array(ncbase.variables['latitude'],dtype=np.float64)[:]
        lon = np.array(ncbase.variables['longitude'],dtype=np.float64)[:]
        area=calc_area.calc_area(lon,lat)	# m2.gridcell-1
        budget=int(round(np.sum(np.mean(data*area, axis=0))*3600*24*360*1E-9))			# Tg.yr-1
    unit = r'$\mathrm{\ Tg(CH_{4})\ yr^{-1}}$'
    return budget, unit

def budget_anc(netCDF, word):
    var=word
    ncbase=netCDF
    data = ncbase.variables[var]		# kg.m-2.-1
    lat = np.array(ncbase.variables['latitude'],dtype=np.float64)[:]
    lon = np.array(ncbase.variables['longitude'],dtype=np.float64)[:]
    area=calc_area.calc_area(lon,lat)		# m2.gridcell-1
    budget=int(round(np.sum(np.mean(data*area, axis=0))*3600*24*360*1E-9))			# Tg.yr-1
    unit = r'$\mathbf{\ Tg\ yr^{-1}}$'
    return budget, unit

def seasonal_budget(netCDF, word):
    var=word
    ncbase=netCDF
    season=seasonal_data.season(ncbase, var)
    budget=[]
    for i in range(0,4):
      if var=='ch4_oh_rxn_flux':
        budget.append(int(round(np.sum(season[i]*16)*3600*24*360*1E-12)))
      elif var=='ch4_ems':
        lat = np.array(ncbase.variables['latitude'],dtype=np.float64)[:]
        lon = np.array(ncbase.variables['longitude'],dtype=np.float64)[:]
        area=calc_area.calc_area(lon,lat)	# m2.gridcell-1
        budget.append(int(round(np.sum(season[i]*area)*3600*24*360*1E-9)))	# Tg.yr-1
      unit = r'$\mathrm{\ Tg(CH_{4})\ yr^{-1}}$'
    return budget, unit

def yearly_budget(netCDF, word): 
    var=word
    ncbase=netCDF
    data = ncbase.variables[var]
    budget=[]
    for y in range(0,np.shape(data)[0]/12):
        if var=='ch4_oh_rxn_flux':
            budget.append(int(round(np.sum(np.mean(data[y*12:(y+1)*12], axis=0)*16)*3600*24*360*1E-12)))
        elif var=='ch4_ems':
            lat = np.array(ncbase.variables['latitude'],dtype=np.float64)[:]
            lon = np.array(ncbase.variables['longitude'],dtype=np.float64)[:]
            area=calc_area.calc_area(lon,lat)	# m2.gridcell-1
            budget=int(round(np.sum(np.mean(data*area[y*12:(y+1)*12], axis=0))*3600*24*360*1E-9))		# Tg.yr-1
    unit = r'$\mathrm{\ Tg(CH_{4})\ yr^{-1}}$'
    return budget, unit

