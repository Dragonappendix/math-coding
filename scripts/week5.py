import numpy as np

# ## 📅 Week 5 – Regression with Matrices
# **Read/Watch**
# - [StatQuest – Least Squares Regression (YouTube)](https://www.youtube.com/watch?v=nk2CQITm_eo)  

# **Exercises**
# 1. Generate `x = [1,2,3,4,5]`, `y = [2,4,6,8,10]`. Fit a line using `np.polyfit`.  
# 2. Implement linear regression manually using the normal equation:  

# β = (XᵀX)⁻¹Xᵀy

# 3. Compare your coefficients with `np.polyfit`.  
# 4. Extend to quadratic regression (`y = a + bx + cx²`).  
# 5. Plot regression line against data (matplotlib).  

# **Stretch Challenges**
# - Implement cubic regression manually (β with x, x², x³).  
# - Generate noisy linear data (`y = 3x + 2 + noise`). Fit a line and compare to true slope/intercept.  

# ---