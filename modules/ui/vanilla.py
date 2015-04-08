# everscan/modules/ui/vanilla.py

from modules.ui.uiErrors import UIInitializeError

class VanillaUI:
    """
    Super class for Qt, Gtk+ GUI classes. 
    
    Implements a single common API for InterfaceManager to control.
    """
    def __init__(self, manager):
        self.m_manager = manager
        
        # Not yet implemented.
        raise UIInitializeError