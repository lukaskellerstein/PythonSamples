import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# ----------------------------------------------------
# Visualization
# ----------------------------------------------------
# ----------------------------------------------------

df = pd.DataFrame(np.random.randn(1000, 2), columns=["A", "B"])


# show histogram for whole dataset
df.plot.hist()

# show histogram for one column
# df["A"].hist()
# df["A"].hist(bins=20)
# df["A"].plot(kind="hist", bins=100)
# or
# df["A"].plot.hist()

# Show the plot
plt.show()
