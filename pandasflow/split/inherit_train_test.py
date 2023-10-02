import pandasflow as pdf

import pandas as pd


def inherit_train_test(
	df: pd.DataFrame,
	train_size=0.6,
	round_=None):
	
	train_size_pice = int(len(df) * train_size)
	
	train = df.iloc[:train_size_pice]
	test = df.iloc[train_size_pice:]
	
	train_pie = len(train) / len(df)
	test_pie = len(test) / len(df)
	
	amount_len = len(train) + len(test)
	amount_prop = amount_len / len(df)
	
	if round_ not in [None, 'n', 'N'] and round_ > 0:
		train_pie = round(train_pie, round_)
		test_pie = round(test_pie, round_)
	
	table = pd.DataFrame({
		'count': [len(train),
				  len(test),
				  '',
				  amount_len,
				  len(df)],
		
		'pct': [train_pie,
				test_pie,
				'',
				amount_prop,
				''],
	})
	
	table.index = ['train',
				   'test',
				   '',
				   'Amount',
				   'InitData']
	print(table)
	
	return train, test




