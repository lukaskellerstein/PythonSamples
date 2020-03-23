import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x ** 2

# ---------------------------------------
# Object-oriented approach
# ---------------------------------------

# define Figure
fig = plt.Figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# add plot to Figure
axes.plot(x, y)


# Show the plot
plt.show()

# ------------------------------------------------------------
# ------------------------------------------------------------
# THIS EXAMPLE WILL NOT WORK WITHOUT GTK
# ------------------------------------------------------------
# ------------------------------------------------------------
