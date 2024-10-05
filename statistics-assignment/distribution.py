import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm, uniform, expon

# Import dataset from excel
data = pd.read_excel("grupp7.xlsx", sheet_name="Uppgift3")


# Function to fit distribution for each dataset
def fit_and_print_dist_params(data, column_name):
    # fit exponential distribution
    loc, scale = expon.fit(data)
    print(f'Exponential distribution for {column_name}: rate (lambda) = {1/scale}, scale = {scale}')
    
    # fit Normal distribution
    mu, std = norm.fit(data)
    print(f'Normal distribution for {column_name}: mean = {mu}, std = {std}')
        
    # fit Uniform distribution
    a, b = uniform.fit(data)
    print(f'Uniform distribution for {column_name}: lower-bound = {a}, upper-bound = {b}')

#Plot the histogram for each dataset in the excel file
for column in data.columns:
    plt.figure
    plt.hist(data[column], bins=15, color='pink', edgecolor='blue')
    plt.title(f'Histogram of {column}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
