import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class NewUserFormGrid:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./new_user_form/NewUserFormGrid.glade")

        self.template = self.builder.get_object("NewUserFormGrid")

        # unregister from glade gtk parent object/window/box ... etc.
        parent = self.template.get_parent()
        parent.remove(self.template)

        # self.add(self.template)
        self.builder.connect_signals(self)

    # Handler methods -------

    def onButtonPressed(self, button):
        print("Hello World!")

    # -----------------------

