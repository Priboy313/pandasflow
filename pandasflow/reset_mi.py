import pandas as pd

def reset_mi(table:pd.DataFrame, sep:str='_') -> pd.DataFrame:
	'''
	Change table columns name from
	 _____________________________
	|target       |target2        |
	|             |               |
	|count | mean | count |  mean |
	|------|------|-------|-------|
	
	to
	 _____________________________________________________________
	| target_count|   target_mean | target2_count |  target2_mean |
	|-------------|---------------|---------------|---------------|
	'''

	_table = table.copy()
	_table.columns = [sep.join(col).strip() for col in _table.columns.values]
	return _table