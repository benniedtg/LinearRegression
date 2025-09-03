import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('data/data.csv')
# plt.scatter(data['YearsExperience'], data['Salary'])
# plt.show()


def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    n = len(points)
    for i in range(n):
        x = points.iloc[i].YearsExperience
        y= points.iloc[i].Salary
        # Partial Derivative of m, and of b
        m_gradient += (-2/n)*x*(y-(m_now *x + b_now))
        b_gradient += (-2/n)* (y-m_now*x + b_now)
    m = m_now-m_gradient*L
    b = b_now-b_gradient*L
    return m, b

m = 0
b = 0
L = 0.0001
epochs = 1000
for i in range(epochs):
    if i%50 ==0:
        print(f'Epoch: {i},')
    m, b = gradient_descent(m, b , data, L)

print(m, b)
yr_range = range(2, 10)
plt.scatter(data['YearsExperience'], data['Salary'], color = 'black')
plt.plot(list(yr_range), [m*x + b for x in yr_range], color = "red")
plt.show()