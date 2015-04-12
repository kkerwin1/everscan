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
        self.m_imaging      = self.m_master.m_imaging
        self.deviceList     = []
        self.deviceDict     = {}
        self.currentDevice  = None
        
        # optionsList is a list of all options available
        self.optionsList    = []
        # optionsDict is a dictionary indexed by optionName. The value indexed 
        # by each optionName is a list of "constraints". These "constraints"
        # are the available choices for values of each option. 
        self.optionsDict    = {}
        
        self.getDevices()
    
    def getDevices(self):
        """
        Obtain deviceList and update the Gui with its contents.
        """
        
        self.deviceList = pyinsane.get_devices()
        try:
            # Presume we obtained at least one device
            assert len(self.deviceList) > 0
            for device in self.deviceList:
                self.deviceDict[device.name] = device
        except AssertionError:
            # Presumption was wrong; there are no 
            # devices in self.deviceList
            self.deviceList = []
        
        # Update Gui
        self.m_interface.updateDevices()
    
    def selectDevice(self, deviceName):
        """
        Provided a deviceName, select device to scan from.
        """
        
        self.currentDevice = self.deviceDict[deviceName]
        self.getDeviceOptions()
        
    def getDeviceOptions(self):
        """
        Obtain optionsList and optionsDict; update Gui with contents.
        
        pyinsane builds this into the device object by default. We'll be explicit
        and duplicate the function here for the purpose of creating code that
        self-documents.
        """
        
        device = self.currentDevice
        self.optionsList = device.options.keys()
        
        for optionName in self.optionsList:
            # Initialize constraintList
            constraintList = []
            for constraintName in device.options[optionName].constraint:
                # Build constraintList
                constraintList.append(constraintName)
            self.optionsDict[optionName] = constraintList
        
        # Update Gui
        self.m_interface.updateOptions()
    
    def selectOptionConstraint(self, optionName, constraint):
        """
        Provided an optionName and a constraint from the Gui, set the option value
        to equal the specified constraint.
        """
        
        device = self.currentDevice
        device.options[optionName].value = constraint
    
    def scan(self):
        """
        Perform a scan.
        """
        
        device = self.currentDevice
        scanSession = None
        
        # Flatbed scan
        if device.options["source"].value is not "ADF":
            scanSession = device.scan(multiple=False)
            # Get one page
            try:
                while True:
                    scanSession.scan.read()
            # Finished getting one page
            except EOFError:
                pass
            
        # ADF (Automatic Document Feeder) scan
        else:
            scanSession = device.scan(multiple=True)
            # Get ALL pages
            try:
                while True:
                    # Get next page
                    try:
                        while True:
                            scanSession.scan.read()
                    # Finished getting next page
                    except EOFError:
                        pass
            # Finished getting ALL pages
            except StopIteration:
                pass
        
        # Presume we got at least one page
        try:
            assert len(scanSession.images) > 0
            self.m_imaging.addImages(scanSession.images)
        except AssertionError:
            pass