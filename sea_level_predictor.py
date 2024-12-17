import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Data", alpha=0.6)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, intercept + slope * years_extended, label="Full Data Fit", color='red')

    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, intercept_recent + slope_recent * years_recent, label="2000+ Fit", color='green')

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.savefig('sea_level_plot.png')
    return plt.gcf()
