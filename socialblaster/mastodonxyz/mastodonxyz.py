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

path_mastodonxyz=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def Click_ScreensaverAway():
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)

def Click_Addressbar():
    #click address bar
    kmi.Click(420,50)

def Paste_mastodonxyzAddress():
    #copy and paste address for mastodonxyz AND hit enter key
    kmi.clip_board.copy("https://mastodon.xyz/web/timelines/public")
    kmi.HoldKey(ctrl,a_key)
    kmi.HoldKey(ctrl,v_key)
    sleep(1)
    #press enter to go to address
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

def Click_Messagebox():
    #click next button
    next_pos=scrseek.positionOf('mastodonxyz_message_box.png')
    next_pos = [x+15 for x in next_pos]
    kmi.Click(next_pos[0],next_pos[1])

def Paste_Caption(comment):
    #paste title
    kmi.clip_board.copy(comment)
    print(comment)
    kmi.HoldKey(ctrl,v_key)
    sleep(1)
    kmi.TapKey(enter_key)

def Click_PostPhotoButton():
    #click next button
    next_pos=scrseek.positionOf('mastodonxyz_post_photo.png')
    next_pos = [x+15 for x in next_pos]
    kmi.Click(next_pos[0],next_pos[1])

def Paste_Filename(file_name):
    #paste file name
    kmi.clip_board.copy(file_name)
    kmi.HoldKey(ctrl,v_key)
    sleep(.61)
    #press enter upload file
    kmi.TapKey(enter_key)

def Click_Toot():
    #click share
    share_pos=scrseek.positionOf('mastodonxyz_toot_btn.png')
    kmi.Click(share_pos[0]+20,share_pos[1]+8)

def Submit_mastodonxyz(fn,comment=""):
    os.chdir(path_mastodonxyz)
    #Tap escape twice to clear 
    kmi.MultiTap(esc_key,3)
    sleep(5)
    Click_Messagebox()
    sleep(2)
    #Load file and get EXIF data
    comment=Load_EXIFData(fn)
    #If comment data not load return false, we are only working with commented images
    if not comment:
        return False
    #paste post contents
    Paste_Caption(comment)
    sleep(1)
    #click post photo button
    Click_PostPhotoButton()
    sleep(3)
    #paste file name
    Paste_Filename(fn)
    sleep(17)
    #click share
    Click_Toot()
    sleep(1)
    return True

def Submit_Folder(folder,delay=60):
    #click address bar
    Click_Addressbar()
    sleep(1)
    #copy and paste address for mastodonxyz
    Paste_mastodonxyzAddress()
    sleep(10)
    for file in os.listdir(folder):
        if '.jpg' in file:
            print(file)
            #Submit file from folder
            Submit_mastodonxyz(folder+"\\"+file)
            sleep(delay)


if __name__ == "__main__":
    print "Submit_Folder(your_folder_here)"