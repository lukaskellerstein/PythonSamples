import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from datetime import datetime
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

from datareader import DataReader
from price_chart.price_chart import PriceChart

import numpy as np


class MyWindow(Gtk.ApplicationWindow):

    datareader = DataReader()

    def __init__(self, app):
        Gtk.Window.__init__(self, application=app)
        self.set_default_size(800, 600)

        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        tesla = self.datareader.get_stock_data("TSLA")
        chart1 = PriceChart(tesla)

        priceChartBox = self.builder.get_object("PriceChart")
        priceChartBox.add(chart1.canvas)

        apple = self.datareader.get_stock_data("AAPL")
        chart2 = PriceChart(apple)

        priceChartBox = self.builder.get_object("PriceChart2")
        priceChartBox.add(chart2.canvas)

        window = self.builder.get_object("MainWindow")
        window.show_all()


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        MyWindow(self)


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)

