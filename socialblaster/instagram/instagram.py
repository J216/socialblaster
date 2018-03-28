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

path_instagram=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def Click_ScreensaverAway():
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)

def Click_Chrome():
    #click google chrome
    ff_btn=scrseek.positionOf('../chrome_taskbar.png')
    ff_btn=[x+30 for x in ff_btn]
    kmi.Click(*ff_btn)
    sleep(.21)
    kmi.HoldKey(win_key,up_arrow)
    sleep(1)

def Device_Mode():
    kmi.HoldKey(ctrl,shift_key,i_key)
    sleep(5)
    dm_pos=scrseek.positionOf('../devicemode_unselected.png')
    kmi.Click(dm_pos[0]+50,dm_pos[1]+15)

def Device_Mode_Deactivate():
    dm_pos=scrseek.positionOf('../devicemode_selected.png')
    kmi.Click(dm_pos[0]+50,dm_pos[1]+15)
    sleep(5)
    kmi.HoldKey(ctrl,shift_key,i_key)


def Multi_Tap(key_press, times, add_enter=False):
    #tabs  give number of tabs and then enters
    for i in range(times):
        kmi.TapKey(key_press)
        sleep(.312)
    if add_enter:
        kmi.TapKey(enter_key)

def Multi_Tab(tabs):
    Multi_Tap(tab,tabs,True)

def Click_Addressbar():
    #click address bar
    kmi.Click(420,50)

def Paste_InstagramAddress():
    #copy and paste address for IG AND hit enter key
    kmi.clip_board.copy("https://www.instagram.com/")
    kmi.HoldKey(ctrl,a_key)
    kmi.HoldKey(ctrl,v_key)
    sleep(1)
    #press enter to go to address
    kmi.TapKey(enter_key)

def Click_Upload():
    #click upload
    upload_pos=scrseek.positionOf('ig_upload_btn.png')
    upload_pos = [x+15 for x in upload_pos]
    kmi.Click(upload_pos[0],upload_pos[1])

def Paste_Filename(file_name):
    #paste file name
    kmi.clip_board.copy(file_name)
    kmi.HoldKey(ctrl,v_key)
    sleep(.61)
    #press enter upload file
    kmi.TapKey(enter_key)

def Click_Nextbutton():
    #click next button
    next_pos=scrseek.positionOf('ig_next_btn.png')
    next_pos = [x+15 for x in next_pos]
    kmi.Click(next_pos[0],next_pos[1])

def Click_Caption():
    #click caption 
    caption_pos=scrseek.positionOf('ig_caption_box.png')
    kmi.Click(caption_pos[0]+14,caption_pos[1]+9)

def Load_EXIFData(file_name):
    #load file comment
    print(file_name)
    e_data=md.getEXIFTags(file_name)
    if e_data == False:
        return False
    else:
        image_comment=e_data['Comment']
        return image_comment

def Paste_Caption(comment):
    #paste title
    kmi.clip_board.copy(comment)
    print(comment)
    kmi.HoldKey(ctrl,v_key)

def Click_Location():
    #click location box
    location_pos=scrseek.positionOf('ig_find_location_box.png')
    kmi.Click(location_pos[0]+60,location_pos[1]+15)
    sleep(1.4)
    kmi.Click(location_pos[0]+60,location_pos[1]+15)

def Click_FindLocation():
    #click location find box
    location_pos=scrseek.positionOf('ig_find_location2_box.png')
    kmi.Click(location_pos[0]+30,location_pos[1]+16)

def Paste_Location():
    #paste location - hardcoded
    kmi.clip_board.copy("Saint Joseph, MO")
    kmi.HoldKey(ctrl,v_key)

def Click_Stjoe():
    #click saint joseph location 
    stjoe_search_pos=scrseek.positionOf('ig_find_saintjoe_box.png')
    kmi.Click(stjoe_search_pos[0]+20,stjoe_search_pos[1]+10)

def Click_Share():
    #click share
    share_pos=scrseek.positionOf('ig_share_btn.png')
    kmi.Click(share_pos[0]+20,share_pos[1]+8)

def Click_ScreensaverAway():
    kmi.Click(600,10)

def Submit_IG(fn,comment=""):
    os.chdir(path_instagram)
    #click upload
    Click_Upload()
    sleep(5)
    #paste file name
    Paste_Filename(fn)
    sleep(17)
    #click next button
    Click_Nextbutton()
    sleep(3)
    #click caption 
    Click_Caption()
    sleep(1.4)
    #Load file and get EXIF data
    comment=Load_EXIFData(fn)
    #If comment data not load return false, we are only working with commented images
    if not comment:
        return False
    #paste title
    Paste_Caption(comment)
    sleep(1)
    #click location box
    Click_Location()
    sleep(3)
    #click location find box
    Click_FindLocation()
    sleep(3)
    #paste location
    Paste_Location()
    sleep(9)
    #click saint joseph location 
    Click_Stjoe()
    sleep(3)
    #click share
    Click_Share()
    sleep(1)
    return True

def Submit_Folder(folder):
    Click_Chrome()
    sleep(3)
    Device_Mode()
    sleep(3)
    #click address bar
    Click_Addressbar()
    sleep(1)
    #copy and paste address for IG
    Paste_InstagramAddress()
    sleep(10)
    for file in os.listdir(folder):
        if '.jpg' in file:
            print(file)
            Submit_IG(folder+"\\"+file)
            sleep(600)
            Click_ScreensaverAway()
            sleep(9)

if __name__ == "__main__":
    print "Submit_Folder(your_folder_here)"