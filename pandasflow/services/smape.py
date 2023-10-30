import numpy as np




def smape(y_true, y_pred) -> float:
	return (1 / len(y_true)) * np.sum(np.abs(y_pred - y_true) / ((np.abs(y_true) + np.abs(y_pred)) / 2))
	
