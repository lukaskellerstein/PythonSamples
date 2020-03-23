import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


from new_user_form.new_form_user_grid import NewUserFormGrid


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, application=app)

        builder = Gtk.Builder()
        builder.add_from_file("main.glade")
        builder.connect_signals(Handler())

        form_frame_box = builder.get_object("FormBox")

        formBox = NewUserFormGrid()
        templ = formBox.template
        print(formBox)
        print(templ)

        form_frame_box.add(templ)
        print(form_frame_box)

        chart_frame_box = builder.get_object("ChartBox")
        print(chart_frame_box)

        aaa = Gtk.Label("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        chart_frame_box.add(aaa)

        window = builder.get_object("MainWindow")
        window.show_all()


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        MyWindow(self)


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
