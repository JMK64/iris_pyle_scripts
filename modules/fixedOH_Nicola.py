''' 
Nicola's model output
match variable names of netCDF file with CH4 source
'''
#################################################################### 
#################################################################### 
import netCDF4 as ncdf
import numpy as np

def nicola(v):
  if v == 'rice':
    var = 'ch4a'
  elif v == 'coal':
    var = 'ch4b'
  elif v == 'gas':
    var = 'ch4c'
  elif v == 'animals':
    var = 'ch4d'
  elif v == 'sewage':
    var = 'ch4e'
  elif v == 'landfill':
    var = 'ch4f'
  elif v == 'manure':
    var = 'ch4g'
  elif v == 'resident':
    var = 'ch4h'
  elif v == 'termites':
    var = 'ch4i'
  elif v == 'ESibWet':
    var = 'ch4j'
  elif v == 'WSibWet':
    var = 'ch4k'
  elif v == 'EuropeWet':
    var = 'ch4l'
  elif v == 'AmerWet':
    var = 'ch4m'
  elif v == 'Twetland':
    var = 'ch4n'
  elif v == 'Hydrates':
    var = 'ch4o'
  elif v == 'Bioburn':
    var = 'ch4p'
  elif v == 'rice13C':
    var = 'ch4q'
  elif v == 'coal13C':
    var = 'ch4r'
  elif v == 'gas13C':
    var = 'ch4s'
  elif v == 'animals13C':
    var = 'ch4t'
  elif v == 'sewage13C':
    var = 'ch4u'
  elif v == 'landfill13C':
    var = 'ch4v'
  elif v == 'manure13C':
    var = 'ch4w'
  elif v == 'resident13C':
    var = 'ch4x'
  elif v == 'termites13C':
    var = 'ch4y'
  elif v == 'ESibWet13C':
    var = 'ch4z'
  elif v == 'WSibWet13C':
    var = 'ch4aa'
  elif v == '13C EuropeWet13C':
    var = 'ch4bb'
  elif v == 'AmerWet13C':
    var = 'ch4cc'
  elif v == 'Twetland13C':
    var = 'ch4dd'
  elif v == 'Hydrates13C':
    var = 'ch4ee'
  elif v == 'Bioburn13C':
    var = 'ch4ff'
  elif v == 'TOTch4':
    var = 'tch4'
  elif v == 'TOT13ch4':
    var = 'dch4'
  elif v == 'TOTch3d':
    var = 'ch3d'
  elif v == 'P':
    var = 'p'
  elif v == 'T':
    var = 't3d'
  elif v == 'Mass':
    var = 'sm'
  elif v == 'MCF':
    var = 'ccl3ch3'
  return var

