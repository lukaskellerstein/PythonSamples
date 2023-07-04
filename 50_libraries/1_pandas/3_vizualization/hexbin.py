import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# ----------------------------------------------------
# Visualization
# ----------------------------------------------------
# ----------------------------------------------------

df = pd.DataFrame(np.random.randn(1000, 2), columns=["A", "B"])


# hexbin
# df.plot.hexbin(x="A", y="B")
# df.plot.hexbin(x="A", y="B", gridsize=25)
df.plot.hexbin(x="A", y="B", gridsize=25, cmap="coolwarm")

plt.show()
