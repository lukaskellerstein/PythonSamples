import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# ----------------------------------------------------
# Visualization
# ----------------------------------------------------
# ----------------------------------------------------

df = pd.DataFrame(np.random.rand(100, 2), columns=["A", "B"])

# show area for whole dataset
df.plot(kind="area", alpha=0.4)

# show area for one column
# df["A"].plot(kind="area", alpha=0.4)

# Show the plot
plt.show()
