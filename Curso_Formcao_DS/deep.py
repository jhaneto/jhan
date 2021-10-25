from sklearn import datasets
from sklearn.model_selection import train_test_split
from yellowbrick.classifier import ConfusionMatrix
from keras.models import Sequential 
from keras.layers import Dense
from keras.utils import np_utils

base = datasets.load_iris()
