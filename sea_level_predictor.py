import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'])

    # regression 
    model= linregress(x=df.Year, y=df['CSIRO Adjusted Sea Level'])
    slope = model.slope
    intercept= model.intercept

    # predicted dataframe
    predicted_df = pd.DataFrame({'Year':np.arange(1880, 2051)})
    predicted_df['Estimated Adjusted Sea Level'] =predicted_df.Year.apply(lambda x: slope * x + intercept)

    # Create first line of best fit till 2050
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'])
    plt.plot(predicted_df.Year, predicted_df['Estimated Adjusted Sea Level'])

    # data from year 2000 
    df_2000 = df[df.Year >= 2000]

    # prediction
    predicted_df_2000 = predicted_df[predicted_df.Year >= 2000]

    # Create second line of best fit
    plt.scatter(df_2000.Year, df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(predicted_df_2000.Year, predicted_df_2000['Estimated Adjusted Sea Level'])

    # Add labels and title
    plt.xlabel('Years')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()