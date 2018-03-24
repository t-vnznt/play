import numpy as np
import matplotlib.pyplot as plt
import h5py

filename = "H-H1_LOSC_4_V1-815828992-4096.hdf5"
datafile = h5py.File(filename, 'r')

# for key in datafile.keys():
#   print key

strain = datafile['strain']['Strain'].value
ts = datafile['strain']['Strain'].attrs['Xspacing']

print "\n\n"
metakeys = datafile['meta'].keys()
meta = datafile['meta']
for key in metakeys:
  print key, meta[key].value

gpsStart = meta['GPSstart'].value
duration = meta['Duration'].value
gpsEnd = gpsStart + duration

time = np.arange(gpsStart, gpsEnd, ts)

numSamples = 10000
plt.plot(time[0:numSamples], strain[0:numSamples])
plt.xlabel('GPS Time (s)')
plt.ylabel('H1 Strain')
plt.show()
