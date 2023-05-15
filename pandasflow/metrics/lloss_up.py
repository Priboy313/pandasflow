
import pandas as pd
from sklearn.metrics import log_loss

# Для задач классификации с таргетом 0-1
# Сравнение человеческого baseline с машинным предиктом
# Возвращает две метрики:
# log_loss - чем меньше, тем лучше
# uplift - чем больше, тем лучше


def def_baseline(target):
	base = target.sum()
	base_pct = base / len(target)
	
	return base, base_pct


def _uplift(target, sort_score, pct, baseline=None):
	base, base_pct = def_baseline(target)
	if baseline != None:
		print('baseline is not None, but unknown')
	
	_df = sort_score.sort_values(ascending=False)
	pct_len = round(len(target) * pct)
	base_found = _df.head(pct_len).sum()

	return base_pct, ((base_found / base) / pct)


def lloss_up(target, score, pct=0.2, baseline=None):
	'''Для задач классификации с таргетом 0-1
	Сравнение человеческого baseline с машинным предиктом
	Возвращает две метрики:
	
	log_loss - чем меньше, тем лучше
	uplift - чем больше, тем лучше
	
	Parameters
	----------
	target : pd.Series
		Название колонки с искомым значением
	
	score : pd.Series
		Название колонки с предиктом машинного обучение
		Результат работы, который и сравниваем
	
	pct : float, default = 0.2
		Процент колонки предикта, из которого и считаем uplift
	
	baseline : None, def, int, float. default = None
		Худший вариант предсказания, базово - среднееарифметическое
		Лучше не трогать и оно посчитается от target
	'''

	lloss = log_loss(target, score)
	base, up = _uplift(target, score, pct, baseline=baseline)
	
	table = pd.DataFrame()
	table.index = ['baseline', 'log_loss', 'uplift']
	table[' '] = [base, lloss, up]
	
	print(table)
	print()
	return base, lloss, up