import matplotlib.pyplot as mpl
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.model_selection import train_test_split

data = [[[(i + j)/100] for i in range(5)] for j in range(100)]
target = [(i + 5)/100 for i in range(100)]
data = np.array(data, dtype=float)
target = np.array(target, dtype=float)
print(data.shape)
print(target.shape)

x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=4)

model = Sequential()
model.add(LSTM(1, batch_input_shape=(None, 5, 1), return_sequences=False))
model.compile(loss="mean_absolute_error", optimizer='adam', metrics=['accuracy'])
model.summary()
history = model.fit(x_train, y_train, epochs=3000, validation_data=(x_test, y_test))
results = model.predict(x_test)
mpl.figure()
mpl.scatter(range(20), results, c='r')
mpl.scatter(range(20), y_test, c='g')
mpl.figure()
mpl.plot(history.history['loss'])
mpl.show()
