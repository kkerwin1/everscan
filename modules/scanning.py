# everscan/modules/scanning.py

class ScanningManager:
    """
    Scanning manager class.
    
    Interfaces with EverscanMaster, peer manager classes, and children
    in order to facilitate communication between them.
    """
    
    def __init__(self, master):
        # Link back to EverscanMaster
        self.m_master   = master