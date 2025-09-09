import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print(screenWidth, screenHeight)
print(currentMouseX, currentMouseY)

x,y = 1599,913
pyautogui.click(x, y)
w=0
while w<3:
    x,y = 1599,913
    pyautogui.click(x, y)
    pyautogui.write('Hello', interval=0.01)  
    w+=1
    
    pyautogui.press('enter')