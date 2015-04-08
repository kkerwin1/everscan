# everscan/modules/ui/curses.py

from modules.ui.uiErrors import UIInitializeError

class CursesUiManager:
    """
    Facilitates communication between parent and child modules.
    """
    def __init__(self, manager):
        self.m_manager  = manager
        
        # Curses UI is not yet implemented; fall back to Qt
        raise UIInitializeError