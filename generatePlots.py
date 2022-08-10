# Optimal Usage: python -W ignore -u "c:\Users\spyre\Downloads\PhysLabs\script.py"

# Install the required packages.
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

dependencies = ['scipy', 'matplotlib', 'pandas']
for dependency in dependencies:
    # If package is not installed, install it.
    try:
        __import__(dependency)
    except ImportError:
        install(dependency)

# Main script
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# colorVals are White, Red, Yellow, Blue, and Green
colorValList = ['white', 'red', 'yellow', 'blue', 'green']

def objective(x, a, b, p):
    return a*x**p + b

# Set plot background color in matplotlib to black
plt.rcParams['axes.facecolor'] = 'black'

regressionResults = open('outputs/regressions.txt', 'w')

def plot_colorVal(colorVal):
    # read variable colorVal.csv and plot it
    colorDf = pd.read_csv('inputs/' + colorVal + '.csv')
    # Plot the data with Volts on the x-axis, Amps on the y-axis, and color by colorVal, and a black background.
    plt.title('Relation between Voltage and Current for ' + colorVal + ' Color Diode')
    plt.xlabel('Volts')
    plt.ylabel('Amps')
    plt.scatter(colorDf['Volts'], colorDf['Amps'], c=colorVal, cmap=plt.cm.Blues, edgecolors='none')
    # Create a regression curve using the data and the objective function.
    popt, pcov = curve_fit(objective, colorDf['Volts'], colorDf['Amps'])
    # Print the parameters of the regression curve.
    print('For LED color "' + colorVal + '", the parameters are: [a =', popt[0], 'b =', popt[1], 'p =', popt[2], end=']\n', file=regressionResults)
    # regression = 'For ' + colorVal + ' color, the parameters are: [a = '+ str(popt[0])+ ' b = ' + str(popt[1]), ' p = ' + str(popt[2]), ' ]'
    # regressionResults.write(regression)
    # Plot the regression curve.
    plt.plot(colorDf['Volts'], objective(colorDf['Volts'], *popt), 'r-', label=colorVal.capitalize()+ ' LED Diode Regression', color=colorVal, linewidth=.5)
    # Add a legend with white text.
    plt.legend(loc='upper left', facecolor='white', edgecolor='white', frameon=True)


for i in colorValList:
    plot_colorVal(i)

plt.savefig('outputs/combined.png')
plt.show()
