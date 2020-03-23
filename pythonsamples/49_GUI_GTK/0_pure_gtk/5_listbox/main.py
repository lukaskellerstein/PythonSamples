import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="My Window", application=app)
        self.set_border_width(10)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        # checkbox
        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_1.add(box_1)
        label_1 = Gtk.Label("Check if you love cheeseburgers:")
        check = Gtk.CheckButton()
        box_1.pack_start(label_1, True, True, 0)
        box_1.pack_start(check, True, True, 0)
        listbox.add(row_1)

        # Toggle Switch
        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_2.add(box_2)
        label_2 = Gtk.Label("Burger making machine:")
        switch = Gtk.Switch()
        box_2.pack_start(label_2, True, True, 0)
        box_2.pack_start(switch, True, True, 0)
        listbox.add(row_2)


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
