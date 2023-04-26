import pandasflow as pdf



y_true = [10, 10, 10, 10, 10]
y_pred = [5, 5, 7, 5, 5]



pdf.metrics.mean_error(y_true, y_pred)


