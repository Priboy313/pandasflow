


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

import warnings
warnings.filterwarnings("ignore", "FutureWarnings")

plt.style.use("dark_background")
'''[1:])


if __name__ == "__main__":
	get_import()