import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.fish_box = Gtk.Box(spacing=10)

        self.tuna_button = Gtk.Button(label="Tuna")
        self.tuna_button.connect("clicked", self.on_tuna_button_clicked)

        self.salomon_button = Gtk.Button(label="Salomon")
        self.salomon_button.connect("clicked", self.on_salomon_button_clicked)

        

        self.fish_box.add(self.tuna_button)
        self.fish_box.add(self.salomon_button)
        self.add(self.fish_box)

    def on_tuna_button_clicked(self, widget):
        print("tuna clicked")

    def on_salomon_button_clicked(self, widget):
        print("salomon clicked")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
