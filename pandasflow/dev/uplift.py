
import pandas as pd
from sklearn.metrics import log_loss

#Для задач классификации с таргетом 0-1

#Cумма 1 в топ-процент сортированной по предсказанию таблицы позиций делённая на сумму 1 для всей таблицы


def uplift(df, target, sort_score, pct, baseline=None):
	_baseline = df[target].sum()
	_df = df.sort_values(sort_score, ascending=False)
	pct_len = round(len(df) * pct)
	base_found = _df.head(pct_len)[target].sum()

	return (base_found / _baseline) / pct




def print_metrics(df, target, score):
	table = pd.DataFrame()
	table.index = ['lloss', 'uplift']
	table[' '] = [log_loss(df[target], df[score]),
	              uplift(df, target, score, .2)]
	print(table)