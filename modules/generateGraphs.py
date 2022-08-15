import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import e
import numpy as np

# from numba import jit, cuda

def objective(x, a, b, p):
    # return a*x**p + b
    # return a*e**(p*x) + b
    # a*e**(p*x) + b
    # I = a*(e**(p*x)-1)
    # (1/(25.852*10**-3))*
    return a*(e**(p*x)-1) + b


plt.rcParams['axes.facecolor'] = 'black'
regressionResults = open('outputs/regressions.txt', 'w')

# function generateIndivGraph: generates a graph for a single individual color
# @jit(target ="cuda")  
def generateIndivGraph(colorVal):
    # read variable colorVal.csv and plot it
    colorDf = pd.read_csv('inputs/' + colorVal + '.csv')
    # Plot the data with Vdio on the x-axis, I on the y-axis, and color by colorVal, and a black background.
    plt.title('Relation between Voltage and Current for ' + colorVal + ' Color Diode')
    plt.xlabel('Vdio')
    plt.ylabel('I')
    plt.scatter(colorDf['Vdio'], colorDf['I'], c=colorVal, cmap=plt.cm.Blues, edgecolors='none')
    # Create a regression curve using the data and the objective function.
    # param_bounds=([-np.inf,-np.inf,0],[np.inf,np.inf,np.inf])
    # param_bounds=([-20,-np.inf,-np.inf],[20,np.inf,np.inf])
    param_bounds=([-np.inf,-np.inf,-np.inf],[np.inf,np.inf,np.inf])
    popt, pcov = curve_fit(objective, colorDf['Vdio'], colorDf['I'], maxfev=10000, bounds=param_bounds)
    # Print the parameters of the regression curve.
    print('For LED color "' + colorVal + '", the parameters are: [a =', popt[0], 'b =', popt[1], 'p =', popt[2], end=']\n')
    regression = 'For ' + colorVal + ' color, the parameters are: [a = '+ str(popt[0])+ ' b = ' + str(popt[1]), ' p = ' + str(popt[2]), ' ]'
    regressionResults.write(str(regression)+'\n')
    # Plot the regression curve using the min and max values of the x-axis.
    # Linspace the x-axis from the min and max values of the x-axis.
    x = np.linspace(min(colorDf['Vdio']), max(colorDf['Vdio']), 100)


    # plt.plot(colorDf['Vdio'], objective(colorDf['Vdio'], *popt), 'r-', label=colorVal.capitalize()+ ' LED Diode Regression', color=colorVal, linewidth=.5)
    plt.plot(x, objective(x, *popt), 'r-', label=colorVal.capitalize()+ ' LED Diode Regression', color=colorVal, linewidth=.5)
    # Add a legend with white text.
    plt.legend(loc='upper left', facecolor='white', edgecolor='white', frameon=True)
    plt.savefig('outputs/' + colorVal + '.png')
    plt.show()


    
    # Plot the original data and connect each point together no regression curve.
    plt.plot(colorDf['Vdio'], colorDf['I'], color='white')
    plt.show()

# List of colors to plot
colorValList = ['white', 'red', 'yellow', 'blue', 'green']

# Generate the individual graphs for each color
for colorVal in colorValList:
    generateIndivGraph(colorVal)
