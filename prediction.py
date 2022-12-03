import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data.csv')


def loss_function(m, b, points):
	total_error = 0
	for i in range(len(points)):
		x = points.iloc[i].price
		y = points.iloc[i].km
		total_error += (y - (m * x + b)) ** 2
	total_error / float(len(points))


def gradient_descent(m_now, b_now, points, L):
	m_gradient = 0
	b_gradient = 0

	n = len(points)

	for i in range(n):
		x = points.iloc[i].price
		y = points.iloc[i].km


		m_gradient += -(2 / n) * x * (y - (m_now * x + b_now))
		b_gradient += -(2 / n) * (y - (m_now * x + b_now))

	retm = m_now - m_gradient * L
	retb = b_now - b_gradient * L
	return retm, retb

m = 0
b = 0
L = 0.0001
epochs = 300

for i in range(epochs):
	if i % 50 == 0:
		print(f"Epoch: {i}")
	m, b = gradient_descent(m, b, data, L)

print(m, b)

print("Range of numpy double:", np.finfo(np.double).min, np.finfo(np.double).max)
plt.scatter(data.price, data.km, color="black")
plt.plot(list(range(10, 10)), [m * x + b for x in range(10, 10)], color="green")
plt.show()

