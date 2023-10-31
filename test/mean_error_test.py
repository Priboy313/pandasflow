import pandasflow as pdf
import pandas as pd


y_true = pd.Series([10, 10, 10, 10, 10])
y_pred = pd.Series([5, 5, 7, 5, -5])
y_pred2 = pd.Series([6, 6, 8, 6, 6])

print('default')
prev = pdf.metrics.mean_error(y_true, y_pred2, r=True)
print('\nw\\prev&round')
pdf.metrics.mean_error(y_true, y_pred, previous=prev, round_=3)