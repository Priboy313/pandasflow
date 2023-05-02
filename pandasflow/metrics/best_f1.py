
import pandas as pd
from sklearn.metrics import f1_score
from tqdm.notebook import tqdm


def best_f1(y_true:pd.Series, score:pd.Series, out:int=1, tqdm_:bool=True):
	thrs = list(score.unique())
	thrs = [max(min(thrs) - 0.000001, 0.000001)] + thrs
	
	df = pd.concat([y_true, score], axis=1)
	
	result = []
	
	if tqdm_: thrs = tqdm(thrs)
	
	for thr in thrs:
		df['y_pred_thr'] = (df[score.name] > thr) * 1
		result.append(
			(
				thr,
				f1_score(df[y_true.name], df['y_pred_thr'])
			)
		)
	
	result = pd.DataFrame(result, columns=['thr', 'f1'])
	result = result.sort_values(by='f1', ascending=False)
	
	print(result.head(min(out, len(result))))




