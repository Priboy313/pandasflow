
import numpy as np




def rmsle(y_true, y_pred):
	
	log_true = np.log1p(y_true)
	log_pred = np.log1p(y_pred)
	
	return np.sqrt(np.mean((log_true - log_pred) ** 2))