import pandas as pd
import pandasflow as pdf

from sklearn.metrics import classification_report


def calc_class_from_score(score:pd.Series, thr=0.5, y_true:pd.Series | None = None) -> pd.Series:
	df = pd.DataFrame({'score': score, 'y_true': y_true})
	
	df['y_pred'] = (df['score'] > thr) * 1
	
	if y_true is not None:
		print(classification_report(df['y_true'], df['y_pred']))
	
	return df['y_pred']