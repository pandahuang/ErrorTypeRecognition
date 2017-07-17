import Tkinter
from Preprocess import Preprocessor
from Modeling import Classifier
import win32ui
import cv2
import numpy as np
import tkMessageBox

class IERApplication(object):
    def __init__(self):
        pass

    def Create(self):
        root = Tkinter.Tk()
        root.geometry('300x200')
        label1 = Tkinter.Label(root, text='ImageErrorRecognition', font=6)
        label1.pack()
        button1 = Tkinter.Button(root, text='Traing', height=4, width=8, command=self.TraingCallBack)
        button1.place(y=50, x=60)
        button1 = Tkinter.Button(root, text='Predict', height=4, width=8, command=self.PredictCallBack)
        button1.place(y=50, x=160)
        root.mainloop()

    def TraingCallBack(self):
        processor = Preprocessor.Processor()
        processor.run()
        classifier = Classifier.Classifier(processor.train_data, processor.test_data, 1)
        classifier.run()
        root1 = Tkinter.Tk()
        # root1.geometry('600x400')
        list1 = Tkinter.Listbox(root1, height=30)
        list2 = Tkinter.Listbox(root1, height=30)
        list1.insert(0, 'Results')
        list2.insert(0, 'Labels')
        for res, l, i in zip(classifier.res, classifier.test_data[1], range(len(classifier.res))):
            list1.insert(i+1, res)
            list2.insert(i+1, l)
        list1.pack(side='left')
        list2.pack(side='left')
        root1.mainloop()
        # return classifier.clf

    def PredictCallBack(self):
        dlg = win32ui.CreateFileDialog(1)
        dlg.SetOFNInitialDir('E:\Projects\SapImageRecognition\ImageErrorRecognition\RData\TData')
        dlg.DoModal()
        filename = dlg.GetPathName()
        print filename
        img = cv2.imread(filename, 1)
        processor = Preprocessor.Processor()
        processor.run()
        classifier = Classifier.Classifier(processor.train_data, processor.test_data, 1)
        classifier.run()
        res = classifier.clf.predict(np.array([processor.FeatureSelect(img)]))
        # print res
        tkMessageBox.showinfo('Message', 'your result is:' + str(res))
        pass

    pass

if __name__=='__main__':
    App = IERApplication()
    App.Create()