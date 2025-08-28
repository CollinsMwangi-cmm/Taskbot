import pyautogui
import time

## monitor Size(width=1920, height=1080)
## import pyautogui
## pyautogui.mouseInfo()

def playAlexRider():
    pyautogui.click(32,1044) #click start button
    time.sleep(0.5) #wait for 1 second
    pyautogui.click(833,243) # click all button
    time.sleep(0.5)
    #move mouse to a scrollable area
    pyautogui.moveTo(593,492)
    time.sleep(.5)
    #scroll
    pyautogui.scroll(-4240) 
    time.sleep(1)
    #click music app button
    pyautogui.click(566,533)
    time.sleep(8)
    #click playlist button
    pyautogui.click(119,942)
    time.sleep(0.5)
    #click a list in the playlist
    pyautogui.click(179,487)
    time.sleep(5)
    #click play all button in the playlist
    pyautogui.click(975,287)
    time.sleep(5)
    
def playAllBtn():
    #click play all button
    pyautogui.click(975,287)
    time.sleep(5)
    
    
def playPlaylist():
    pyautogui.click(32,1044) #click start button
    time.sleep(0.5) #wait for 1 second
    pyautogui.click(833,243) # click all button
    time.sleep(0.5)
    #move mouse to a scrollable area
    pyautogui.moveTo(593,492)
    time.sleep(.5)
    #scroll
    pyautogui.scroll(-4240) 
    time.sleep(1)
    #click music app button
    pyautogui.click(566,533)
    time.sleep(8)
    #click playlist button
    pyautogui.click(119,942)
    time.sleep(0.5)
    pyautogui.click(237,542)
    time.sleep(0.5)
    playAllBtn()
    
def pause():
    #click play/pause
    pyautogui.click(964,939)
    time.sleep(0.5)

def next():
    #click next button
    pyautogui.click(1100,938)
    time.sleep(5)

def prev():
    #click previous button
    pyautogui.click(1100,938)
    time.sleep(5)
    
    
# spotify controls and music app controls
def play():
    pyautogui.click(32,1044) #click start button
    time.sleep(1)
   
    pyautogui.click(954,438) #click next page
    time.sleep(1)
    pyautogui.click(710,330) #click spotify app
    pyautogui.press('win', 'up')








