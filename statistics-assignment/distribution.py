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

#Plot the histogram and fit distrubution for each dataset in the excel file
for column in data.columns:
    plt.figure
    plt.hist(data[column], bins=15, color='pink', alpha=0.7, edgecolor='blue', density=True)
    
    # Fit and print distribution parameters
    fit_and_print_dist_params(data[column], column)
    
    # Plot fitted exponential distribution
    loc, scale = expon.fit(data[column])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = expon.pdf(x, loc, scale)
    plt.plot(x, p, 'b:', linewidth=2, label="Exponential plot")
    
    # Plot fitted normal distribution
    mu, std = norm.fit(data[column])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p= norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2, label="Normal plot")
    
    # plot fitted Uniform distribution
    a,b = uniform.fit(data[column])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = uniform.pdf(x, a, b-a)
    plt.plot(x, p, 'r--', linewidth=2, label="Uniform plot")
    
    
    #Add title and labels and show plots
    plt.title(f'Histogram and fitted distribution of {column}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()
