#!/usr/bin/python
#************************************************************
# Collate plots to create a pdf with multiple plots
# Ines Heimann, May 2015 
#************************************************************
import os

import scipy
import scipy.optimize as sciopt

import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as backend_pdf
import matplotlib.image as mpimg
#************************************************************
# Set up
pltpage	= 4	# plots per page
px	= 2	# plots per row
py	= 2	# plots per column

#************************************************************
# Plots 
indir	= '/home/xxx'
outdir	= '/home/xxx' 
outname = 'xxx.pdf' 

if not os.path.exists(outdir):
    os.makedirs(outdir)

name	= [
'a.png'
,'b.png'
]

#************************************************************
# Set up loop variables depending on how many plots per page, row, and column
pages=range(len(name)/pltpage)                  # number of pages in document
if not (len(name)/pltpage)*pltpage==len(name):  # if len(name)/pltpage not an integer
   pages.append(pages[-1]+1)

items=[]                                        # number of plots per page
for i in pages:
  if pltpage<len(name)-i*pltpage:
    items.append(pltpage)
  else:                                         # to account for possibility that the last page has less plots
    items.append(len(name)-i*pltpage)

items

#************************************************************
# Create and write out pdf
pp 	= backend_pdf.PdfPages(outdir+outname)

# j = for the individual page
# i = for the individual plots
for j in pages:
  plt.figure(figsize=(15,12))
  plt.subplots_adjust(left=0, bottom=0, right=1, top=1,\
                    wspace=0.02, hspace=0.02)
  for i in range(items[j]):
    plt.subplot(px,py,i+1)
    img=mpimg.imread(indir+name[j*pltpage+i])
    plt.imshow(img)
    plt.axis('off')
  plt.savefig(pp, format='pdf')

pp.close()


