import pickle
from sklearn import *
def mali(query):
  loaded_model = pickle.load(open('log.sav', 'rb'))
  result = loaded_model.predict(query)
  return result