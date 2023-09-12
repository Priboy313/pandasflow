import pandasflow as pdf
import pandas as pd
from sklearn.metrics import precision_recall_curve, average_precision_score
from matplotlib import pyplot


def precision_recall(y_true, y_pred, plot=True, marker='', round_=2):
	if type(y_pred) == pd.Series:
		y_pred_ = []
		y_pred_.append(y_pred)
	else:
		y_pred_ = y_pred
	
	for sc in y_pred_:
		precision, recall, _ = precision_recall_curve(y_true, sc)
		pyplot.plot(recall, precision, marker=marker, label=sc.name)
		
		average = average_precision_score(y_true, sc)
		average = round(average, round_)
		print(f"{sc.name} average precision: ", average)
		
	pyplot.xlabel('Recall')
	pyplot.ylabel('Precision')
	pyplot.legend()
	
	if plot:
		pyplot.show()