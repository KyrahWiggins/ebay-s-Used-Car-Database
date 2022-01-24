import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplot


pd.set_option('display.max_columns', None)
df = pd.read_csv('tc20171021.csv', encoding='latin-1')
data = pd.read_csv('true_car_listings.csv')

df.head(5)

df.tail(5)

df.columns
