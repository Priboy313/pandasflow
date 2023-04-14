from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error


def mean_error(y_true, y_pred):
	print(mean_absolute_error(y_true, y_pred))
	print(mean_absolute_percentage_error(y_true, y_pred))