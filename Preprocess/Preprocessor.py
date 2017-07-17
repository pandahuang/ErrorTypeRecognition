import cv2
import os
import numpy as np
import Tkinter

class Processor(object):
    def __init__(self):
        self.imagelist = []
        self.imageDatalist = []
        self.train_data = ([],[])
        self.test_data = ([],[])

    def ReadData(self, path):
        filelist = os.listdir(path)
        # print filelist
        for file in filelist:
            img = cv2.imread(os.path.join(path, file), 1)
            self.imagelist.append(img)
        return len(filelist)
        pass

    def WriteData(self, imglist):
        for img, i in zip(imglist, range(len(imglist))):
            filename = str(i) + '.png'
            cv2.imwrite(filename, img)
        pass

    def GetImgSize(self):
        for img in self.imagelist:
            # height , width , channels = img.shape
            print img.shape
            # print cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        pass

    def Thresholding(self, img):
        lower_red = np.array([0,0,230])
        upper_red = np.array([188,188,255])
        mask = cv2.inRange(img, lower_red, upper_red)
        return mask
        pass

    def FeatureSelect(self, img):
        # resize
        # INTER_NEAREST,INTER_LINEAR,INTER_AREA,INTER_CUBIC,INTER_LANCZOS4
        res = cv2.resize(img, (300, 300), interpolation=cv2.INTER_LINEAR)
        # clip
        cres = res[0:300]
        # threshold
        tres = self.Thresholding(cres)

        kernel = np.ones((5, 5), np.uint8)
        # closing
        # dres = cv2.morphologyEx(tres, cv2.MORPH_CLOSE, kernel)
        # dilation
        dres = cv2.dilate(tres, kernel, iterations=1)
        features = []
        # features.append(float(np.sum(dres[:100,:100]==255))/10000.0)
        # features.append(float(np.sum(dres[:100,100:200]==255))/10000.0)
        # features.append(float(np.sum(dres[:100, 200:]==255))/10000.0)
        # features.append(float(np.sum(dres[100:200, :100]==255))/10000.0)
        # features.append(float(np.sum(dres[100:200, 100:200]==255))/10000.0)
        # features.append(float(np.sum(dres[100:200, 200:]==255))/10000.0)
        # features.append(float(np.sum(dres[200:, :100]==255))/10000.0)
        # features.append(float(np.sum(dres[200:, 100:200] == 255))/10000.0)
        # features.append(float(np.sum(dres[200:, 200:] == 255))/10000.0)
        features.append(float(np.sum(dres[:125, :50] == 255)) / 6250.0)
        features.append(float(np.sum(dres[:125, 50:] == 255)) / 31250.0)
        # features.append(float(np.sum(dres[:125, 175:] == 255)) / 15625.0)
        features.append(float(np.sum(dres[125:, :] == 255)) / 52500.0)
        # if np.sum(dres[:135, 50:] == 255)!=0 and (float(np.sum(dres[:125, 50:] == 255))/float(np.sum(dres[:135, 50:] == 255))) >= 0.95:
        #     features.append(1.0)
        # else:
        #     features.append(0.0)
        if float(np.sum(dres[:, :] == 255)) != 0:
            if (float(np.sum(dres[:125, 50:] == 255)) / float(np.sum(dres[:, :] == 255))) >= 0.95:
                features.append(1.0)
            elif (float(np.sum(dres[:125, 50:] == 255)) / float(np.sum(dres[:, :] == 255))) >= 0.90 and (float(np.sum(dres[:135, 50:] == 255))/float(np.sum(dres[:, :] == 255))) >= 0.95:
                features.append(1.0)
            else:
                features.append(0.0)
        else:
            features.append(0.0)
        features.append(float(np.sum(dres[:, :] == 255)) / 90000.0)
        return np.array(features)
        pass

    def ShowImage(self, imglist):
        for img in imglist:
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def SetInput(self, len1, len2, len3, len4, len5, len6):
        for img in self.imageDatalist[:len1]:
            self.train_data[0].append(img)
            self.train_data[1].append(0)
        for img in self.imageDatalist[len1:(len1+len2)]:
            self.train_data[0].append(img)
            self.train_data[1].append(1)
        for img in self.imageDatalist[(len1+len2):(len1+len2+len3)]:
            self.train_data[0].append(img)
            self.train_data[1].append(1)
        for img in self.imageDatalist[(len1+len2+len3):(len1+len2+len3+len4)]:
            self.test_data[0].append(img)
            self.test_data[1].append(0)
        for img in self.imageDatalist[(len1+len2+len3+len4):(len1+len2+len3+len4+len5)]:
            self.test_data[0].append(img)
            self.test_data[1].append(1)
        for img in self.imageDatalist[(len1+len2+len3+len4+len5):]:
            self.test_data[0].append(img)
            self.test_data[1].append(1)
        pass

    def run(self):
        #read data
        len1 = self.ReadData('E:\\Projects\\SapImageRecognition\\ImageErrorRecognition\\Data\\0')
        len2 = self.ReadData('E:\\Projects\\SapImageRecognition\\ImageErrorRecognition\\Data\\1')
        len3 = self.ReadData('E:\\Projects\\SapImageRecognition\\ImageErrorRecognition\\Data\\2')
        len4 = self.ReadData('E:\\Projects\\SapImageRecognition\\ImageErrorRecognition\\Data\\T0')
        len5 = self.ReadData('E:\\Projects\\SapImageRecognition\\ImageErrorRecognition\\Data\\T1')
        len6 = self.ReadData('E:\\Projects\\SapImageRecognition\\ImageErrorRecognition\\Data\\T2')
        for img in self.imagelist:
            nres = self.FeatureSelect(img)
            self.imageDatalist.append(nres)
        self.SetInput(len1, len2, len3, len4, len5, len6)
    pass

if __name__ == '__main__':
    processor = Processor()
    processor.run()
    # print processor.imagelist[0]
    # print processor.imageDatalist[:]
    # processor.ShowImage(processor.imagelist[:])
    # processor.WriteData(processor.imageDatalist)