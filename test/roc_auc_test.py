import pandasflow as pdf
import pandas as pd
import numpy as np

t = pd.DataFrame({'y_true': [0]*990 + [1]*10})

np.random.seed(42)

t['y_score1'] = np.concatenate([np.random.uniform(0, 0.2, size=970),
                                np.random.uniform(0.8, 1, size=20),
                                np.random.uniform(0, 0.2, size=5),
                                np.random.uniform(0.8, 1, size=5)])

t['y_score2'] = np.concatenate([np.random.uniform(0, 0.2, size=900), #TN
                                np.random.uniform(0.8, 1, size=90),  #FP
                                np.random.uniform(0, 0.2, size=4),   #FN
                                np.random.uniform(0.8, 1, size=6)])  #TP

t['y_score3'] = np.concatenate([np.random.uniform(0, 0.2, size=850), #TN
                                np.random.uniform(0.8, 1, size=140), #FP
                                np.random.uniform(0, 0.2, size=2),   #FN
                                np.random.uniform(0.8, 1, size=8)])  #TP



# pdf.metrics.roc_auc(t['y_true'], score=t['y_score1'], plot=True)

# pdf.metrics.roc_auc(t['y_true'], score=[t['y_score1'], t['y_score2']])

pdf.metrics.roc_auc(t['y_true'], score=[t['y_score1'], t['y_score2'], t['y_score3']], plot=True)