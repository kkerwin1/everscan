# everscan/modules/interface.py

class InterfaceManager:
    """
    Interface manager class.
    
    Interfaces with EverscanMaster, peer manager classes, and children
    in order to facilitate communication between them.
    """
    def __init__(self, master):
        # Link to EverscanMaster
        self.m_master   = master