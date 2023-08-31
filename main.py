import gi
import subprocess
import functions

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

monitors = functions.listMonitors()

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Brightness Controller")
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 6)
        self.add(self.box)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(10)

        lines = []

        for numMonitors in range(len(monitors)):
            value = functions.getBrightness(monitors[numMonitors]) * 100
            adjustment = Gtk.Adjustment(value, 10, 100, 1, 10, 0)

            self.scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjustment)
            lines.append(self.scale)

            self.scale.set_value_pos(Gtk.PositionType.BOTTOM)
            self.scale.set_vexpand(True)
            self.scale.set_hexpand(True)
            #self.box.pack_start(self.scale, True, True, 0)
            self.scale.connect("value-changed", self.changeBrightness, monitors[numMonitors], lines)

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)

        for numScales in range(len(lines)):
            stack.add_titled(lines[numScales], "mon{}".format(numScales), "{}".format(monitors[numScales]))
            self.box.pack_start(stack_switcher, True, True, 0)
            self.box.pack_start(stack, True, True, 0)

    def changeBrightness(self, widget, monitor, scales):
        value = scales[monitors.index(monitor)].get_value()
        x = ["xrandr", "--output", "{}".format(monitor), "--brightness", "{}".format(value / 100)]
        change_brightness = subprocess.run(x)

win = MyWindow() # Creates window
win.show_all() # Displays window
Gtk.main()


