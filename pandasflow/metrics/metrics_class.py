import pandas as pd
import pandasflow as pdf
from sklearn.metrics import confusion_matrix, roc_auc_score, average_precision_score



def metrics_class(y_true, y_pred, round_=2):
	tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
	roc_auc = round(roc_auc_score(y_true, y_pred), round_)
	precrec = round(average_precision_score(y_true, y_pred), round_)
	
	table = pd.DataFrame()
	table.index = ['ROC_AUC', 'PRECREC']
	table[' '] = [roc_auc, precrec]
	
	print(f'CONFMAT  {(tn, fp, fn, tp)}', table)
