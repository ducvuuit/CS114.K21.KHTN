 # import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn import svm, datasets
from sklearn.metrics import classification_report
from DataLoader.simpledatasetloader import SimpleDatasetLoader
from preprocessing.simplepreprocessor import SimplePreprocessor
from imutils import paths

from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# grab the list of images that we’ll be describing
print("[INFO] loading images...")
imagePaths = list(paths.list_images('Dataset'))
#print(imagePaths)

# initialize the image preprocessor, load the dataset from disk,
# and reshape the data matrix
sp = SimplePreprocessor(32, 32)
sdl = SimpleDatasetLoader(preprocessors=[sp])
(data, labels) = sdl.load(imagePaths, verbose=500)
data = data.reshape((data.shape[0], 3072))

# show some information on memory consumption of the images
print("[INFO] features matrix: {:.1f}MB".format(
    data.nbytes / (1024 * 1000.0)))

# encode the labels as integers
le = LabelEncoder()
labels = le.fit_transform(labels)

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels,
    test_size=0.25, random_state=42)

# train and evaluate a svm classifier on the raw pixel intensities
print("[INFO] evaluating LDA classifier...")

#model = svm.SVC(kernel='rbf', C=1, gamma=0.5)
model = LinearDiscriminantAnalysis()

model.fit(trainX, trainY)
print(classification_report(testY, model.predict(testX),
    target_names=le.classes_))



