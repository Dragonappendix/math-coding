import numpy as np

# Create an array of numbers 1–20. Slice out only the even numbers.

# a = np.array(np.arange(1, 21))

# print(a)

# print(a[a%2 == 0])


# # Given arr = np.arange(25).reshape(5,5), extract the middle 3×3 submatrix.

# b = np.arange(25).reshape(5, 5)

# print(b)

# # print(b[1:4, 1:4])

# # Replace all numbers > 10 in a random 4×4 matrix with -1.

# c = np.random.randint(1, 21, (4, 4))

# c[c>10] = -1

# # print(c)

# # Create a diagonal matrix with values [5,10,15,20].

# i = np.identity(4, int)

# j = np.array([5, 10, 15, 20])

# # print(i*j)


# Stretch Problems:
# Flip a 5×5 matrix upside down and then left-to-right (array flipping).

k = np.random.randint(0, 20, (5, 5))

print(k)

print(np.flip(k, axis=0))

print(np.flip(k, axis=1))

# Create a checkerboard pattern (alternating 0 and 1 in an 8×8 array).

z = (np.arange(72))


z[z % 2 != 0] = 1


z[z % 2 == 0] = 0

print(z)

z = z.reshape((8,9))

print(z)

z = np.delete(z, 8, 1)

print(z)