import pandasflow as pdf
import pandas as pd


y_true = pd.Series([10, 10, 10, 10, 10])
y_pred = pd.Series([5, 5, 7, 5, 5])
weights = pd.Series([5, 5, 7, 5, 5])


pdf.metrics.mean_error(y_true, y_pred)
pdf.metrics.mean_error(y_true, y_pred, weights=weights)
