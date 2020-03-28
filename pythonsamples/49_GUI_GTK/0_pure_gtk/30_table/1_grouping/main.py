from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Table Demo")
        self.set_border_width(10)

        # create a TreeStore with one string column to use as the model
        store = Gtk.TreeStore(str)

        # add row
        row1 = store.append(None, ["JAVA"])

        # add child rows
        store.append(row1, ["AWT"])
        store.append(row1, ["Swing"])
        store.append(row1, ["JSF"])

        # add another row
        row2 = store.append(None, ["Python"])
        store.append(row2, ["PyQt"])
        store.append(row2, ["WxPython"])
        store.append(row2, ["PyGTK"])

        # TreeView is the item that is displayed
        self.tree_view = Gtk.TreeView(store)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", renderer, text=0)
        self.tree_view.append_column(column)

        self.add(self.tree_view)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
