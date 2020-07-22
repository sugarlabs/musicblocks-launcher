import gi
import os

gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2

WebKit2.WebView.__gtype__
WebKit2.Settings.__gtype__

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
@Gtk.Template(filename=os.path.join(SCRIPT_PATH, 'webview.ui'))
class MyWindow(Gtk.Window):
    __gtype_name__ = "MyWindow"
    
    view = Gtk.Template.Child()
    settings = Gtk.Template.Child()
    
    def __init__(self):
        super(MyWindow, self).__init__()
        print(self.view)
        
        
win = MyWindow()
win.set_title('Music Blocks')
win.view.load_uri('file:///app/bin/index.html')
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
