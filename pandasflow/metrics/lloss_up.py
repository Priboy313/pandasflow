
import pandas as pd
from sklearn.metrics import log_loss

# Для задач классификации с таргетом 0-1
# Сравнение человеческого baseline с машинным предиктом
# Возвращает две метрики:
# log_loss - чем меньше, тем лучше
# uplift - чем больше, тем лучше


def def_baseline(df, target):
	base = df[target].sum()
	base_pct = df[target].sum() / len(df)
	
	return base, base_pct


def _uplift(df, target, sort_score, pct, baseline=None):
	base, base_pct = def_baseline(df, target)
	if baseline != None:
		print('baseline is not None, but unknown')
	
	_df = df.sort_values(sort_score, ascending=False)
	pct_len = round(len(df) * pct)
	base_found = _df.head(pct_len)[target].sum()

	return base_pct, ((base_found / base) / pct)


def lloss_up(df, target, score, pct=0.2, baseline=None):
	'''Для задач классификации с таргетом 0-1
	Сравнение человеческого baseline с машинным предиктом
	Возвращает две метрики:
	
	log_loss - чем меньше, тем лучше
	uplift - чем больше, тем лучше
	
	Parameters
	----------
	df : pd.DataFrame
		Таблица данных
	
	target : str
		Название колонки с искомым значением
	
	score : str
		Название колонки с предиктом машинного обучение
		Результат работы, который и сравниваем
	
	pct : float, default = 0.2
		Процент колонки предикта, из которого и считаем uplift
	
	baseline : None, def, int, float. default = None
		Худший вариант предсказания, базово - среднееарифметическое
		Лучше не трогать и оно посчитается от target
	'''

	lloss = log_loss(df[target], df[score])
	base, up = _uplift(df, target, score, pct, baseline=baseline)
	
	table = pd.DataFrame()
	table.index = ['base', 'lloss', 'uplift']
	table[' '] = [base, lloss, up]
	
	print(table)
	
	return base, lloss, up