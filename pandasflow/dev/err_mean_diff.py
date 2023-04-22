import pandasflow as pdf
import seaborn as sns


def err_mean_diff(df, index_col, dark=True, color='red'):
	CM = sns.dark_palette(color, as_cmap=True) if dark else sns.light_palette(color, as_cmap=True)
	
	t = df.groupby(index_col)[['error', 'error_abs']].agg(['count', 'mean'])
	t = pdf.reset_mi(t)
	t = t.drop(['error_abs_count'], axis=1)
	t = t.rename({'error_count': 'count'}, axis=1)
	t['error_mean_diff'] = t['error_abs_mean'] - df['error_abs'].mean()
	t = t.rename({'error_count': 'count'}, axis=1)
	t['test_mean_error'] = df['error_abs'].mean()
	
	return t.style.background_gradient(cmap=CM, subset=['error_mean_diff'])











