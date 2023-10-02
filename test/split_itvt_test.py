import pandasflow as pdf
from test import df_eurusd as df
import pandas as pd



train, valid, test = pdf.split.inherit_train_valid_test(df)
print('\n')
print(test.tail())