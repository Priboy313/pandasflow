import pandasflow as pdf
from test import df_eurusd as df
import pandas as pd



train, test = pdf.split.inherit_train_test(df)
print('\n')
print(test.tail())