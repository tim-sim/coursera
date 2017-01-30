import pandas
import matplotlib
import re

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
print('survived: {:.2%}'.format(survived/total))

# 3
print('\n3: first class percent')
first_class = data[data.Pclass == 1].shape[0]
print('first class: {:.2%}'.format(first_class/total))

# 4
print('\n4: average age')
mean = data.Age.mean()
median = data.Age.median()
print('age mean: {:.2f}'.format(mean))
print('age median: {:.2f}'.format(median))

# #5
print('\n5: relatives correlation')
print('correlation between SilSp and Parch: {:.2f}'.format(data.corr(method='pearson').SibSp.Parch))

#6
def extractFemaleName(fullName):
	if (fullName.find('Miss') != -1):
		missResult = re.findall('[^,+]+,\s+Miss\.\s+(\w+)\s*.*', fullName)
		if (missResult != None  and len(missResult) > 0):
			return missResult[0]

	if (fullName.find('Mrs') != -1):
		mrsResult = re.findall('[^,+]+,\s+Mrs\.[^\()]*\((\w+)[^\)]*\)', fullName)
		if (mrsResult != None and len(mrsResult) > 0) :
			return mrsResult[0]
		else:
			mrsResult = re.findall('[^,+],\s+Mrs\.\s(\w+)\s*.*', fullName)
			if (mrsResult != None and len(mrsResult) > 0) :
				return mrsResult[0]

	return ''

print('\n6: most popular female name')

females = data[data.Sex == 'female']
print(females.Name.apply(lambda x: extractFemaleName(x)).value_counts().head())

