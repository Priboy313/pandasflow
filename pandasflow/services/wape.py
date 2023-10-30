
import numpy as np



def wape(y_true, y_pred, weights):
	if len(y_true) != len(y_pred) or len(y_pred) != len(weights):
		raise ValueError('Размеры массивов не совпадают!')
	
	errors = np.abs((y_true - y_pred) / y_true)
	wape = np.average(errors, weights=weights)
	
	return wape