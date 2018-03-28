import blogger
import deviantart
import facebook
import flickr
import googleplus
import instagram
import tumblr
import mastodonxyz

import mouse_keyboard_input as kmi
import scrseek

from time import sleep
import os
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

path_core=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def Clear_ScreensaverAndDialog():
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)

def Click_Chrome():
    #click google chrome
    os.chdir(path_core)
    chrome_btn=scrseek.positionOf('chrome_taskbar.png')
    chrome_btn=[x+30 for x in chrome_btn]
    kmi.Click(*chrome_btn)
    sleep(.21)
    kmi.HoldKey(win_key,up_arrow)
    sleep(1)

def Click_Addressbar():
    #click address bar
    kmi.Click(420,50)

def Device_Mode_Activate():
    os.chdir(path_core)
    kmi.HoldKey(ctrl,shift_key,i_key)
    sleep(10)
    dm_pos=scrseek.positionOf('devicemode_unselected.png')
    kmi.Click(dm_pos[0]+50,dm_pos[1]+15)

def Device_Mode_Deactivate():
    os.chdir(path_core)
    dm_pos=scrseek.positionOf('devicemode_selected.png')
    kmi.Click(dm_pos[0]+50,dm_pos[1]+15)
    sleep(5)
    kmi.HoldKey(ctrl,shift_key,i_key)

def Blogger_Post(filename):
    #blogger section
    Click_Addressbar()
    sleep(2)
    blogger.Paste_bloggerAddress()
    sleep(7)
    blogger.Submit_Blogger(filename)

def DeviantArt_Post(filename):
    #deviantart
    Click_Addressbar()
    sleep(2)
    deviantart.Paste_Address()
    sleep(7)
    deviantart.Submit_DA(filename)

def Facebook_Post(filename):
    #facebook
    Click_Addressbar()
    sleep(2)
    facebook.Paste_FacebookAddress()
    sleep(7)
    facebook.Submit_FB(filename)

def Flickr_Post(filename):
    #flickr
    Click_Addressbar()
    sleep(2)
    flickr.Paste_FlickrAddress()
    sleep(7)
    flickr.Submit_FL(filename)

def GooglePlus_Post(filename):
    #google plus
    Click_Addressbar()
    sleep(2)
    googleplus.Paste_GooglePlusAddress()
    sleep(7)
    googleplus.Submit_GP(filename)

def Instagram_Post(filename):
    #instagram
    Device_Mode_Activate()
    sleep(2)
    Click_Addressbar()
    sleep(2)
    instagram.Paste_InstagramAddress()
    sleep(7)
    instagram.Submit_IG(filename)
    sleep(2)
    Device_Mode_Deactivate()

def Tumblr_Post(filename):
    #tumblr
    Click_Addressbar()
    sleep(2)
    tumblr.Paste_TumblrAddress()
    sleep(7)
    tumblr.Submit_TB(filename)

def Mastodonxyz_Post(filename):
    #tumblr
    Click_Addressbar()
    sleep(2)
    mastodonxyz.Paste_mastodonxyzAddress()
    sleep(7)
    mastodonxyz.Submit_mastodonxyz(filename)

def Submit_All(filename):
    os.chdir(path_core)
    #Set up
    Click_Chrome()
    sleep(7)
    #blogger section
    Blogger_Post(filename)
    sleep(7)
    #deviantart
    DeviantArt_Post(filename)
    sleep(7)
    #facebook
    Facebook_Post(filename)
    sleep(7)
    #flickr
    Flickr_Post(filename)
    sleep(7)
    #google plus
    GooglePlus_Post(filename)
    sleep(7)
    #tumblr
    Tumblr_Post(filename)
    sleep(7)
    #instagram
    Instagram_Post(filename)

def Submit_Folder(folder,delay=120):
    os.chdir(path_core)
    Click_Chrome()
    sleep(3)
    for file in os.listdir(folder):
        if '.jpg' in file:
            print(file)
            #Submit file from folder
            Submit_All(folder+"\\"+file)
            sleep(delay)

def test_mode():
    sleep(3)
    Click_Chrome()
    sleep(3)
    mastodonxyz.Submit_Folder("K:\\art\\script_drawing\\x-men")