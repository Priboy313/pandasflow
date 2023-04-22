import pandasflow as pdf




print('tvt:')
train, valid, test = pdf.split.train_valid_test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 3, round_=2)

'''return:

train     19  0.58
valid      7  0.21
test       7  0.21
---
Amount    33   1.0
InitData  33
'''



print('\ntt:')

train, test = pdf.split.train_test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 3, train_size=0.6, round_=2)

''' return:

train     19  0.58
test      14  0.42
---
Amount    33   1.0
InitData  33
'''