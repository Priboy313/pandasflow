import pandasflow as pdf
import pandas as pd
import numpy as np



t = pd.DataFrame()
t['y_true'] = [0]*990 + [1]*10
t['y_pred'] = [0]*990 + [1]*10

pdf.metrics.metrics_class(t['y_true'], t['y_pred'])