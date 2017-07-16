from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib

clf = joblib.load('model.dat')
digits = datasets.load_digits()

testDatas = digits.data[-1:]
testLabels = clf.predict(testDatas)

print('Result = %i' % testLabels)
print('label = %i' % digits.target[-1:])
