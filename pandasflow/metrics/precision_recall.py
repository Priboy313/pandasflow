import pandasflow as pdf
import pandas as pd
from sklearn.metrics import precision_recall_curve, average_precision_score
from matplotlib import pyplot


def precision_recall(target, score, plot=False, marker='', round_=2):
	if type(score) == pd.Series:
		score_ = []
		score_.append(score)
	else:
		score_ = score
	
	for sc in score_:
		precision, recall, _ = precision_recall_curve(target, sc)
		pyplot.plot(recall, precision, marker=marker, label=sc.name)
		
		average = average_precision_score(target, sc)
		average = round(average, round_)
		print(f"{sc.name} average precision: ", average)
		
	pyplot.xlabel('Recall')
	pyplot.ylabel('Precision')
	pyplot.legend()
	
	if plot:
		pyplot.show()