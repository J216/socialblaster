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

path_blogger=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def Click_ScreensaverAway():
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)
    sleep(3)
    kmi.TapKey(esc_key)

def Click_Chrome():
    #click google chrome
    os.chdir('c:/scr')
    ff_btn=scrseek.positionOf('..//chrome_taskbar.png')
    ff_btn=[x+30 for x in ff_btn]
    kmi.Click(*ff_btn)
    sleep(.21)
    kmi.HoldKey(win_key,up_arrow)
    sleep(1)

def Click_Addressbar():
    #click address bar
    kmi.Click(420,50)

def Paste_bloggerAddress():
    #copy and paste address for FB AND hit enter key
    kmi.clip_board.copy("https://www.blogger.com/blogger.g?blogID=8839635347814454641#allposts/postNum=0")
    kmi.HoldKey(ctrl,a_key)
    kmi.HoldKey(ctrl,v_key)
    sleep(1)
    #press enter to go to address
    kmi.TapKey(enter_key)

def Click_NewPost():
    #click upload
    upload_pos=scrseek.positionOf('blogger_new_post_btn.png')
    upload_pos = [x+15 for x in upload_pos]
    kmi.Click(upload_pos[0],upload_pos[1])

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

def Click_PostTitle():
    ##click upload
    tags_pos=scrseek.positionOf('blogger_post_title_btn.png')
    tags_pos = [x+15 for x in tags_pos]
    kmi.Click(tags_pos[0],tags_pos[1])

def Paste_PostTitle(title):
    #paste title 
    kmi.clip_board.copy(title)
    kmi.HoldKey(ctrl,v_key)

def Tab_PostText():
    #tab to post title
    kmi.MultiTap(tab, 7)

def Click_InsertImage():
    #click upload
    tags_pos=scrseek.positionOf('blogger_insert_image_btn.png')
    tags_pos = [x+15 for x in tags_pos]
    kmi.Click(tags_pos[0],tags_pos[1])

def Click_ChooseFile():
    #click upload
    tags_pos=scrseek.positionOf('blogger_upload choose_file_btn.png')
    tags_pos = [x+15 for x in tags_pos]
    kmi.Click(tags_pos[0],tags_pos[1])

def Paste_Filename(file_name):
    #paste file name
    kmi.clip_board.copy(file_name)
    kmi.HoldKey(ctrl,v_key)
    sleep(.61)
    #press enter upload file
    kmi.TapKey(enter_key)

def Click_AddSelected():
    #click upload
    tags_pos=scrseek.positionOf('blogger_upload_add_selection_btn.png')
    tags_pos = [x+15 for x in tags_pos]
    kmi.Click(tags_pos[0],tags_pos[1])

def Paste_PostText(post_text):
    #paste title 
    kmi.clip_board.copy(post_text)
    kmi.HoldKey(ctrl,v_key)

def Click_Image():
    #click upload
    tags_pos=scrseek.positionOf('blogger_A_btn.png')
    kmi.Click(tags_pos[0],tags_pos[1]+100)

def Click_ImageXL():
    #click upload
    tags_pos=scrseek.positionOf('blogger_xlarge_btn.png')
    tags_pos = [x+10 for x in tags_pos]
    kmi.Click(tags_pos[0],tags_pos[1])

def Click_Labels():
    #click upload
    tags_pos=scrseek.positionOf('blogger_label_btn.png')
    tags_pos = [x+10 for x in tags_pos]
    kmi.Click(tags_pos[0],tags_pos[1])

def Paste_Tags(tags):
    #paste tags
    kmi.clip_board.copy(tags.replace('#','').replace('\n',''))
    print(tags.replace('#','').replace('\n',''))
    kmi.HoldKey(ctrl,v_key)
    kmi.TapKey(enter_key)

def Click_Done():
    #click upload
    tags_pos=scrseek.positionOf('blogger_done_btn.png')
    tags_pos = [x+10 for x in tags_pos]
    kmi.Click(tags_pos[0]+10,tags_pos[1])

def Click_Location():
    #click share
    share_pos=scrseek.positionOf('blogger_location_btn.png')
    kmi.Click(share_pos[0]+20,share_pos[1]+8)
    sleep(1)
    kmi.TapKey(tab)

def Paste_Location():
    #paste location
    location = "Saint Joseph, MO"
    kmi.clip_board.copy(location)
    print(location)
    kmi.HoldKey(ctrl,v_key)
    kmi.TapKey(enter_key)

def Click_Location_Done():
    #click upload
    tags_pos=scrseek.positionOf('blogger_location_done_btn.png')
    tags_pos = [x+10 for x in tags_pos]
    kmi.Click(tags_pos[0]+10,tags_pos[1])

def Click_Publish():
    #click upload
    tags_pos=scrseek.positionOf('blogger_publish_btn.png')
    tags_pos = [x+15 for x in tags_pos]
    kmi.Click(tags_pos[0]+10,tags_pos[1])

def Submit_Blogger(fn,comment=""):
    #Set path to blogger folder
    os.chdir(path_blogger)
    #click new post
    Click_NewPost()
    sleep(6)
    exif_data=Load_EXIFData(fn)
    if len(exif_data) < 2:
        return False
    Click_PostTitle()
    sleep(2)
    Paste_PostTitle(exif_data[1])
    sleep(2)
    Tab_PostText()
    sleep(2)
    Click_InsertImage()
    sleep(6)
    Click_ChooseFile()
    sleep(5)
    Paste_Filename(fn)
    sleep(12)
    Click_AddSelected()
    sleep(4)
    if comment =="":
        Paste_PostText(exif_data[0].replace(exif_data[1]+'\n','').replace(exif_data[2],''))
    else:
        Paste_PostText(comment)
    sleep(3)
    Click_Image()
    sleep(2)
    Click_ImageXL()
    sleep(2)
    Click_Labels()
    sleep(2)
    Paste_Tags(exif_data[2])
    sleep(2)
    Click_Done()
    sleep(2)
    Click_Location()
    sleep(2)
    Paste_Location()
    sleep(2)
    Click_Location_Done()
    sleep(2)
    Click_Publish()
    return True

def Submit_Folder(folder,delay=60):
    os.chdir(blogger_path)
    Click_Chrome()
    sleep(3)
    #click address bar
    Click_Addressbar()
    sleep(1)
    #copy and paste address for FB
    Paste_bloggerAddress()
    sleep(10)
    for file in os.listdir(folder):
        if '.jpg' in file:
            print(file)
            #Submit file from folder
            Submit_Blogger(folder+"\\"+file)
            sleep(delay)

if __name__ == "__main__":
    fldname='K:\\art\\script_drawing\\x-men'
    Submit_Folder(fldname)

