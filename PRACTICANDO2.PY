import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print(screenWidth, screenHeight)
print(currentMouseX, currentMouseY)

x,y = 180,70
w=0
while w<1:
    x,y = 180,70
    pyautogui.click(x, y,clicks=3)
    pyautogui.write(
# ---link de html y css 
#'https://www.youtube.com/watch?v=ELSm-G201Ls'  
#----link de javasscript 
#'https://www.youtube.com/watch?v=z95mZVUcJ-E'
#-----prueba de youtube 
'https://www.youtube.com/watch?v=7HOb6yA-lm8&list=RDGMEMCMFH2exzjBeE_zAHHJOdxgVM7HOb6yA-lm8&start_radio=1'
,interval=0.01)
    w+=1
    
    pyautogui.press('enter')
x,y = 500,500
pyautogui.click(x, y, clicks=2, interval=4)


