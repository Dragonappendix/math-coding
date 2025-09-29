import numpy as np

# **Exercises**
# 1. Create `A = [[2,1],[1,2]]`. Compute its determinant and inverse.  
# 
# # 
# A = np.array([2, 1, 1, 2]).reshape((2, 2))

# print(A)

# print(np.linalg.det(A))

# print(np.linalg.inv(A))
# # 2. Solve the system:  

# 2x + y = 5
# x + 2y = 6

# using `np.linalg.solve`.  


# A = np.array([2, 1, 1, 2]).reshape((2, 2))

# print(A)

# B = np.array([5, 6])

# print(B)
# print(np.linalg.solve(A, B))


# 3. Compute eigenvalues and eigenvectors of `[[4,2],[2,3]]`.  

C = np.array([[4, 2], [2, 3]])

print(np.linalg.eig(C))

c_eigenvals, c_eigenvects = np.linalg.eig(C)[0], np.linalg.eig(C)[1]



# 4. Verify that `A @ v = λv` holds for one eigenpair.  


print(C@c_eigenvects[:, 0])
print(c_eigenvals[0]*c_eigenvects[:, 0])

# **Stretch Challenges**
# - Create a random symmetric 3×3 matrix. Compute its eigenvalues and confirm they’re real.  
# - Compute the rank of a random 4×4 matrix. Explain what it means.  

# ---