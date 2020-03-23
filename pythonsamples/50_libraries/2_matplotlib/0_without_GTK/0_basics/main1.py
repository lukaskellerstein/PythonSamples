import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x ** 2

# add to the plot this line
plt.plot(x, y)


# add description for plot
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Title")

# Show the plot
plt.show()
