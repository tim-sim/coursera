import pandas
import matplotlib

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

# 1
print('\n1: male/female count')
male = data[data.Sex == 'male'].shape[0]
female = data[data.Sex == 'female'].shape[0]
print('male: {0}'.format(male))
print('female: {0}'.format(female))

# 2
print('\n2: survived percent')
survived = data[data.Survived == 1].shape[0]
total = data.shape[0]
print('survived: {:.0%}'.format(survived/total))

# 3
print('\n3: first class percent')