import numpy as np


a = np.array([1, 2, 3, 4, 5])
b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
# print(a)
# print(b)

# print(a.dtype)
# print(b.dtype)

# print(a.itemsize)
# print(b.itemsize)


c = np.array([[5, 3, 5, 2, 6], [6, 3, 2, 6, 8]])\

print(c)

print(c[0, 3])

# Exercises

d = np.array([1, 2, 3, 4, 5])

e = d*d

print(e)

f = np.array([[1, 2, 3], [4, 5, 6]])

print(f[1])


g = np.random.randint(50, size=10)
print(g)
print(np.max(g), int(np.mean(g)), np.min(g))

h = np.identity(3)
i = np.array([1, 2, 3])

print(h*i)

j = np.zeros((5, 5))
j[0] = j[4] = 1
j[:, 0] = j[:, 4] = 1
j [2, 2] = 9

h = np.ones((5, 5))
z = np.zeros((3, 3))
z[1, 1] = 9

h[1:4, 1:4] = z

# print(j)
# print(h)

i = np.full((1, 100), np.arange(1, 101))
print(i)

j = i.reshape((10,10))
print(j)