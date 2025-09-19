# 📘 NumPy + Matrices Study Plan
(via ChatGPT) 
A progressive roadmap for learning **NumPy**, **matrix operations**, and **regression** in Python.  
The plan builds from basic arrays → matrix algebra → regression from scratch → applied datasets.  
Includes **core exercises** and **stretch challenges**.

---

## 📅 Week 1 – NumPy Basics & Arrays
**Read/Watch**
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)  
- [Corey Schafer – NumPy Tutorial (YouTube)](https://www.youtube.com/watch?v=QUT1VHiLmmI)  

**Exercises**
1. Create a 1D NumPy array `[1,2,3,4,5]`. Square each element.  
2. Make a 2D array `[[1,2,3],[4,5,6]]`. Extract the second row.  
3. Generate an array of 10 random integers (0–50). Find the max, min, and mean.  
4. Create a 3×3 identity matrix. Multiply it by `[1,2,3]ᵀ`.  

**Stretch Challenges**
- Create a 10×10 random matrix. Replace all values below 0.5 with 0, above 0.5 with 1.  
- Create an array from 1–100 and reshape into 10×10. Find row and column sums.  

---

## 📅 Week 2 – Array Indexing & Slicing
**Read/Watch**
- [NumPy Indexing Documentation](https://numpy.org/doc/stable/reference/arrays.indexing.html)  
- [Keith Galli – NumPy Tutorial (YouTube)](https://www.youtube.com/watch?v=GB9ByFAIAH4)  

**Exercises**
1. Create an array of numbers 1–20. Slice out only the even numbers.  
2. Given `arr = np.arange(25).reshape(5,5)`, extract the middle 3×3 submatrix.  
3. Replace all numbers > 10 in a random 4×4 matrix with `-1`.  
4. Create a diagonal matrix with values `[5,10,15,20]`.  

**Stretch Challenges**
- Flip a 5×5 matrix upside down and then left-to-right.  
- Create an 8×8 checkerboard pattern (alternating 0s and 1s).  

---

## 📅 Week 3 – Array Operations & Broadcasting
**Read/Watch**
- [NumPy Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)  

**Exercises**
1. Add `[1,2,3]` to every row of a 3×3 matrix.  
2. Compute the dot product of `[1,2,3]` and `[4,5,6]`.  
3. Multiply a 3×3 matrix by a scalar (5).  
4. Normalize a random vector (length 5) so its sum = 1.  

**Stretch Challenges**
- Create a 5×5 matrix of random numbers, subtract the mean of each column.  
- Compute cosine similarity between two random vectors using dot product.  

---

## 📅 Week 4 – Linear Algebra Foundations
**Read/Watch**
- [NumPy Linear Algebra Docs](https://numpy.org/doc/stable/reference/routines.linalg.html)  
- [StatQuest – Eigenvalues and Eigenvectors (YouTube)](https://www.youtube.com/watch?v=PFDu9oVAE-g)  

**Exercises**
1. Create `A = [[2,1],[1,2]]`. Compute its determinant and inverse.  
2. Solve the system:  

2x + y = 5
x + 2y = 6

using `np.linalg.solve`.  
3. Compute eigenvalues and eigenvectors of `[[4,2],[2,3]]`.  
4. Verify that `A @ v = λv` holds for one eigenpair.  

**Stretch Challenges**
- Create a random symmetric 3×3 matrix. Compute its eigenvalues and confirm they’re real.  
- Compute the rank of a random 4×4 matrix. Explain what it means.  

---

## 📅 Week 5 – Regression with Matrices
**Read/Watch**
- [StatQuest – Least Squares Regression (YouTube)](https://www.youtube.com/watch?v=nk2CQITm_eo)  

**Exercises**
1. Generate `x = [1,2,3,4,5]`, `y = [2,4,6,8,10]`. Fit a line using `np.polyfit`.  
2. Implement linear regression manually using the normal equation:  

β = (XᵀX)⁻¹Xᵀy

3. Compare your coefficients with `np.polyfit`.  
4. Extend to quadratic regression (`y = a + bx + cx²`).  
5. Plot regression line against data (matplotlib).  

**Stretch Challenges**
- Implement cubic regression manually (β with x, x², x³).  
- Generate noisy linear data (`y = 3x + 2 + noise`). Fit a line and compare to true slope/intercept.  

---

## 📅 Week 6 – Applied Dataset Practice
**Datasets**
- [Fish Market Dataset](https://www.kaggle.com/datasets/vipullrathod/fish-market) – species, weight, and measurements  
- [Medical Insurance Costs](https://www.kaggle.com/datasets/mirichoi0218/insurance) – age, BMI, smoking status, charges  

**Exercises**
1. Load dataset with `pandas`. Convert a column to NumPy.  
2. Compute mean and standard deviation of one feature.  
3. Normalize a column (subtract mean, divide by std).  
4. Use NumPy to compute correlation matrix between features.  
5. Perform a linear regression: predict fish weight from length and height.  
6. Perform a multiple regression: predict insurance charges from BMI, age, children.  

**Stretch Challenges**
- Write a function to standardize all numerical features.  
- Split dataset into train/test sets and compute mean squared error.  
- Compare manual regression to `sklearn.linear_model.LinearRegression`.  

---

## ✅ Outcomes
By the end, you’ll be able to:
- Slice and manipulate NumPy arrays confidently  
- Perform linear algebra operations (inverse, eigenvalues, solving systems)  
- Implement linear/quadratic/cubic regression from scratch  
- Apply regression to real-world datasets  

---
