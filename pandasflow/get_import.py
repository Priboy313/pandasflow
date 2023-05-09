


def get_import():
	print('''
import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import phik
import shap

from catboost import CatBoostClassifier, CatBoostRegressor
from catboost import Pool

plt.style.use("dark_background")
shap.initjs()
'''[1:])


if __name__ == "__main__":
	get_import()