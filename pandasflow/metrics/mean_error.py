from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
import pandas as pd


def mean_error(y_true, y_pred):
	'''print beauty table
	'''
	mae = mean_absolute_error(y_true, y_pred)
	mape = mean_absolute_percentage_error(y_true, y_pred)
	
	table = pd.DataFrame()
	table.index = ['MAE', 'MAPE']
	table[' '] = [mae, mape]

	print(table)
	
	return mae, mape