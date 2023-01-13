import time
import os
from pywinauto import mouse
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from selenium import webdriver
import win32api

# For mp4Folder and spotifyFolder, put {SPACE} to replace spaces in your path, ie:
vlcPath = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"  # Copy path of vlc.exe
PATH = "C:\Program Files (x86)\chromedriver.exe"  # Copy path of chromedriver.exe
mp4Folder = r"C:\Users\Bob{SPACE}K\Desktop\mp4Dump"  # Copy path to folder to hold mp4s
mp4FolderDirectory = r"C:\Users\Bob K\Desktop\mp4Dump"  # Copy actual path
spotifyFolder = r"C:\Users\Bob{SPACE}K\Desktop\Spotify{SPACE}Music"  # Copy path of spotify local files folder

url = str(input("Enter YT link or type 'EXIT' to stop: "))
while url != "EXIT":
    driver = webdriver.Chrome(PATH)
    driver.get(url)
    title = str(driver.title) + ".mp4"
    driver.close()
    print("Title: " + title)
    print("opening vlc...")
    app = Application(backend="uia").start(cmd_line=vlcPath)
    media = app.VLCmediaplayer.child_window(title="Media Alt+M", control_type="MenuItem").wrapper_object()
    media.click_input()
    media.click_input()
    send_keys("^n", with_spaces=False)
    send_keys("^v", with_spaces=False)
    send_keys("{ENTER 1}", with_spaces=False)
    send_keys("^j", with_spaces=False)
    time.sleep(5)
    codec = app.CurrentMediaInformation.child_window(title="Location:", control_type="Text").wrapper_object()
    codec.click_input()
    x, y = win32api.GetCursorPos()
    mouse.click(button='left', coords=(x + 75, y))
    time.sleep(2)
    send_keys('^a')
    time.sleep(2)
    send_keys('^c')
    time.sleep(1)
    send_keys('%{F4}')
    send_keys('%{F4}')
    time.sleep(1)
    send_keys("^v", with_spaces=False)
    time.sleep(1)
    downloadUrl = input(send_keys("{ENTER 1}", with_spaces=False))
    driver = webdriver.Chrome(PATH)
    driver.get(downloadUrl)
    time.sleep(1)
    send_keys("^s", with_spaces=False)
    time.sleep(2)
    send_keys(title)
    send_keys("^L")
    send_keys(mp4Folder)
    time.sleep(1)
    send_keys("{ENTER}")
    time.sleep(1)
    send_keys('{ENTER}')
    send_keys('{ENTER}')
    send_keys('{ENTER}')
    print('\nBeginning file download...')
    time.sleep(5)
    while True:
        downloaded_files = os.listdir(mp4FolderDirectory)
        if any(file.endswith('.crdownload') for file in downloaded_files):
            time.sleep(1)
        else:
            print('Download complete.')
            print("opening vlc...")
            break
    driver.close()

    # Reformatting .mp4 file to valid .mp3 file:

    app2 = Application(backend="uia").start(cmd_line=vlcPath)
    media = app2.VLCmediaplayer.child_window(title="Media Alt+M", control_type="MenuItem").wrapper_object()
    media.click_input()
    media.click_input()
    send_keys("^r", with_spaces=False)
    add = app2.VLCmediaplayer.child_window(title="Open Media", control_type="Window").child_window(
        title="File Selection", control_type="Group").child_window(title="Add...",
                                                                   control_type="Button").wrapper_object()
    add.click_input()
    send_keys("^L")
    send_keys(mp4Folder)
    send_keys("{ENTER}")
    send_keys("%n")
    send_keys(title)
    send_keys("{ENTER}")
    convertSave = app2.VLCmediaplayer.child_window(title="Open Media", control_type="Window").child_window(
        title="Convert / Save Alt+o", control_type="MenuItem")
    convertSave.click_input()
    destination = app2.Convert.child_window(title="Destination", control_type="Group").child_window(
        title="Browse Enter", control_type="Button").wrapper_object()
    destination.click_input()
    send_keys("{RIGHT}", with_spaces=False)
    for i in range(12):
        send_keys("{BACKSPACE}", with_spaces=False)
    send_keys("^L")
    send_keys(spotifyFolder)
    time.sleep(1)
    send_keys("{ENTER}")
    time.sleep(1)
    send_keys('{ENTER}')
    send_keys('{ENTER}')
    send_keys('{ENTER}')
    start = app2.Convert.GroupBox4.child_window(title="Start Alt+S", control_type="Button").wrapper_object()
    start.click_input()
    print("Done! " + title[0:-4] + " Has been uploaded to your spotify local files")
    url = str(input("Enter YT link or type 'EXIT' to stop: "))