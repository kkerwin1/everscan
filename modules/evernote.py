# everscan/modules/evernote.py

class EvernoteManager:
    """
    Evernote manager class.
    
    Interfaces with EverscanMaster, peer manager classes, and children
    in order to facilitate communication between them.
    """
    def __init__(self, master):
        self.m_master   = master