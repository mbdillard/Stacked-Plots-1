"""
Created on Wed May  1 11:42:14 2019

@author: Michael Dillard
"""

#Improvements
#   Expand y-axis (top and bottom) ever so slightly for all subplots

##############################
####    Stacked Plots   ######
##############################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#################################################################################
# Read in data file
#################################################################################

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

fileofinterest=['example1.csv']     # File to analyze, 1 Hz refresh for this file

data_path = os.path.join(__location__,*fileofinterest)
df = pd.read_csv(data_path)         # Since 1st column may not be the index, not using index_col=0

#################################################################################
# Specify parameters to plot
#################################################################################

d_vars = ({'Speeds' : ['CALIB_AIRSPEED', 'TRUE_AIRSPEED'],
          'Angle of \nAttack' : ['AOA_LEFT','AOA_RIGHT'],
          'Altitude' : ['ALTITUDE'],
          'Vertical Speed' : ['VERTICAL_SPEED'],
          'Heading' : ['MAGNETIC_HEADING'], 
          'Autoflight\nStatus' : ['AUTOPILOT_ENGAGED','AUTOTHROTTLE_ENGAGED'],
          'On Ground\nvs In Air' : ['IN_AIR'] } )

#################################################################################
# Configure markers and colors
#################################################################################

# Vertical line config
vline1loc   = 700       # location on x-axis
vline1alpha = 0.5       # line transparency
vline1width = 5         # line width
vline1color = 'gray'    # line color

# Y-axis label location
yaxisloc = (-0.05,0.5)

# Y-axis labels
yaxislabels = ['kts','degs','feet','feet/min','degs','on/off','on/off']

# Subplot index (captures length of dictionary, sets to use 1 column)
subindex = (len(d_vars) * 100) + 11

# Colors to iterate through
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']

##############################################################################
# Plot
##############################################################################

plt.figure(figsize=(15,10), dpi=80)         # set figure size and dpi

for index, (key, value) in enumerate(d_vars.items()):
    ax1 = plt.subplot(subindex + index)     # set ax1 to whatever subplot we're on now
    ax1.set_xticklabels([])                 # clear x-axis for this subplot

    for index2, v in enumerate(d_vars[key]):
        plt.plot(df[v].dropna(), alpha=0.6, linewidth=3, color=colors[index+index2])    # Data line config
        plt.title(key, x=0.02, y=0.5, fontsize=11, horizontalalignment='left', verticalalignment='center', bbox=dict(facecolor='white', alpha=0.5)) #Subplot title config
        plt.grid(True)
    
        ax1.grid(which='major', axis='both', linestyle='-', linewidth=0.5, color='grey', alpha=0.4)  # Subplot major grid config
        ax1.minorticks_on()
        ax1.grid(which='minor', axis='x', linestyle=':', linewidth=0.5, color='grey', alpha=0.4)  # Subplot minor grid config
        ax1.set_ylabel(yaxislabels[index])                                              # Set y-axis label from pre-established array
        ax1.yaxis.set_label_coords(*yaxisloc)                                           # Set y-axis label location

    ax1.legend(labels=value, loc='upper right', ncol=1)                                 # Set legend location
    plt.axvline(x=vline1loc, alpha=vline1alpha, linewidth=vline1width, color=vline1color) # Create vertical marker line
    ax1.set_xticks( np.arange(0, (len(df) + 1), len(df)/10 ))   # Set xtick marks to match length of df, with 10 markers

    if index == len(d_vars.items()) - 1:                # For last subplot only, set x-axis labels
        xaxisvalues = ax1.get_xticks().astype(str)      # Get the 10 x-axis tickmarks
        xaxisvalues = [ i[ : -2] for i in xaxisvalues ] # Strip last 2 characters, in this case are .0
        ax1.set_xticklabels( xaxisvalues )              # Set xticklabels with formatted strings

ax1.set_xlabel('Time (secs)', fontsize=14)          # Display x-axis label for last subplot
    
plt.suptitle('Recorded Flight Parameters Depicted over Time', fontsize=16, x=0.5, y=0.95)
plt.gcf().set_facecolor('whitesmoke')       # background color config
plt.subplots_adjust(hspace=0.18)            # white space between subplots
plt.show()

#plt.savefig('example1.png', format='png', dpi=600)     #if you want to save the figure