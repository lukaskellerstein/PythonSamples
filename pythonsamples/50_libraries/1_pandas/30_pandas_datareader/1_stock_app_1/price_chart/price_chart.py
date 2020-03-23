import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import matplotlib.pyplot as plt

from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas


class PriceChart:
    def __init__(self, data):

        fig, axes = plt.subplots(nrows=2, ncols=1)

        data["Close"].plot(ax=axes[0])
        data["Volume"].plot(ax=axes[1])

        self.canvas = FigureCanvas(fig)
        self.canvas.set_size_request(400, 300)
