import numpy as np

from pandasflow import services
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error, mean_squared_log_error

def mean_error(y_true: pd.Series, y_pred: pd.Series,
			   previous:  list | tuple | None = None,
			   round_: int | None = None,
			   r: bool = False,
			   ):
	'''print beauty table
	'''
	
	if len(y_true) != len(y_pred):
		raise ValueError('Размеры массивов y_true и y_pred не совпадают!')
	
	mae = mean_absolute_error(y_true, y_pred)
	mape = mean_absolute_percentage_error(y_true, y_pred)
	smape = services.smape(y_true, y_pred)
	rmse = mean_squared_error(y_true, y_pred, squared=False)
	try:
		rmsle = mean_squared_log_error(y_true, y_pred, squared=False)
	except Exception:
		rmsle = -1.111
	
	if round_ is not None:
		mae		= round(mae, round_)
		mape	= round(mape, round_)
		smape	= round(smape, round_)
		rmse	= round(rmse, round_)
		
		try:
			rmsle	= round(rmsle, round_)
		except Exception:
			rmsle	= -1.111
		
	table = pd.DataFrame()
	table.index =	['MAE', 'MAPE', 'SMAPE', 'RMSE', 'RMSLE']
	table['current'] =	[mae, mape, smape, rmse, rmsle]
	
	if previous is not None:
		if len(previous) != len(table.index):
			raise ValueError('list с метриками прошлой итерации имеет неподходящую длину')
		
		table['previous'] = previous
		if round_ is not None: table['previous'] = round(table['previous'], round_)
		
		table['diff'] = (table['current'] - table['previous']) * -1
		if round_ is not None: table['diff'] = round(table['diff'], round_)
		
		table['diff %'] = round(table['diff'] / table['current'] * 100, 2)
	
	print(table)
	
	if r:
		return tuple(table['current'])
