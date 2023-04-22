import pandasflow as pdf
from test import df
import pandas as pd




train, valid, test = pdf.split.train_valid_test(df)
print('\n')

train, valid, test = pdf.split.train_valid_test(df, target='Exited')
print('\n')

train, valid, test = pdf.split.train_valid_test(df, target='Exited', stratify='Exited')
print('\n')

train, valid, test = pdf.split.train_valid_test(df, target=['Exited', 'HasCrCard'])
print('\n')

train, valid, test = pdf.split.train_valid_test(df, target=['Exited', 'HasCrCard'], stratify='Exited')
print('\n')

#
# train, valid, test = pdf.split.train_valid_test(df, target=['Surname'])
# print('\n')
