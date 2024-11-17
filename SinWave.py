#Online Source
import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 300)

# Calculate y values using the sine function
y = np.sin(x)

# Create the plot
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Graph')
plt.grid(True)
plt.show()