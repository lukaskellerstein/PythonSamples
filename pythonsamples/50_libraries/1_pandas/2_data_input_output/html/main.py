import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# Read data from HTML
# ----------------------------------------------------
# ----------------------------------------------------


df = pd.read_html("http://www.fdic.gov/bank/individual/failed/banklist.html")

print(df)
