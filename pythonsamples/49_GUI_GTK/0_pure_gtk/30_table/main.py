from gi.repository import Gtk

# import pango


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

        self.list_store = Gtk.ListStore(str, float, float, float, float)

        # TreeView is the item that is displayed
        self.tree_view = Gtk.TreeView(self.list_store)

        # Handle selection
        self.selected_row = self.tree_view.get_selection()
        self.selected_row.connect("changed", self.item_selected)

        # Make a click activate a row such that we get the row_activated signal when it is clicked
        self.tree_view.set_activate_on_single_click(True)

        # Connect a listener to the row_activated signal to check whether the correct column was clicked
        self.tree_view.connect("row_activated", self.action_icon_clicked)

        self.add(self.tree_view)

        self.setHistoricalDataTable(data)

    def setHistoricalDataTable(self, data):
        self.list_store.clear()

        for item in data:
            self.list_store.append(
                [item["date"], item["open"], item["high"], item["low"], item["close"]]
            )

        for i, col_title in enumerate(["Date", "Open", "High", "Low", "Close"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            column.set_sort_column_id(i)
            self.tree_view.append_column(column)

        # delete button
        action_icon = Gtk.CellRendererPixbuf()
        self.column_action_icon = Gtk.TreeViewColumn("", action_icon, icon_name=2)
        self.tree_view.append_column(self.column_action_icon)

    # delete handler
    def action_icon_clicked(self, treeview, path, column):
        # If the column clicked is the action column remove the clicked row
        if column is self.column_action_icon:

            # Get the iter that points to the clicked row
            iter = self.list_store.get_iter(path)

            # Remove it from the ListStore
            self.list_store.remove(iter)

    def item_selected(self, selection):
        model, row = selection.get_selected()
        if row is not None:
            print("TABLE LOG")
            print("Date: ", model[row][1])
            print("Close: ", model[row][4])
            print("")


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
