import pandasflow as pdf
from pandasflow.services import get_column_name

import pandas as pd
from sklearn.model_selection import train_test_split

def train_test(
	*arrays,
	test_size=None,
	train_size=0.8,
	random_state=42,
	shuffle=True,
	stratify=None,
	round_=None,
	target=None
):
	"""
	Split arrays or matrices into random train and test subsets.

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
	"""
	
	df = arrays[0]
	
	_stratify = stratify
	if stratify != None:
		if type(stratify) == pd.Series:
			_stratify = df[get_column_name(stratify)]
		elif type(stratify) == str:
			_stratify = df[stratify]
	
	train, test = train_test_split(*arrays, train_size=train_size, random_state=random_state, shuffle=shuffle, stratify=_stratify)
	
	train_pie = len(train) / len(arrays[0])
	test_pie = len(test) / len(arrays[0])
	
	amount_len = len(train) + len(test)
	amount_prop = amount_len / len(arrays[0])
	
	if round_ not in [None, 'n', 'N'] and round_ > 0:
		train_pie = round(train_pie, round_)
		test_pie = round(test_pie, round_)
	
	table = pd.DataFrame({
		'count': [len(train),
			  len(test),
			  '',
			  amount_len,
			  len(arrays[0])],
		
		'prop': [train_pie,
			   test_pie,
			   '',
			   amount_prop,
			   '']
	})
	
	table.index = ['train',
				   'test',
				   '---',
				   'Amount',
				   'InitData']
	
	if target != None:
		try:
			table[target] = [train[target].mean(),
							test[target].mean(),
							'',
							'',
							df[target].mean()]
		except KeyError:
			raise KeyError(target)
	
	print(table)
	
	if amount_prop != 1.0 or len(arrays[0]) != amount_len:
		print('---')
		print('Some data is droped')
	
	return train, test





