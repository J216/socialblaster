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
page_down=0x22
enter_key=0x0D
a_key=0x41
c_key=0x43
v_key=0x56
left_arrow=0x25
up_arrow=0x26
right_arrow=0x27
down_arrow=0x28
browser = "chrome"
image_preview = True

path_deviantart=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def Click_ScreensaverAway():
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)

def Click_Chrome():
    #click google chrome
    ff_btn=scrseek.positionOf('da_ff_btn.png')
    ff_btn[0]=ff_btn[0]+30
    ff_btn[1]=ff_btn[1]+20
    kmi.Click(*ff_btn)
    sleep(.21)
    kmi.HoldKey(win_key,up_arrow)
    sleep(1)

def Click_AdressBar():
    #click address bar
    kmi.Click(450,50)
    sleep(1)

def Paste_Address():
    #copy and paste address for DA
    kmi.clip_board.copy("https://www.deviantart.com/submit/")
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
        title = image_comment[:image_comment.find('\n')]
        title=title.replace('\n', '')
        hashtags =  image_comment[image_comment.find('#'):]
        return (image_comment, title, hashtags)

def Click_Upload():
    #click upload
    upload_pos=scrseek.positionOf('da_upload_btn.png')
    upload_pos = [x+37 for x in upload_pos]
    kmi.Click(upload_pos[0],upload_pos[1])

def Paste_Filename(fn):
    #paste file name
    kmi.clip_board.copy(fn)
    kmi.HoldKey(ctrl,v_key)
    #press enter upload file
    kmi.TapKey(enter_key)

def Click_NoMature():
    #click no mature content
    size_pos=scrseek.positionOf('da_mature_no.png')
    size_pos = [x+15 for x in size_pos]
    kmi.Click(size_pos[0],size_pos[1])

def Click_OriginalSize():
    #click to set original size
    size_pos=scrseek.positionOf('da_size_dropdown.png')
    size_pos = [x+60 for x in size_pos]
    kmi.Click(size_pos[0],size_pos[1])
    sleep(.71)
    kmi.Click(size_pos[0],size_pos[1])

def Click_Title():
    #click title 
    title_pos=scrseek.positionOf('da_size_dropdown.png')
    kmi.Click(title_pos[0],title_pos[1]+150)

def Paste_Title(title):
    #paste title
    kmi.clip_board.copy(title)
    kmi.HoldKey(ctrl,a_key)
    kmi.HoldKey(ctrl,v_key)

def Paste_Description(comment):
    #paste description
    kmi.clip_board.copy(comment)
    kmi.HoldKey(ctrl,v_key)

def Click_Tags():
    #click tags
    kmi.Click(23,270)
    kmi.MultiTap(down_arrow,3,False)
    tag_pos=scrseek.positionOf('da_tags_txt.png')
    tag_pos = [x+8 for x in tag_pos]
    kmi.Click(tag_pos[0],tag_pos[1])

def Paste_Tags(tags):
    #paste tags
    kmi.clip_board.copy(tags)
    kmi.HoldKey(ctrl,v_key)
    sleep(1)
    kmi.TapKey(enter_key)

def Paste_Category():
    #paste category
    kmi.clip_board.copy('psy')
    kmi.HoldKey(ctrl,v_key)

def Click_Submit():
    #click submit
    submit_pos=scrseek.positionOf('da_final_submit_btn.png')
    submit_pos = [x+20 for x in submit_pos]
    kmi.Click(submit_pos[0],submit_pos[1])

def Submit_DA(fn,comment=""):
    #change path to deviantart
    os.chdir(path_deviantart)
    #load tag data
    exif_data=Load_EXIFData(fn)
    #load file comment
    print(fn)
    if exif_data == False:
        return False
    title=exif_data[1]
    tags=exif_data[2]
    if comment=="":
        comment=exif_data[0]
        print comment
    #file name set for paste
    fn='"'+fn.replace('/','\\')+'"'
    #click upload
    Click_Upload()
    sleep(5)
    #paste file name
    Paste_Filename(fn)
    sleep(20)
    #click no mature content
    Click_NoMature()
    sleep(.5)
    #click to set original size
    Click_OriginalSize()
    sleep(1)
    #click title 
    Click_Title()
    sleep(1.4)
    #paste title
    Paste_Title(title)
    sleep(1)
    #tab to description
    kmi.TapKey(tab)
    sleep(1)
    #paste description
    Paste_Description(comment)
    sleep(1)
    #click tags
    Click_Tags()
    sleep(1)
    #paste tags
    Paste_Tags(tags)
    sleep(1)
    #tab to category
    kmi.TapKey(tab)
    sleep(1)
    #paste category
    Paste_Category()
    sleep(1)
    #tab 5 to select category
    kmi.MultiTap(tab, 5, True)
    sleep(1)
    #click submit
    submit_pos=scrseek.positionOf('da_final_submit_btn.png')
    submit_pos = [x+20 for x in submit_pos]
    kmi.Click(submit_pos[0],submit_pos[1])
    sleep(1)
    return True

def Submit_Folder(folder):
    Click_Chrome()
    #click address bar
    Click_AdressBar()
    sleep(1)
    Paste_Address()
    sleep(17)
    for file in os.listdir(folder):
        if '.jpg' in file:
            print(file)
            Submit_DA(folder+"\\"+file)
            sleep(15)

