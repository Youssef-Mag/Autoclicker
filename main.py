import pyautogui
import time
import threading
from tkinter import *
import keyboard

interval = 1
isClicking = False
button = ""

def click():
    global isClicking, interval, window
    isClicking = True
    print(f"Clicking Every {interval}s ..")

def unClick():
    global isClicking
    isClicking = False
    print("Stopped Clicking..")

#Thread that runs when clicking and terminates itself when its done
def loop():
    while True:
        if isClicking:
            time.sleep(interval)
            pyautogui.click(button=button)
        else:
            break


class Window:
    def __init__(self):
        self.isClicking = False
        #Hotkeys to start and stop clicking
        keyboard.add_hotkey('ctrl+shift+c', self.start)
        keyboard.add_hotkey('ctrl+shift+s', self.stop)
        #Setting up the GUI
        self.root = Tk()
        self.root.title("Autoclicker")
        self.intervalFrame = Frame(self.root)
        self.intervalLabel = Label(self.intervalFrame, text="Interval:", font=15)
        self.intervalText = Entry(self.intervalFrame, width=5, font=15)
        self.intervalText.insert(0, "1")
        self.intervalText.focus()

        self.buttonFrame = Frame(self.root)
        self.buttonLabel = Label(self.buttonFrame, text="Button:", font=15)
        self.leftClickButton = Button(self.buttonFrame, text="Left", font=15, command=self.setLeftClick)
        self.rightClickButton = Button(self.buttonFrame, text="Right", font=15, command=self.setRightClick)

        self.clickButton = Button(self.root, text= "Start", font=15, width=20, command=self.start)

        self.hotkeyLabel = Label(self.root, text='"ctrl+shift+c" to start, "ctrl+shift+s" to stop', font=("Arial", 10), fg="gray")
        self.creditLabel = Label(self.root, text='Made by Youssef Magdi', font=("Arial", 9), fg="gray")

        self.intervalFrame.pack(ipady=10, padx=100)
        self.intervalLabel.pack(side="left")
        self.intervalText.pack(side="left")

        self.buttonFrame.pack(padx=5)
        self.buttonLabel.pack(side="left")
        self.leftClickButton.pack(side="left")
        self.rightClickButton.pack(side="left")

        self.clickButton.pack(side="top", padx=10, pady=10)

        self.hotkeyLabel.pack()
        self.creditLabel.pack()

        self.setLeftClick()

        self.root.mainloop()
    
    #To start the clicker thread
    def start(self):
        global interval, isClicking
        interval = eval(self.intervalText.get())
        self.clickButton.configure(text = "Stop", relief="sunken", command=self.stop)
        click()
        threading.Thread(target = loop).start()
        
    #To stop the clicker thread
    def stop(self):
        global isClicking
        self.clickButton.configure(text = "Start", relief="raised", command=self.start)
        unClick()
    
    #To make it use right click
    def setRightClick(self):
        global button
        button = "right"
        self.rightClickButton.configure(relief="sunken")
        self.leftClickButton.configure(relief="raised")

    #To make it use left click
    def setLeftClick(self):
        global button
        button = "left"
        self.leftClickButton.configure(relief="sunken")
        self.rightClickButton.configure(relief="raised")

window = Window()