# everscan/modules/ui/curses.py

class CursesUiManager:
    """
    Facilitates communication between parent and child modules.
    """
    def __init__(self, manager):
        self.m_manager  = manager
        
        # Curses UI is not yet implemented; fall back to Qt
        raise ImportError