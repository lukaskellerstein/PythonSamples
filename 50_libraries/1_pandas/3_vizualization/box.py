import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# ----------------------------------------------------
# Visualization
# ----------------------------------------------------
# ----------------------------------------------------

df = pd.DataFrame(np.random.randn(1000, 2), columns=["A", "B"])

# show bars for whole dataset
df.plot.box()

# show bars for one column
# df["A"].plot.box()

# Show the plot
plt.show()
