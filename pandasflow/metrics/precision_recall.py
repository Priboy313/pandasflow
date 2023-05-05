import pandasflow as pdf
import pandas as pd
from sklearn.metrics import precision_recall_curve, average_precision_score
from matplotlib import pyplot


def precision_recall(df, target, score, plot=False, round_=2):
	
	if type(score) == str or type(score) == list and len(score) == 1:
		precision, recall, _ = precision_recall_curve(df[target], df[score])
		pyplot.plot(recall, precision, marker='.', label=score[0] if type(score) == list else score)
		average = average_precision_score(df[target], df[score])
		average = round(average, round_)
		print(f"{score[0] if type(score) == list else score} average precision: ", average)
	
	
	if type(score) == list and len(score) > 1:
		for sc in score:
			precision, recall, _ = precision_recall_curve(df[target], df[sc])
			pyplot.plot(recall, precision, marker='.', label=sc)
			average = average_precision_score(df[target], df[sc])
			average = round(average, round_)
			print(f"{sc} average precision: ", average)
	
	if plot:
		pyplot.xlabel('Recall')
		pyplot.ylabel('Precision')
		pyplot.legend()
		pyplot.show()