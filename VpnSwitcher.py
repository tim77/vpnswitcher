import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="VpnSwitcher")
        self.set_border_width(10)
        hbox = Gtk.Box(spacing = 10)
        self.add(hbox)

        button1 = Gtk.Button.new_with_label("Turn on WireGuard")
        button1.connect("clicked", self.clicked1)
        hbox.pack_start(button1, True, True, 0)
 
        button2 = Gtk.Button.new_with_label("Turn off WireGuard")
        button2.connect("clicked", self.clicked2) 
        hbox.pack_start(button2, True, True, 0)

        button3 = Gtk.Button.new_with_label("Close programm")
        button3.connect("clicked", self.closed)
        hbox.pack_start(button3, True, True, 0)
        
    def clicked1(self, button1):
        os.system("pkexec systemctl enable --now wg-quick@wg0.service")
    def clicked2(self, button2):
        os.system("pkexec systemctl disable --now wg-quick@wg0.service")
    def closed(self, button3):
        Gtk.main_quit()

window = ButtonWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
       

