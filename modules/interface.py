# everscan/modules/interface.py

from ui.qt import QtUiManager
from ui.gtk import GtkUiManager
from ui.curses import CursesUiManager

import sys

class InterfaceManager:
    """
    Interface manager class.
    
    Interfaces with EverscanMaster, peer manager classes, and children
    in order to facilitate communication between them.
    """
    def __init__(self, master, selectedUI="qt"):
        # Link to EverscanMaster
        self.m_master   = master
        self.selectedUI = selectedUI
        
        # Qt UI is set as default for now.
        try:
            if self.selectedUI is "qt":
                self.ui = QtUiManager(self)
            elif self.selectedUI is "gtk":
                self.ui = GtkUiManager(self)
            elif self.selectedUI is "curses":
                self.ui = CursesUiManager(self)
            else:
                self.ui = QtUiManager(self)
        except ImportError:
            try:
                self.ui = QtUiManager(self)
            except ImportError:
                print "Failed to initialize Qt UI. Terminating application."
                sys.exit(1)