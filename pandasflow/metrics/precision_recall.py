import pandasflow as pdf
import pandas as pd
from sklearn.metrics import precision_recall_curve, average_precision_score
from matplotlib import pyplot


def precision_recall(target, score, plot=False, round_=2):
	
	if type(score) == pd.Series or type(score) == list and len(score) == 1:
		score_ = score if type(score) == pd.Series else score[0]
		score_name = score_.name
		
		precision, recall, _ = precision_recall_curve(target, score_)
		pyplot.plot(recall, precision, marker='.', label=score_name)
		
		average = average_precision_score(target, score_)
		average = round(average, round_)
		print(f"{score_name} average precision: ", average)
	
	
	if type(score) == list and len(score) > 1:
		for sc in score:
			precision, recall, _ = precision_recall_curve(target, sc)
			pyplot.plot(recall, precision, marker='.', label=sc.name)
			
			average = average_precision_score(target, sc)
			average = round(average, round_)
			print(f"{sc.name} average precision: ", average)
			
	pyplot.xlabel('Recall')
	pyplot.ylabel('Precision')
	pyplot.legend()
	
	if plot:
		pyplot.show()