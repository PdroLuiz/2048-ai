import tensorflow as tf
from tensorflow.keras import layers, models, Input
from game import Game
from numpy import log2, exp

def normalize(arr_):
    arr = arr_.copy()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != 0:
                arr[i][j] = 1 / (1 + exp(-(log2(arr[i][j]))))
    return arr

class Model:

    def __init__(self):
        self.model = models.Sequential()
        self.model.add(layers.Conv1D(1, kernel_size=1, activation='relu', input_shape=(4,4), kernel_initializer='random_normal', bias_initializer='random_normal'))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(16, activation='relu', kernel_initializer='random_normal', bias_initializer='random_normal'))
        self.model.add(layers.Dense(16, activation='relu', kernel_initializer='random_normal', bias_initializer='random_normal'))
        self.model.add(layers.Dense(4, activation='softmax', kernel_initializer='random_normal', bias_initializer='random_normal'))
        self.model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
    
    def predict(self, state_):
        state = [normalize(state_.tolist())]
        prediction = self.model.predict(state)[0]
        return prediction.tolist().index(max(prediction))

    def LoadWeights(self, weights):
        self.model.set_weights(weights)

    def GetWeights(self):
        return self.model.get_weights()
