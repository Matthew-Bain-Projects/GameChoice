import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk


class Main: 
    def __init__(self):
        glade_file = "main.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)

#        main_button = self.builder.get_object("Main_Button")
#        main_button.connect("clicked", self.printText)

        window = self.builder.get_object("Main")
        window.connect("delete-event", gtk.main_quit)
        window.show()

    def print_text(self, widget):
        print("Hello World")


if __name__ == '__main__':
    main = Main()
    gtk.main()
        
