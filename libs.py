import numpy as np 

a = np.array([1,2,3])
print(a.ndim)
print(a.size)

b = np.array([[1,2,3],[4,5,6]])
print(b.ndim)
print(b.size)

c = np.arange(10)
print(c)
c = np.arange(10).reshape(2,5)
print(c)

d = np.zeros((3))
print(d)

e = np.ones((2,3))
e = e * 9
print(e)