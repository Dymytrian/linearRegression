import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Data representation
data = pd.DataFrame({
    'Interest Rate': [18.3, 9.0, 7.0, 8.2, 9.5, 8.5, 8.0, 11.0, 10.6, 8.6, 7.8, 7.5, 6.8, 12.0, 26.6, 17.3, 13.1, 17.3, 16.7, 7.4, 7.7, 20.7],
    'CPI': [106.1, 99.4, 108.2, 112.3, 110.3, 111.6, 116.6, 122.3, 112.3, 109.1, 104.6, 99.8,100.5 ,124.9 ,143.3 ,112.4 ,113.7 ,109.8 ,104.1 ,105 ,110 ,126]
})

# Pearson correlation coefficient calculation
r, p_value = stats.pearsonr(data['Interest Rate'], data['CPI'])
print(f'Pearson correlation coefficient: {r:.2f}')
print(f'Value for testing the statistical significance of the result: {p_value:.5f}')
# Relationship materiality check
if p_value < 0.05:
    print('The relationship between the quantities is significant')
else:
    print('The relationship between the quantities is insignificant')

# Calculation of the coefficients of the linear regression equation
slope, intercept, r_value, p_value, std_err = stats.linregress(data['Interest Rate'], data['CPI'])
print(f'Linear regression equation: y = {intercept:.2f} + {slope:.2f}x')

# Plotting a Linear Regression Plot
plt.scatter(data['Interest Rate'], data['CPI'])
plt.plot(data['Interest Rate'], intercept + slope * data['Interest Rate'], 'r')
plt.xlabel('NBU interest rate')
plt.ylabel('Consumer price index')
plt.show()

