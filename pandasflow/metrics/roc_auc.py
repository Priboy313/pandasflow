import pandasflow as pdf
import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score
from matplotlib import pyplot


def roc_auc(y_true, y_pred, plot=True, marker='', round_=2):
	if type(y_pred) == pd.Series:
		y_pred_ = []
		y_pred_.append(y_pred)
	else:
		y_pred_ = y_pred
	
	for sc in y_pred_:
		fpr, tpr, _ = roc_curve(y_true, sc)
		pyplot.plot(fpr, tpr, marker=marker, label=sc.name)
		
		auc = roc_auc_score(y_true, sc)
		auc = round(auc, round_)
		print(f"{sc.name}: ", auc)
	
	pyplot.xlabel('False Positive Rate')
	pyplot.ylabel('True Positive Rate')
	pyplot.legend(loc = 'lower right')
	
	if plot:
		pyplot.show()