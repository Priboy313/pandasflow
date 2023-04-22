import pandasflow as pdf

import pandas as pd
from sklearn.model_selection import train_test_split

def train_valid_test(
	*arrays,
	test_size=None,
	train_size=0.6,
	random_state=42,
	shuffle=True,
	stratify=None,
	round_=None,
	target=None
):
	"""
	Split arrays or matrices into random train, valid and test subsets.

	Parameters
	----------
	*arrays : sequence of indexables with same length / shape[0]
		Allowed inputs are lists, numpy arrays, scipy-sparse
		matrices or pandas dataframes.
	
	test_size : float or int, default=None
		If float, should be between 0.0 and 1.0 and represent the proportion
		of the dataset to include in the test split. If int, represents the
		absolute number of test samples. If None, the value is set to the
		complement of the train size. If ``train_size`` is also None, it will
		be set to 0.25.
	
	train_size : float or int, default=None
		If float, should be between 0.0 and 1.0 and represent the
		proportion of the dataset to include in the train split. If
		int, represents the absolute number of train samples. If None,
		the value is automatically set to the complement of the test size.
	
	random_state : int, RandomState instance or None, default=None
		Controls the shuffling applied to the data before applying the split.
		Pass an int for reproducible output across multiple function calls.
		See :term:`Glossary <random_state>`.
	
	round_ : int, RandomState more 0 or None, default=None
		Print the proportion of each array with rounding.
		If None or 0 print all numbers after the decimal point
	
	target : None, str, pd.Series, default = None
		Add new columns with mean float proportion for tvt and df
	"""
	
	df = arrays[0]
	
	if test_size in [None, 0]:
		test_size_pice = ((1 - train_size) / 2) / (1 - train_size)
	else:
		test_size_pice = test_size / (1 - train_size)
	
	_strat_col = None
	_stratify = None
	if stratify != None: _strat_col = stratify
	
	if _strat_col != None: _stratify = df[_strat_col]
	train, valid_test = train_test_split(*arrays, train_size=train_size, random_state=random_state, shuffle=shuffle, stratify=_stratify)
	
	if _strat_col != None: _stratify = valid_test[_strat_col]
	valid, test = train_test_split(valid_test, test_size=test_size_pice, random_state=random_state, shuffle=shuffle, stratify=_stratify)
	
	train_pie = len(train) / len(df)
	valid_pie = len(valid) / len(df)
	test_pie = len(test) / len(df)
	
	amount_len = len(train) + len(valid) + len(test)
	amount_prop = amount_len / len(df)
	
	if round_ not in [None, 'n', 'N'] and round_ > 0:
		train_pie = round(train_pie, round_)
		valid_pie = round(valid_pie, round_)
		test_pie = round(test_pie, round_)
	
	table = pd.DataFrame({
		'count': [len(train),
				len(valid),
				len(test),
				'',
				amount_len,
				len(df)],
		
		'prop': [train_pie,
				 valid_pie,
				 test_pie,
				 '',
				 amount_prop,
				 ''],
		
		
	})
	
	if target != None:
		try:
			if type(target) is str:
				table[target] = [train[target].mean(),
							  valid[target].mean(),
							  test[target].mean(),
							  '',
							  '',
							  df[target].mean()]
			
			
			elif type(target) is list:
				for col in list(target):
					table[col] = [train[col].mean(),
									valid[col].mean(),
									test[col].mean(),
									'',
									'',
									df[col].mean()]
		except KeyError:
			raise KeyError(*target)
	
	table.index = ['train',
				   'valid',
				   'test',
				   '---',
				   'Amount',
				   'InitData']
	print(table)
	
	
	if amount_prop != 1.0 or len(df) != amount_len:
		print('---')
		print('Some data is droped')
	
	return train, valid, test