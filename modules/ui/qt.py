# everscan/modules/ui/qt.py

class QtUiManager:
    """
    Facilitates communication between parent and child modules.
    """
    def __init__(self, manager):
        self.m_manager  = manager
        
        # Qt UI is not yet implemented.
        # Qt UI will be the first to be implemented.
        raise ImportError