from gi.repository import Gtk
from random import randint


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Table Demo")
        self.set_border_width(10)

        # create a TreeStore with one string column to use as the model
        self.store = Gtk.TreeStore(str, float, float)

        # # add row
        # row1 = store.append(None, ["CL", 0, 0, 0, 0])
        # store.append(row1, ["CLZ0", 100, 105, 95, 110])
        # store.append(row1, ["CLZ1", 100, 105, 95, 110])
        # store.append(row1, ["CLZ2", 100, 105, 95, 110])
        # store.append(row1, ["CLZ3", 100, 105, 95, 110])
        # store.append(row1, ["CLZ4", 100, 105, 95, 110])

        # # add another row
        # row2 = store.append(None, ["ES", 0, 0, 0, 0])
        # store.append(row2, ["ESZ0", 100, 105, 95, 110])
        # store.append(row2, ["ESZ1", 100, 105, 95, 110])
        # store.append(row2, ["ESZ2", 100, 105, 95, 110])
        # store.append(row2, ["ESZ3", 100, 105, 95, 110])
        # store.append(row2, ["ESZ4", 100, 105, 95, 110])

        # TreeView is the item that is displayed
        self.tree_view = Gtk.TreeView(self.store)

        for i, col_title in enumerate(["Ticker", "Open", "Close"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            column.set_sort_column_id(i)
            self.tree_view.append_column(column)

        data = {
            "CL": {"CLM0": (0, 0), "CLZ0": (0, 0)},
            "ES": {"ESM0": (0, 0), "ESX0": (0, 0)},
        }
        self.updateTreeView(data)

        data2 = {
            "CL": {
                "CLM0": (randint(0, 100), randint(0, 100)),
                "CLZ0": (randint(0, 100), randint(0, 100)),
            },
            "ES": {
                "ESM0": (randint(0, 100), randint(0, 100)),
                "ESX0": (randint(0, 100), randint(0, 100)),
            },
        }
        self.updateTreeView(data2)

        self.add(self.tree_view)

    def updateTreeView(self, data):

        aaa = len(self.store)
        print(aaa)

        for mainItemKey, mainItemValue in data.items():
            if aaa == 0:
                par1 = self.store.append(None, (mainItemKey, 0, 0))
                for innerItemKey, innerItemValue in mainItemValue.items():
                    self.store.append(par1, (innerItemKey, *innerItemValue))
            else:

                for item in self.store:
                    print(item[:])

                    for inner in item.iterchildren():
                        print(inner[:])

                        for innerItemKey, innerItemValue in mainItemValue.items():

                            if inner[0] == innerItemKey:
                                self.store[treeiter][1:] = ["Donald Ervin Knuth", 41.99]
                                self.store.set(inner, (innerItemKey, *innerItemValue))


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
