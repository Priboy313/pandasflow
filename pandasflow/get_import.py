


def get_import():
	print('''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import phik
import shap

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from sklearn.metrics import log_loss

plt.style.use("dark_background")
shap.initjs()
'''[1:])


if __name__ == "__main__":
	get_import()