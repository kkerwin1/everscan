# everscan/modules/scanning.py

import pyinsane.abstract as pyinsane

class ScanningManager:
    """
    Scanning manager class.
    
    Interfaces with EverscanMaster, peer manager classes, and children
    in order to facilitate communication between them.
    """
    
    def __init__(self, master):
        """
        Initialize ScanningManager object.
        """        
        # Link back to EverscanMaster
        self.m_master       = master
        
        # Declare attribute variable names.
        self.m_interface    = self.m_master.m_interface
        self.deviceList     = []
        self.deviceDict     = {}
        self.currentDevice  = None
        
        self.getDevices()
    
    def getDevices(self):
        """
        Obtain deviceList and update the Gui with its contents.
        """
        self.deviceList = pyinsane.get_devices()
        try:
            assert len(self.deviceList) > 0
            for device in self.deviceList:
                self.deviceDict[device.name] = device
        except AssertionError:
            pass
        self.m_interface.updateDevices()
    
    def selectDevice(self, deviceName):
        """
        Provided a deviceName, select device to scan from.
        """
        self.currentDevice = self.deviceDict[deviceName]
    
    