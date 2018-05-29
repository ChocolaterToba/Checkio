import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-5, 5, 0.1)
y = x ** 2
z = x * 2 + 6
plt.plot(x, y, x, z)

plt.title('y = x ^ 2  and y = x * 2 + 6 functions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)