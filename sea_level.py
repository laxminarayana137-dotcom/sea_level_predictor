
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit using all data
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create extended years to 2050
    years_extended = range(df["Year"].min(), 2051)

    # Calculate predicted sea level
    line1 = res.intercept + res.slope * years_extended

    # Plot first line
    ax.plot(years_extended, line1, "r", label="Best Fit: All Data")

    # Create second line of best fit using data from year 2000 onwards
    df_recent = df[df["Year"] >= 2000]

    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])

    years_recent = range(2000, 2051)

    line2 = res_recent.intercept + res_recent.slope * years_recent

    # Plot second line
    ax.plot(years_recent, line2, "green", label="Best Fit: Since 2000")

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    ax.legend()

    # Save plot
    plt.savefig("sea_level_plot.png")

    # Return the plot
    return ax