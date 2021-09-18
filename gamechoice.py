import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import database_functions as db_f


class Main:
    def __init__(self):
        glade_file = "main.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)

        window = self.builder.get_object("Main")
        window.connect("delete-event", gtk.main_quit)
        window.show()

    def print_text(self, widget):
        text_box = self.builder.get_object("text_box")
        conn = db_f.connect_database()
        curr = conn.cursor()
        curr.execute("SELECT * from boardgames")
        string = curr.fetchone()
        text_box.set_text(str(string))


if __name__ == '__main__':
    main = Main()
    gtk.main()
