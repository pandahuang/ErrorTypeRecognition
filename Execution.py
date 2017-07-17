from Preprocess import Preprocessor
from Modeling import Classifier

if __name__=='__main__':
    processor = Preprocessor.Processor('E:\\Projects\\SapImageRecognition\\ImageErrorRecognition\\Data')
    processor.run()
    # print processor.imageDatalist[0]
    # processor.ShowImage(processor.imageDatalist[:2])

    classifier = Classifier.Classifier(processor.train_data, processor.test_data, 2)
    classifier.run()