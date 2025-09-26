import numpy as np

# ## 📅 Week 3 – Array Operations & Bri neeoadcasting
# **Read/Watch**
# - [NumPy Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)  

# **Exercises**
# 1. Add `[1,2,3]` to every row of a 3×3 matrix.  

a = np.ones((3,3))

b = np.array([1, 2, 3])

print(a+b)

# 2. Compute the dot product of `[1,2,3]` and `[4,5,6]`.  

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])



print(np.sum(a*b))



# 3. Multiply a 3×3 matrix by a scalar (5).  

a = np.ones((3, 3))

print(a*5)

# 4. Normalize a random vector (length 5) so its sum = 1.  

r = np.random.randint(1, 10, 5)

print(r)

n = r/np.sum(r)

print(n)

# **Stretch Challenges**
# - Create a 5×5 matrix of random numbers, subtract the mean of each column.  



# - Compute cosine similarity between two random vectors using dot product.  

# ---