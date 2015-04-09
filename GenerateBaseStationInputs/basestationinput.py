#!/usr/bin/env python

# This script generates the coordinate inputs for createbaseinfo_netcdf.
# It requires the cellid ascii file. To generate the cellid.asc file,
# first import the netcdf extent into grass and create a raster from it.
# Next, use mapcalc to generate a raster with unique id for each cell 
# (I used rows and columns), then you can export the resulting raster
# as an ASCII file which by default has the correct format for this.

fi = open('/media/cee-user/Storage/CRB_MANUAL/base/AbatzMetdataIDsASCII.asc', 'r')
fo = open('/media/cee-user/Storage/CRB_MANUAL/base/AbatzMetdataCoord.txt','w')

cols = int(fi.readline().split()[1])
rows = int(fi.readline().split()[1])
xbase = float(fi.readline().split()[1])
ybase = float(fi.readline().split()[1])
csize = float(fi.readline().split()[1])
fi.readline()


print xbase
print ybase
print csize

cellCount = 0

for i in range (0, rows):
  line = fi.readline().split()
  for j in range (0, cols):
    cellCount = cellCount + 1
    if int(line[j]) != -9999:

      xcoord = str(xbase + j*csize + csize/2)
      ycoord = str(ybase + csize/2 + (rows-i-1)*csize)

      print ("YCoord: %s  XCoord: %s" %(ycoord, xcoord) ) 
      fo.write(line[j]+" "+line[j]+" "+ycoord+" "+xcoord+" "+xcoord+" "+ycoord+"\n")
