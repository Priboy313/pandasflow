


def get_import():
	print('''
! pip install catboost
! pip install phik
! pip install shap

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import phik

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from sklearn.metrics import log_loss

plt.style.use("dark_background")
'''[1:])


if __name__ == "__main__":
	get_import()