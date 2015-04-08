# everscan/modules/ui/gtk.py

class GtkUiManager:
    """
    Facilitates communication between parent and child modules.
    """
    def __init__(self, manager):
        self.m_manager  = manager
        
        # GTK UI is not yet implemented; fall back to Qt
        raise ImportError