# everscan/modules/imaging.py

import pillow

class ImagingManager:
    """
    Imaging manager class.
    
    Interfaces with EverscanMaster, peer manager classes, and children
    in order to facilitate communication between them.
    """
    
    def __init__(self, manager):
        """
        Initialize ImagingManager object.
        """
        
        self.m_manager = manager