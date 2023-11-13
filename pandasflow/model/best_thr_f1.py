import pandas as pd
import numpy as np
from sklearn.metrics import f1_score

from tqdm.auto import tqdm

def best_thr_f1(y_true:pd.Series, score:pd.Series, bins:int = 100, out:int=1, r:bool=False):
	scores = list(score.unique()) if type(score) is pd.Series else list(score)
	scores = [max(min(scores) - 0.000001, 0.000001)] + scores
	
	percentiles = np.arange(0, 100, 100/bins)
	thrs = np.percentile(scores, percentiles)
	
	df = pd.concat([y_true, score], axis=1)
	result = []
	
	for thr in tqdm(thrs):
		df['y_pred_thr'] = (df[score.name] > thr) * 1
		
		result.append(
			(thr, f1_score(df[y_true.name], df['y_pred_thr']))
		)
	
	result = pd.DataFrame(result, columns=['thr', 'f1'])
	result = result.sort_values(by='f1', ascending=False)
	
	result = result.head(min(out, len(result)))
	best_thr = result['thr'].loc[result.index[0]]
	
	print()
	print(result)
	
	if r: return round(best_thr, 6)




