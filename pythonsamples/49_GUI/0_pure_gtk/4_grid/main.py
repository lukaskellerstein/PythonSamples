import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="My Window", application=app)

        self.grid = Gtk.Grid()
        # some space between the columns of the grid
        # self.grid.set_column_spacing(20)
        # self.grid.set_halign(Gtk.Align.FILL)
        # self.grid.set_valign(Gtk.Align.FILL)

        print(self.grid.get_halign())
        print(self.grid.get_valign())
        print(self.grid.get_hexpand())
        print(self.grid.get_vexpand())

        button1 = Gtk.Button(label="button1")
        button2 = Gtk.Button(label="button2")
        button3 = Gtk.Button(label="button3")
        # button3.set_hexpand(True)
        # button3.set_vexpand(True)
        button4 = Gtk.Button(label="button4")
        button5 = Gtk.Button(label="button5")
        button6 = Gtk.Button(label="button6")

        self.grid.attach(button1, 0, 0, 1, 1)
        self.grid.attach(button2, 1, 0, 2, 1)
        self.grid.attach(button3, 0, 1, 1, 2)
        self.grid.attach(button4, 1, 1, 2, 1)
        self.grid.attach(button5, 1, 2, 1, 1)
        self.grid.attach(button6, 2, 2, 1, 1)

        print(button3.get_halign())
        print(button3.get_valign())
        print(button3.get_hexpand())
        print(button3.get_vexpand())

        self.add(self.grid)


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
