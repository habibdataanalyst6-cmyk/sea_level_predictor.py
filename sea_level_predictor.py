import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # 3. Create first line of best fit (using all data 1880 - latest)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    line_all = res_all.intercept + res_all.slope * years_extended
    plt.plot(years_extended, line_all, 'r', label='Best Fit Line (1880-2050)')

    # 4. Create second line of best fit (using data from year 2000 - latest)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series(range(2000, 2051))
    line_recent = res_recent.intercept + res_recent.slope * years_recent_extended
    plt.plot(years_recent_extended, line_recent, 'green', label='Best Fit Line (2000-2050)')

    # 5. Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
