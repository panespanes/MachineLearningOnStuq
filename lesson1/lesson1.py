from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib
import matplotlib.pyplot as plt

digits = datasets.load_digits();
print('load digits')

#获取分类器
clf = svm.SVC(gamma=0.001, C=1.0)

#0-倒数第二个作为训练集
trainData = digits.data[:-4]
trainLabel = digits.target[:-4]

#训练
clf.fit(trainData, trainLabel)

# 保存模型
joblib.dump(clf, 'model.dat')
testData = digits.data[-4:]
#testLabel = digits.data[-1:]

predict = clf.predict(testData)
print('result = ',predict)

testLabel = digits.target[-4:]
print('label = ', testLabel)

images = digits.images[-4:]
for index in range(len(images)):
    plt.subplot(1, 4, index+1)
    plt.axis('off')
    plt.imshow(images[index], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title('%i' % index)
    # plt.show()

plt.show()