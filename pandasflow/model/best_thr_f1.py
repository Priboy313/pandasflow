import pandas as pd
from sklearn.metrics import f1_score

from tqdm.auto import tqdm

def best_thr_f1(y_true:pd.Series, score:pd.Series, out:int=1):
	thrs = list(score.unique())
	thrs = [max(min(thrs) - 0.000001, 0.000001)] + thrs
	
	df = pd.concat([y_true, score], axis=1)
	
	result = []
	
	for thr in tqdm(thrs):
		df['y_pred_thr'] = (df[score.name] > thr) * 1
		result.append(
			(
				thr,
				f1_score(df[y_true.name], df['y_pred_thr'])
			)
		)
	
	result = pd.DataFrame(result, columns=['thr', 'f1'])
	result = result.sort_values(by='f1', ascending=False)
	
	result = result.head(min(out, len(result)))
	best_thr = result['thr'].loc[result.index[0]]
	
	print()
	print(result)
	
	return round(best_thr, 6)




