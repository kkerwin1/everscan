#!/usr/bin/python
# everscan/everscan.py

from modules.scanning   import ScanningManager
from modules.evernote   import EvernoteManager
from modules.interface  import InterfaceManager
from modules.imaging    import ImagingManager

class EverscanMaster:
    """
    Everscan master class.
    
    Facilitates communication between child objects.
    """
    def __init__(self):
        # Initialize child manager objects.
        self.m_scanning     = ScanningManager(self)
        self.m_evernote     = EvernoteManager(self)
        self.m_interface    = InterfaceManager(self)
        self.m_imaging      = ImagingManager(self)