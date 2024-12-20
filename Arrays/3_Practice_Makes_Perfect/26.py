import numpy as np
import matplotlib.pyplot as plt

x_degrees = np.linspace(0, 360, 361)  
x_radians = np.radians(x_degrees)  

y_values = np.sin(x_radians)

plt.plot(x_degrees, y_values, label='y = sin(x)', color='blue')
plt.title('Graph of y = sin(x) from 0 to 360 degrees')
plt.xlabel('x (degrees)')
plt.ylabel('y (sin(x))')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

plt.legend()
plt.show()
