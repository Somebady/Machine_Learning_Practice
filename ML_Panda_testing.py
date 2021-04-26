# pandas

import numpy as np
import pandas as pd
from numpy.random import randn
# 1.Series
np.random.seed(101)
# df = pd.DataFrame(randn(5, 4), ['A', 'A', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
# print(df.loc['A'])
data = pd.read_csv(
    f"C:/Users/akshason/Desktop/bin/AAM_FAILED_TRX_FOR_ALL_INSTANCE_D_1.csv", skipinitialspace=True, encoding='utf-8', dtype=object)
# print(data)
# # print(data)
data = data[['CIRCLE', 'INSTANCE', 'SERVICE_TYPE', 'SUBSCRIBER', 'ORDER_NO', 'MSISDN',
             'STATUS', 'TRX_NO', 'ERROR_CODE', 'REMARKS']]
data['REPROCESS_STATUS'] = 'P'

for i in data:
    data[i] = data[i].str.replace('\W', '')
# print(data[data['INSTANCE'] == 'P2'])
# print(data[['INSTANCE', 'CIRCLE']])
index = list(zip(data['INSTANCE'], data['CIRCLE']))
index = pd.MultiIndex.from_tuples(index)
# print(index)
# df = pd.DataFrame(randn(44, 2), index, ['INSTANCE', 'CIRCLE'])
# print(df)
print(data.groupby('INSTANCE').describe().transpose()['P1'])
