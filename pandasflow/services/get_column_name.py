
import pandasflow as pdf
import pandas as pd


def get_column_name(col:pd.Series) -> str:
	# print(type(col))
	# print(type(col) == pd.Series)
	return str(col.name)