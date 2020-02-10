import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('Pokemon.csv')
df = df[['Name', 'Type 1', 'Generation', 'Legendary']]

label = LabelEncoder()
dfUji = df
dfUji['Type 1'] = label.fit_transform(dfUji['Type 1'])

cosScore = cosine_similarity(df[['Type 1', 'Generation' ,'Legendary']])