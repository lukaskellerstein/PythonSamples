import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# ----------------------------------------------------
# Visualization
# ----------------------------------------------------
# ----------------------------------------------------

df = pd.DataFrame(np.random.rand(100, 2), columns=["A", "B"])

# show bars for whole dataset
df.plot(kind="bar")

# show bars for one column
# df["A"].plot.bar()

# Show the plot
plt.show()
