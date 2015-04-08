# everscan/modules/ui/gtk.py

from modules.ui.uiErrors import UIInitializeError

class GtkUiManager:
    """
    Facilitates communication between parent and child modules.
    """
    def __init__(self, manager):
        self.m_manager  = manager
        
        # GTK UI is not yet implemented; fall back to Qt
        raise UIInitializeError