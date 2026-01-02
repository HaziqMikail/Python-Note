import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('pokemon.csv')

type_count = df['Type 1'].value_counts(ascending=True) #count occurrences of each unique value in 'Type 1' column

plt.bar(type_count.index, type_count.values , color='skyblue', edgecolor='black')
plt.xlabel('Pokemon Type')
plt.ylabel('Count')
plt.tight_layout()
plt.title('Number of Pokemon by Type')

plt.show()


















