import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#import dataset from excel
data = pd.read_excel("grupp7.xlsx", sheet_name="Uppgift3")

#Plot the histogram for each dataset in the excel file
for column in data.columns:
    plt.figure
    plt.hist(data[column], bins=15, color='pink', edgecolor='blue')
    plt.title(f'Histogram of {column}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
