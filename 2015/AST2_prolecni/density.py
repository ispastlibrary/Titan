import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, MaxNLocator
from numpy import linspace
from numpy import loadtxt
plt.ion()
 
# Define the x and y data 
# For example just using random numbers
#x = np.random.randn(10000)
#y = np.random.randn(10000)

x, y, z = loadtxt('halo_slika2.txt', unpack=True)
#x = x - 56793
#y = y - 17929
x = x - 79630
y = y - 17620


# Set up default x and y limits
xlims = [min(x),max(x)]
ylims = [min(y),max(y)]

#xlims = [-1000,1000]
#ylims = [-1000,1000]

# Set up your x and y labels
xlabel = '$\mathrm{Your\\ X\\ Label}$'
ylabel = '$\mathrm{Your\\ Y\\ Label}$'
 
# Define the locations for the axes
left, width = 0.12, 0.55
bottom, height = 0.12, 0.55
bottom_h = left_h = left+width+0.02
 
# Set up the geometry of the three plots
rect_temperature = [left, bottom, width, height] # dimensions of temp plot
rect_histx = [left, bottom_h, width, 0.25] # dimensions of x-histogram
rect_histy = [left_h, bottom, 0.25, height] # dimensions of y-histogram
 
# Set up the size of the figure
fig = plt.figure(1, figsize=(9.5,9))
 
# Make the three plots
axTemperature = plt.axes(rect_temperature) # temperature plot
axHistx = plt.axes(rect_histx) # x histogram
axHisty = plt.axes(rect_histy) # y histogram
 
# Remove the inner axes numbers of the histograms
nullfmt = NullFormatter()
axHistx.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)
 
# Find the min/max of the data
xmin = min(xlims)
xmax = max(xlims)
ymin = min(ylims)
ymax = max(ylims)
 
# Make the 'main' temperature plot
# Define the number of bins
nxbins = 200
nybins = 200
nbins = 200
 
xbins = linspace(start = xmin, stop = xmax, num = nxbins)
ybins = linspace(start = ymin, stop = ymax, num = nybins)
xcenter = (xbins[0:-1]+xbins[1:])/2.0
ycenter = (ybins[0:-1]+ybins[1:])/2.0
aspectratio = 1.0*(xmax - 0)/(1.0*ymax - 0)
 
H, xedges,yedges = np.histogram2d(y,x,bins=(ybins,xbins))
X = xcenter
Y = ycenter
Z = H
 
# Plot the temperature data
cax = (axTemperature.imshow(H, extent=[xmin,xmax,ymin,ymax],
       interpolation='none', origin='lower',aspect=aspectratio, cmap='spectral'))
 

#Plot the axes labels
axTemperature.set_xlabel(xlabel,fontsize=18)
axTemperature.set_ylabel(ylabel,fontsize=18)
 
#Make the tickmarks pretty
ticklabels = axTemperature.get_xticklabels()
for label in ticklabels:
    label.set_fontsize(12)
    label.set_family('serif')
 
ticklabels = axTemperature.get_yticklabels()
for label in ticklabels:
    label.set_fontsize(12)
    label.set_family('serif')
 
#Set up the plot limits
axTemperature.set_xlim(xlims)
axTemperature.set_ylim(ylims)
 
#Set up the histogram bins
xbins = np.arange(xmin, xmax, (xmax-xmin)/nbins)
ybins = np.arange(ymin, ymax, (ymax-ymin)/nbins)
 
#Plot the histograms
axHistx.hist(x, bins=xbins, color = 'blue')
axHisty.hist(y, bins=ybins, orientation='horizontal', color = 'red')
 
#Set up the histogram limits
axHistx.set_xlim( min(x), max(x) )
axHisty.set_ylim( min(y), max(y) )
 
#Make the tickmarks pretty
ticklabels = axHistx.get_yticklabels()
for label in ticklabels:
    label.set_fontsize(12)
    label.set_family('serif')
 
#Make the tickmarks pretty
ticklabels = axHisty.get_xticklabels()
for label in ticklabels:
    label.set_fontsize(12)
    label.set_family('serif')
 
#Cool trick that changes the number of tickmarks for the histogram axes
axHisty.xaxis.set_major_locator(MaxNLocator(4))
axHistx.yaxis.set_major_locator(MaxNLocator(4))
 
#Show the plot
plt.draw()
 
# Save to a File
filename = 'myplot'
plt.savefig(filename + '.pdf',format = 'pdf', transparent=True)
