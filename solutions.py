#!/usr/bin/env python
# coding: utf-8

# ![head.png](https://github.com/iwh-halle/FinancialDataAnalytics/blob/master/figures/head.jpg?raw=1)
# 
# # Financial Data Analytics in Python
# 
# **Prof. Dr. Fabian Woebbeking**</br>
# Assistant Professor of Financial Economics
# 
# IWH - Leibniz Institute for Economic Research</br>
# MLU - Martin Luther University Halle-Wittenberg
# 
# fabian.woebbeking@iwh-halle.de

# ## Please follow these rules:
# 
# 1. Do NOT change the name of this file.
# 2. The numerical result (if applicable) of each task must be printed, e.g.
#     ```python
#     result = 1/3
#     print(result)
#     ```
# 3. Do not format any printed output using `print(f"...")`. Print **numeric or variable results** directly (see example above).
# 4. Do **not** round results at any point in your calculations.
# 5. Do not **change or remove the last code cell**. It is necessary for conversion and grading.
# 
# 
# From this point onward, you may start adding your solutions, you can add as many code and markdown cells as you like. However, please follow the print instructions exactly to ensure your submission is autograded correctly.

# # Example case part I:
# 
# ## Example task 1.1: 

# In[1]:


# example code cell 
x = 1 + 1/3
print(x)


# In[2]:


def present_value(C_t, r, t):
    """
    Calculate the present value of a future cash flow.

    Parameters
    ----------
    C_t : float
        Future cash flow at time t.
    r : float
        Interest rate as a decimal.
    t : int or float
        Time period.

    Returns
    -------
    float
        Present value of C_t.
    """
    return C_t / (1 + r) ** t


print(present_value(100, 0.03, 10))


# In[3]:


import numpy as np
import matplotlib.pyplot as plt

interest_rates = np.linspace(0, 0.25, 100)
present_values = present_value(100, interest_rates, 10)

plt.plot(interest_rates, present_values)
plt.xlabel("Interest rate")
plt.ylabel("Present value")
plt.title("Present value of 100 paid in 10 years")
plt.show()


# In[4]:


cash_flows = [10, 10, 110]
r = 0.05

total_present_value = 0

for t, C_t in enumerate(cash_flows, start=1):
    total_present_value = total_present_value + present_value(C_t, r, t)

print(total_present_value)


# In[5]:


import pandas as pd
import numpy as np

prices = pd.read_csv("02_python_data.csv", index_col=0, parse_dates=True)

returns = prices.pct_change()
logreturns = np.log(prices / prices.shift(1))

print(prices.head())
print(returns.head())
print(logreturns.head())


# # The End
# 
# <div style="color: red; font-weight: bold; font-size: 18px">
# ⚠️ DO NOT MODIFY OR MOVE THE CODE CELL BELOW! ⚠️
# </div>
# 
# The following code **must remain unchanged** and at the end of the script and **must be executed once your homework is completed**.
# 
# This block converts your notebook to a `.py` file for GitHub Classroom autograding. After you have completed the assignment, simply run the entire notebook again and you should see a file called solutions.py, which we will use for autograding. You can run - and therefore recreate solutions.py - as often as you want.

# 

# In[ ]:


# Convert notebook to script
try:
    # Check if running in a Jupyter notebook
    shell = get_ipython().__class__.__name__
    if shell == 'ZMQInteractiveShell':
        import os
        os.system('jupyter nbconvert solutions.ipynb --to script')
except NameError:
    pass

