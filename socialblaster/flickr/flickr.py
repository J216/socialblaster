import mouse_keyboard_input as kmi
from time import sleep
from random import randrange
import os
from j_tools import metadata as md
import pyautogui as pag
import scrseek
import inspect

win_key=0x5B
tab=0x09
ctrl=0x11
shift_key=0x10
page_down=0x22
enter_key=0x0D
esc_key=0x1B
a_key=0x41
c_key=0x43
i_key=0x49
v_key=0x56
left_arrow=0x25
up_arrow=0x26
right_arrow=0x27
down_arrow=0x28
browser = "chrome"
image_preview = True

path_flickr=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def Click_ScreensaverAway():
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)

def Click_Chrome():
    #click google chrome
    ff_btn=scrseek.positionOf('chrome_taskbar.png')
    ff_btn=[x+30 for x in ff_btn]
    kmi.Click(*ff_btn)
    sleep(.21)
    kmi.HoldKey(win_key,up_arrow)
    sleep(1)

def Click_Addressbar():
    #click address bar
    kmi.Click(420,50)

def Paste_FlickrAddress():
    #copy and paste address for FB AND hit enter key
    kmi.clip_board.copy("https://www.flickr.com")
    kmi.HoldKey(ctrl,a_key)
    kmi.HoldKey(ctrl,v_key)
    sleep(1)
    #press enter to go to address
    kmi.TapKey(enter_key)

def Click_FlickrUpload():
    #click upload
    upload_pos=scrseek.positionOf('fl_upload_btn.png')
    upload_pos = [x+15 for x in upload_pos]
    kmi.Click(upload_pos[0],upload_pos[1])

def Click_FlickrChoosePhoto():
    #click upload
    upload_pos=scrseek.positionOf('fl_choose_btn.png')
    upload_pos = [x+15 for x in upload_pos]
    kmi.Click(upload_pos[0],upload_pos[1])

def Paste_Filename(file_name):
    #paste file name
    kmi.clip_board.copy(file_name)
    kmi.HoldKey(ctrl,v_key)
    sleep(.61)
    #press enter upload file
    kmi.TapKey(enter_key)

def Load_EXIFData(file_name):
    #load file comment
    print(file_name)
    e_data=md.getEXIFTags(file_name)
    if e_data == False:
        return False
    else:
        image_comment=e_data['Comment']
        return image_comment

def Click_FlickrTags():
    #click upload
    tags_pos=scrseek.positionOf('fl_tags_btn.png')
    tags_pos = [x+15 for x in tags_pos]
    kmi.Click(tags_pos[0],tags_pos[1])

def Paste_Tags(tags):
    #paste title
    kmi.clip_board.copy(tags)
    print(tags)
    kmi.HoldKey(ctrl,v_key)
    kmi.TapKey(enter_key)

def Click_Upload():
    #click share
    share_pos=scrseek.positionOf('fl_submit_upload_btn.png')
    kmi.Click(share_pos[0]+20,share_pos[1]+8)


def Submit_FL(fn,comment=""):
    os.chdir(path_flickr)
    #Tap escape twice to clear 
    kmi.MultiTap(esc_key,3)
    sleep(1)
    #click upload
    Click_FlickrUpload()
    sleep(7)
    #click choose photo
    Click_FlickrChoosePhoto()
    sleep(3)
    #paste file name
    Paste_Filename(fn)
    sleep(17)
    #Load file and get EXIF data
    comment=Load_EXIFData(fn)
    #If comment data not load return false, we are only working with commented images
    if not comment:
        return False
    #click tags
    Click_FlickrTags()
    sleep(1)
    #paste post contents
    Paste_Tags(comment[comment.rfind('\n')+1:])
    sleep(1)
    #click upload
    Click_Upload()
    sleep(1)
    #click upload
    Click_Upload()
    sleep(1)
    return True

def Submit_Folder(folder,delay=60):
    Click_Chrome()
    sleep(3)
    #click address bar
    Click_Addressbar()
    sleep(1)
    #copy and paste address for FB
    Paste_FlickrAddress()
    sleep(10)
    for file in os.listdir(folder):
        if '.jpg' in file:
            print(file)
            #Submit file from folder
            Submit_FL(folder+"\\"+file)
            sleep(delay)

if __name__ == "__main__":
    print "Submit_Folder(your_folder_here)"
