import pandasflow as pdf
from test import df
import pandas as pd




train, valid, test = pdf.split.train_valid_test(df)
print('\n')

train, valid, test = pdf.split.train_valid_test(df, target='Exited')
print('\n')

train, valid, test = pdf.split.train_valid_test(df, target='Exited', stratify='Exited')
print('\n')

train, valid, test = pdf.split.train_valid_test(df, target=['Exited', 'Age'])
print('\n')

train, valid, test = pdf.split.train_valid_test(df, target=['Exited', 'Age'], stratify='Exited')
print('\n')

train, valid, test = pdf.split.train_valid_test(df, target=['Exited', 'Age'], stratify='Exited', round_=3)
print('\n')

train, valid, test = pdf.split.train_valid_test(df, target=['Exited', 'Age'], stratify='Exited', round_=1)
print('\n')