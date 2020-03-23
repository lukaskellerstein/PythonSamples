import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()


builder = Gtk.Builder()
builder.add_from_file("main.glade")
builder.connect_signals(Handler())

grid = builder.get_object("MainGrid")

print(grid.get_halign())
print(grid.get_valign())
print(grid.get_hexpand())
print(grid.get_vexpand())


button3 = builder.get_object("button3")

print(button3.get_halign())
print(button3.get_valign())
print(button3.get_hexpand())
print(button3.get_vexpand())


window = builder.get_object("MainWindow")
window.show()

Gtk.main()
