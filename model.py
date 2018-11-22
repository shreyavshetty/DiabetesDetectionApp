# importing library
import numpy as np
import pandas
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from keras.callbacks import ModelCheckpoint
# fix random seed for reproducibility
seed = 40
np.random.seed(seed)
# variable initialization
NB_EPOCHS = 1000
BATCH_SIZE = 16
DATASET_PATH = "diabetes.csv"
WEIGHTS_PATH = "pima-weights.best.hdf5"
# load dataset
dataframe = pandas.read_csv(DATASET_PATH, header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:8].astype(float)
Y = dataset[:,8]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
# creating model
def create_model():
	model = Sequential()
	# 1st layer: input_dim=8, 12 nodes, RELU
	model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
	# 2nd layer: 8 nodes, RELU
	model.add(Dense(8, init='uniform', activation='relu'))
	# output layer: dim=1, activation sigmoid
	model.add(Dense(1, init='uniform', activation='sigmoid' ))
	return model
# train model
def train():
	# compile the model
	model = create_model()
	model.compile(loss='binary_crossentropy',
		     optimizer='adam',
		     metrics=['accuracy'])
	# create checkpoints and store the best model
	ckpt_model = 'pima-weights.best.hdf5'
	checkpoint = ModelCheckpoint(ckpt_model,
			            monitor='val_acc',
			            verbose=1,
			            save_best_only=True,
			            mode='max')
	callbacks_list = [checkpoint]
	# fit the model
	history = model.fit(X_train,
		            y_train,
		            validation_data=(X_test, y_test),
		            nb_epoch=NB_EPOCHS,
		            batch_size=BATCH_SIZE,
		            callbacks=callbacks_list,
		            verbose=1)
# restore the model
def restore_model(test_values):
   # create the model
   model = create_model()
   # load model weights
   model.load_weights(WEIGHTS_PATH)
   # predict values
   predicted_values = model.predict(test_values)
   for value in predicted_values :
	if value > 0.5:
		value = 1
	else:
		value = 0
   return value

if __name__ == '__main__':
	print(restore_model(np.array([[10,125,70,26,115,31.1,0.205,41],], dtype=np.float32)))
