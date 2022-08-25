import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Plot I_B against I_C from ../inputs/data1.xlsx
def plot1(data1):
    # Plot I_B against I_C
    plt.plot(data1['I_B'], data1['I_C'], 'o')
    plt.xlabel('I_B')
    plt.ylabel('I_C')
    plt.title('I_B vs I_C')
    plt.show()

# Run plot1() with data1.xlsx
def runPlot1():
    data1 = pd.read_excel('../inputs/data1.xlsx')
    plot1(data1)

