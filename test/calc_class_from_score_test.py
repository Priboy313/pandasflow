import pandasflow as pdf
import pandas as pd


df = pd.read_csv('test_data.csv')

train, valid, test = pdf.split.train_valid_test(df, target='Exited', stratify='Exited')
train['age_group'] = pd.cut(train['Age'], [0, 31, 35, 40, 45, float('inf')])
model = train.groupby(['NumOfProducts', 'age_group'])['Exited'].mean().reset_index()
model = model.rename({'Exited': 'score_prod_age'}, axis=1)
train = train.merge(model, how='left', on=['NumOfProducts', 'age_group'])
test['age_group'] = pd.cut(test['Age'], [0, 31, 35, 40, 45, float('inf')])
test = test.merge(model, how='left', on=['NumOfProducts', 'age_group'])
test['y_pred'] = (test['score_prod_age'] > 0.5) * 1

print(test['Exited'])

thr = pdf.model.best_thr_f1(test['Exited'], test['score_prod_age'])
print()
print(thr)
print('\nv1')
a = pdf.model.calc_class_from_score(test['score_prod_age'], y_true=test['Exited'])
print('\nv2')
a = pdf.model.calc_class_from_score(test['score_prod_age'], thr, y_true=test['Exited'])

