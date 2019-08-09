#-----------------BEGIN HEADERS-----------------
import numpy as np
import matplotlib.pyplot as plt
#-----------------END HEADERS-----------------

ONI = []
data_y_clean = []
data_x_clean = []
data_5=[]
data_m5=[]

book = open('sst.dat', 'r')
data_y_string = list(book)
for i in range(len(data_y_string)):
    ONI.append(float(data_y_string[i]))

for i in range(len(ONI)/4):
    data_y_clean.append(ONI[4*i+1])
    data_x_clean.append(ONI[4*i+2] + ONI[4*i+3]/4.0)
    data_5.append(0.5)
    data_m5.append(-0.5)

del ONI

plt.title("Nino3.4 temperature")
plt.xlabel('Year')
plt.ylabel('Temperature anomaly (K)')
plt.plot(data_x_clean, data_y_clean)
plt.plot(data_x_clean, data_5)
plt.plot(data_x_clean, data_m5)
plt.savefig('plot.png')
