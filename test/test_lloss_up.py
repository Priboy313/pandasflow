import pandasflow as pdf
import pandas as pd
import numpy as np


df = pd.read_csv('test_data.csv')

train, valid, test = pdf.split.train_valid_test(df)

train_full = pd.concat([train, valid])

model = train_full.groupby('NumOfProducts')['Exited'].mean().reset_index()
model = model.rename({'Exited':'score_prod'}, axis=1)

np.random.seed(42)
noise = np.random.uniform(0, 0.001, size=len(train_full))

train_full = train_full.merge(model, how='left', on='NumOfProducts')
train_full['score_prod'] = train_full['score_prod'] - noise

pdf.metrics.lloss_up(train_full, 'Exited', 'score_prod')