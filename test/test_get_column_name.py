import pandasflow as pdf
from test import df
import pandas as pd


from pandasflow.services import get_column_name


print(get_column_name(df['Exited']))