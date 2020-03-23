import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# ----------------------------------------------------
# Visualization - Scatter plot = CORRELATION
# ----------------------------------------------------
# ----------------------------------------------------

df = pd.DataFrame(np.random.randn(1000, 3), columns=["A", "B", "Z"])


# show scatter of two columns
# df.plot.scatter(x="A", y="B")
# with deep
df.plot.scatter(x="A", y="B", c="Z")

# Show the plot
plt.show()
