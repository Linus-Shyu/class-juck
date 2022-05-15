#导入整活儿所需要的库


import pyautogui
import time

from sqlalchemy import true


#等待鼠标位置移动好
time.sleep(5)  


#哈哈哈，马上就开始吧
while true:
    pyautogui.typewrite('hihihim')
    pyautogui.typewrite(['enter'])
    time.sleep(1)

    stop=input('')
    pyautogui.typewrite(['enter'])
    if(stop=='c'):
        print("再见")
        break