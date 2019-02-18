import gi
from _blueman import destroy_bridge
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="GUI Calculator")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()