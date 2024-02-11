#!/usr/bin/env python3
"""Battery drain/charge rate indicator for Ubuntu tray.

This works on my ThinkPad E14 G4 with a single battery.
You may need to change the POWER_CMD command to adjust
it to your system.
 
You may need to do: sudo apt install gir1.2-appindicator3-0.1
"""
import signal
import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, AppIndicator3, GObject
import time
from threading import Thread

POWER_CMD = "cat /sys/class/power_supply/BAT0/power_now"
ICON = "gnome-power-manager-symbolic"

class Indicator():
    def __init__(self):
        self.app = "Battery Power" 
        self.indicator = AppIndicator3.Indicator.new(
            self.app, "gnome-power-manager-symbolic",
            AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)       
        self.indicator.set_menu(self.create_menu())
        self.indicator.set_label("Power", self.app)
        # the thread:
        self.update = Thread(target=self.show_power)
        # daemonize the thread to make the indicator stopable
        self.update.setDaemon(True)
        self.update.start()

    def create_menu(self):
        menu = Gtk.Menu()
        # quit
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.stop)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def show_power(self):
        interval_s = 2
        while True:
            time.sleep(interval_s)
            mention = f"{self.get_power():0.2} W"
            # apply the interface update using  GObject.idle_add()
            GObject.idle_add(
                self.indicator.set_label,
                mention, self.app,
                priority=GObject.PRIORITY_DEFAULT
                )

    def get_power(self):
        result = subprocess.run(POWER_CMD, shell=True, capture_output=True, text=True)
        return float(result.stdout.strip()) / 1e6

    def stop(self, source):
        Gtk.main_quit()

Indicator()
# this is where we call GObject.threads_init()
GObject.threads_init()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()