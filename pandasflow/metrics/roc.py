import pandasflow as pdf
import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score
from matplotlib import pyplot


def roc(target, score, plot=False, marker='', round_=2):
	if type(score) == pd.Series or type(score) == list and len(score) == 1:
		score_ = score if type(score) == pd.Series else score[0]
		score_name = score_.name
		
		fpr, tpr, _ = roc_curve(target, score_)
		pyplot.plot(fpr, tpr, marker=marker, label=score_name)
		
		auc = roc_auc_score(target, score_)
		auc = round(auc, round_)
		print(f"{score_name} auc: ", auc)
	
	if type(score) == list and len(score) > 1:
		for sc in score:
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