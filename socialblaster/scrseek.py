import cv2
import os, sys, platform
import shutil

isMSW = False
if os.name == 'nt' :
    isMSW = True
    import PIL.ImageGrab as ig
else :      # Assume Linux/GTK
    from config import launchCommand

def GrabScreen( filename ) :
    if platform.system() =='Windows' :
        img =ig.grab()      # ImageGrab is a module from the PIL package
        img.save( filename )        #  similar to the Image module.
    else :      # ??? Is this a Linux hack or always a perfectly acceptable command line :
        launchCommand( '/usr/bin/xwd -display  :0 -root -out %s' % filename )

method = cv2.TM_SQDIFF_NORMED

def positionOf(image_name):
    GrabScreen( 'screen.png' )
    # Read the images from the file
    small_image = cv2.imread(image_name)
    large_image = cv2.imread('screen.png')
    result = cv2.matchTemplate(small_image, large_image, method)
    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc
    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]
    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    return [MPx, MPy]
    # Display the original image with the rectangle around the match.
