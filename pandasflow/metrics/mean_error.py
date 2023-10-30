from pandasflow import services
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

def mean_error(y_true: pd.Series, y_pred: pd.Series, weights: None | pd.Series = None):
	'''print beauty table
	'''
	
	if len(y_true) != len(y_pred):
		raise ValueError('Размеры массивов y_true и y_pred не совпадают!')
	
	if weights is not None:
		if len(y_pred) != len(weights):
			raise ValueError('Размер массива weights не соответствует размеру y_pred')
	
	
	mae = mean_absolute_error(y_true, y_pred)
	mape = mean_absolute_percentage_error(y_true, y_pred)
	smape = services.smape(y_true, y_pred)
	wape = None
	
	if weights is not None:
		wape = services.wape(y_true, y_pred, weights)
	
	t_index = ['MAE', 'MAPE', 'SMAPE']
	t_values = [mae, mape, smape]
	
	table = pd.DataFrame()
	table.index =	t_index if weights is None else t_index + ['WAPE']
	table[' ']	=	t_values if weights is None else t_values + [wape]
	
	print(table)
