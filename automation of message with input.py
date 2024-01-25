import pyautogui as pyg
import time
a = input("enter your word and then click where you want to send")
time.sleep(5)
count = 0
while count<=5:
    pyg.typewrite(a)
    pyg.press("enter")
    count=count+1

