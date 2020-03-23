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

        box = Gtk.Box(spacing=10)

        fig1 = self.get_plot(2)
        fig2 = self.get_plot(4)

        box.add(fig1)
        box.add(fig2)

        self.add(box)

    def get_plot(self, num):

        x = np.linspace(0, 5, 11)
        y = x ** num

        fig = plt.figure()
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

        axes.plot(x, y, color="red")

        canvas = FigureCanvas(fig)
        canvas.set_size_request(400, 300)
        return canvas


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)

