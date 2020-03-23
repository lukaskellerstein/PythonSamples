import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self):
        Gtk.Window.__init__(self, title="My Window")

        self.label = Gtk.Label()
        self.label.set_label("OMG this is awesome")
        self.label.set_angle(30)
        self.label.set_halign(Gtk.Align.END)
        self.add(self.label)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

