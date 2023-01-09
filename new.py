import win32com.client as comclt
import keyboard
import time
from pynput.keyboard import Key, Listener
wsh= comclt.Dispatch("WScript.Shell")
while True:
    pass
if keyboard.is_pressed("F11"):
    wsh.SendKeys("{BACKSPACE}")
    wsh.SendKeys("climb")
    wsh.SendKeys("{ENTER}")
    wsh.SendKeys("climb")
    wsh.SendKeys("{ENTER}")
    wsh.SendKeys("climb")
    wsh.SendKeys("{ENTER}")
    wsh.SendKeys("push @KLuebbert#0499")
    wsh.SendKeys("{ENTER}")
if keyboard.is_pressed("F10"):
    wsh.SendKeys("push @KLuebbert#0499")
    wsh.SendKeys("{ENTER}")
    