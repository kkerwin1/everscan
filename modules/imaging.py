# everscan/modules/imaging.py

from PIL import Image
import sys

class ImagingManager:
    """
    Imaging manager class.
    
    Interfaces with EverscanMaster, peer manager classes, and children
    in order to facilitate communication between them.
    """
    
    def __init__(self, master):
        """
        Initialize ImagingManager object.
        """
        
        self.m_master       = master
        self.m_interface    = self.m_master.m_interface
        self.images         = []
        self.deletedImages  = []
    
    def addImages(self, imageList):
        """
        Provided a list of image objects, append them one by one to self.images.
        """
        
        try:
            # Presume a list of images was passed to function.
            assert type(imageList) == type([])
            for image in imageList:
                self.images.append(image)
            self.m_interface.updateImagePane()
        except AssertionError:
            # We presumed wrong; a single image was passed
            # to the function.
            print "Naughty, naughty. imaging.ImagingManager.addImages takes a list of images."
            sys.exit(1)
    
    def rotateClockwise(self, imageIndex):
        """
        Provided an index number of an image, look up the image and rotate 90* clockwise.
        """
        
        try:
            image = self.images[imageIndex]
            image = image.rotate(90)
            self.images[imageIndex] = image
            self.m_interface.updateImagePane()
        except IndexError:
            pass
    
    def rotateCounter(self, imageIndex):
        """
        Provided an index number of an image, look up the image and rotate 90* counter-clockwise.
        """
        
        try:
            image = self.images[imageIndex]
            image = image.rotate(270)
            self.images[imageIndex] = image
            self.m_interface.updateImagePane()
        except IndexError:
            pass
    
    def flipVertical(self, imageIndex):
        """
        Flip image vertically.
        """
        
        try:
            image = self.images[imageIndex]
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            self.images[imageIndex] = image
            self.m_interface.updateImagePane()
        except IndexError:
            pass
    
    def flipHorizontal(self, imageIndex):
        """
        Flip image horizontally.
        """
        
        try:
            image = self.images[imageIndex]
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            self.images[imageIndex] = image
            self.m_interface.updateImagePane()
        except IndexError:
            pass
        
    def moveImageUp(self, imageIndex):
        """
        Move image up the stack in the Gui.
        """
        
        if imageIndex > 0:
            try:
                image = self.images[imageIndex]
                self.images[imageIndex-1] = image
                self.m_interface.updateImagePane()
            except IndexError:
                pass
        else:
            pass
    
    def moveImageDown(self, imageIndex):
        """
        Move image down the stack in the Gui.
        """
        
        try:
            image = self.images[imageIndex]
            self.images[imageIndex+1] = image
            self.m_interface.updateImagePane()
        except IndexError:
            # Image was already at the bottom of the stack.
            pass
    
    def removeImage(self, imageIndex):
        """
        Delete an image.
        """
        
        try:
            deletedImage = self.images[imageIndex]
            self.deletedImages.append(deletedImage)
            del self.images[imageIndex]
            self.m_interface.updateImagePane()
        except IndexError:
            pass
    
    def un_removeImage(self, deletedIndex):
        """
        Undo deletion of an image.
        """
        
        try:
            deletedImage = self.deletedImages[deletedIndex]
            self.images.append(deletedImage)
            del self.deletedImages[deletedIndex]
            self.m_interface.updateImagePane()
        except IndexError:
            pass