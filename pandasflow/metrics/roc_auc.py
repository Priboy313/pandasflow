import pandasflow as pdf
import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score
from matplotlib import pyplot


def roc_auc(target, score, plot=False, marker='', round_=2):
	if type(score) == pd.Series:
		score_ = []
		score_.append(score)
	else:
		score_ = score
	
	for sc in score_:
		fpr, tpr, _ = roc_curve(target, sc)
		pyplot.plot(fpr, tpr, marker=marker, label=sc.name)
		
		auc = roc_auc_score(target, sc)
		auc = round(auc, round_)
		print(f"{sc.name} auc: ", auc)
	
	pyplot.xlabel('False Positive Rate')
	pyplot.ylabel('True Positive Rate')
	pyplot.legend(loc = 'lower right')
	
	if plot:
		pyplot.show()