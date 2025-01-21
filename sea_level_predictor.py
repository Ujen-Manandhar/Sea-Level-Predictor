import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('CSV_files/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()