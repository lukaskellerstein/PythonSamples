from gi.repository import Gtk


data = [
    {"date": "1-1-2000", "open": 100, "high": 105, "low": 95, "close": 110},
    {"date": "1-2-2000", "open": 115, "high": 125, "low": 110, "close": 120},
    {"date": "1-3-2000", "open": 123, "high": 155, "low": 100, "close": 130},
    {"date": "1-4-2000", "open": 130, "high": 145, "low": 95, "close": 140},
]


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Table Demo")
        self.set_border_width(10)

        # create a TreeStore with one string column to use as the model
        store = Gtk.TreeStore(str, float, float, float, float)

        # add row
        row1 = store.append(None, ["CL", 0, 0, 0, 0])
        store.append(row1, ["CLZ0", 100, 105, 95, 110])
        store.append(row1, ["CLZ1", 100, 105, 95, 110])
        store.append(row1, ["CLZ2", 100, 105, 95, 110])
        store.append(row1, ["CLZ3", 100, 105, 95, 110])
        store.append(row1, ["CLZ4", 100, 105, 95, 110])

        # add another row
        row2 = store.append(None, ["ES", 0, 0, 0, 0])
        store.append(row2, ["ESZ0", 100, 105, 95, 110])
        store.append(row2, ["ESZ1", 100, 105, 95, 110])
        store.append(row2, ["ESZ2", 100, 105, 95, 110])
        store.append(row2, ["ESZ3", 100, 105, 95, 110])
        store.append(row2, ["ESZ4", 100, 105, 95, 110])

        # TreeView is the item that is displayed
        self.tree_view = Gtk.TreeView(store)

        for i, col_title in enumerate(["Ticker", "Open", "High", "Low", "Close"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            column.set_sort_column_id(i)
            self.tree_view.append_column(column)

        self.add(self.tree_view)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
