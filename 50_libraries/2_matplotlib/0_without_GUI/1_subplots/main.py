import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x ** 2

# ---------------------------------------
# Easiest approach
# ---------------------------------------

# set the current subplot
plt.subplot(nrows=1, ncols=2, index=1)

# add the plot to subplot
plt.plot(x, y)

# set the current subplot
plt.subplot(nrows=1, ncols=2, index=2)

# add the plot to subplot
plt.plot(y, x)

# add description for current plot
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Title")

# Show the plot
plt.show()
