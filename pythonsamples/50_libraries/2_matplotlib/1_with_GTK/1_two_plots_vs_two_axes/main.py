import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from datetime import datetime
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):

        Gtk.Window.__init__(self, application=app)
        self.set_default_size(800, 600)

        # ------------------------------------------------------------------

        # Functions to plot
        x = np.linspace(0, 5, 11)
        y = x ** 2

        # Figure as wrapper for plots
        fig = plt.figure()

        # Axes1
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.set_title("Bigger plot")

        # Plot1 to Axes1
        axes.plot(x, y)

        # Axes2
        axes2 = fig.add_axes([0.2, 0.2, 0.4, 0.3])
        axes2.set_title("Smaller plot")

        # Plot2 to Axes2
        axes2.plot(y, x)

        # ------------------------------------------------------------------
        canvas = FigureCanvas(fig)
        canvas.set_size_request(400, 300)

        self.add(canvas)


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)

