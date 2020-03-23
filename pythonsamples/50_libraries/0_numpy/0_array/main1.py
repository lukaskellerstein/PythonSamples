import numpy as np
from numpy import pi

# ----------------------------------------------------
# Linear space/curve
# ----------------------------------------------------

# generate linear curve points (30x) from 0 to 10

space1 = np.linspace(0, 10, 30)
print(type(space1))
print(space1)


# ----------------------------------------------------
# Goniometric functions - Sinus
# ----------------------------------------------------

x = np.linspace(0, 2 * pi, 100)
a = np.sin(x)
print(type(a))
print(a)

