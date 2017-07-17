import numpy as np
import cv2
from sklearn import neighbors
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

class Classifier(object):
    def __init__(self, train_data, test_data, model):
        self.train_data = train_data
        self.test_data = test_data
        self.model = model
        self.res = []
        self.clf = 0

    def run(self):
        if self.model == 0:
            self.clf = self.neighbors(self.train_data, self.test_data)
            pass
        elif self.model == 1:
            self.clf = self.svm(self.train_data, self.test_data)
            pass
        elif self.model == 2:
            self.clf = self.randomforest(self.train_data, self.test_data)
            pass

    def neighbors(self, train_data, test_data):
        clf = neighbors.KNeighborsClassifier(n_neighbors=3)
        clf.fit(np.array(train_data[0]), np.array(train_data[1]))
        res = clf.predict(np.array(test_data[0]))
        # print res
        # print test_data[1]
        self.res = res
        return clf
        pass

    def svm(self, train_data, test_data):
        clf = svm.SVC(kernel='rbf')
        clf.fit(np.array(train_data[0]), np.array(train_data[1]))
        res = clf.predict(np.array(test_data[0]))
        # print res
        # print test_data[1]
        self.res = res
        return clf
        pass

    def randomforest(self, train_data, test_data):
        clf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
        clf.fit(np.array(train_data[0]), np.array(train_data[1]))
        res = clf.predict(np.array(test_data[0]))
        # print res
        # print test_data[1]
        self.res = res
        return clf

    pass