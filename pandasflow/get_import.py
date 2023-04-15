


def get_import():
	print('''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

plt.style.use("dark_background")
'''[1:])


if __name__ == "__main__":
	get_import()