import pandasflow as pdf
from test import df
import pandas as pd



train, test = pdf.split.train_test(df)
print('\n')


train, test = pdf.split.train_test(df, target='Exited')
print('\n')



train, test = pdf.split.train_test(df, target='Exited', stratify='Exited')
print('\n')

