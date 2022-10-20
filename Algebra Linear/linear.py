import numpy as np

A = np.array([[1, 1, 1, 1, 1, 1],
              [10, 2, 3, 4, 5, 1],
              [1, 1, 2, 4, 1, 1],
              [2, 7, 1, 1, 10, 2],
              [3, 1, 1, 1, 20, 1],
              [2, 6, 1, 4, 5, 1]])
B = np.array([[21],
              [70],
              [36],
              [85],
              [118],
              [64]])

A_I = np.linalg.inv(A)


X = np.dot(A_I, B)
print("{}".format(A))
print('')

print("{}".format(A_I))
print('')

print("{}".format(B))
print('')

print("{}".format(X))
print('')
