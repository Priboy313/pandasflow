
import pandas as pd
from sklearn.model_selection import train_test_split

def train_test_split_(
	*arrays,
	test_size=None,
	train_size=0.8,
	random_state=42,
	shuffle=True,
	stratify=None,
	round_=None
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
	
	train, test = train_test_split(arrays[0], train_size=train_size, random_state=random_state, shuffle=shuffle, stratify=stratify)
	
	train_pie = len(train) / len(arrays[0])
	test_pie = len(test) / len(arrays[0])
	
	amount_len = len(train) + len(test)
	amount_prop = amount_len / len(arrays[0])
	
	if round_ not in [None, 'n', 'N'] and round_ > 0:
		train_pie = round(train_pie, round_)
		test_pie = round(test_pie, round_)
	
	table = pd.DataFrame({
		# count
		' ': [len(train), len(test), '', amount_len, len(arrays[0])],
		# proportion
		'  ': [train_pie, test_pie, '', amount_prop, '']})
	
	table.index = ['train', 'test', '---', 'Amount', 'InitData']
	print(table)
	
	if amount_prop != 1.0 or len(arrays[0]) != amount_len:
		print('---')
		print('Some data is droped')
	
	return train, test


if __name__ == "__main__":
	train, test = train_test_split_([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 3,
									train_size=0.6,
									round_=2)

''' return:

train     19  0.58
test      14  0.42
---
Amount    33   1.0
InitData  33
'''






