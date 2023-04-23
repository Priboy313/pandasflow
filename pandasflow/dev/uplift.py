
import pandas as pd

#Для задач классификации с таргетом 0-1

#Cумма 1 в топ-процент сортированной по предсказанию таблицы позиций делённая на сумму 1 для всей таблицы


def uplift(df, target, sort_score, pct):
  exited_all = df[target].sum()
  df = df.sort_values(sort_score, ascending=False)
  pct_len = round(len(df) * pct)
  exited_found = df.head(pct_len)[target].sum()

  return (exited_found / exited_all) / pct