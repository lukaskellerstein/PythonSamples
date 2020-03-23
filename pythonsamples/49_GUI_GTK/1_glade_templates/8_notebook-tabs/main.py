import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from datetime import datetime

import json
import jsonpickle

from helpers import printObject


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)
        self.set_default_size(800, 600)

        self.builder = Gtk.Builder()
        # self.builder.connect_signals(self)
        # self.connect("destroy", self.onDestroy)
        self.builder.add_from_file("main.glade")

        # set tabs
        main_tabs = self.builder.get_object("MainTabs")

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label("Here is the content of the first section."))
        main_tabs.append_page(self.page1, Gtk.Label("First Tab"))

        window = self.builder.get_object("MainWindow")
        window.connect("destroy", self.onDestroy)
        window.show_all()

    def onDestroy(self, *args):
        print("CLOSING")
        Gtk.main_quit()


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        MyWindow(self)


app = MyApplication()
app.run()

