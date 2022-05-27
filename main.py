#Made by Alex

#======Libraries======
import tkinter as tk
import tkinter.ttk as ttk
import random

#======Main Window======
MainWindow = tk.Tk()
MainWindow.title("Cookie RPG") #Window title
MainWindow.configure(background = "#555555") #Window background color
MainWindow.geometry("720x480") #Resolution
MainWindow.resizable(0,0) #Disables resizing

#======Variables======
BgColor = "#555555"
FgColor = "#64A6D0"
PlayerHP = tk.IntVar()
PlayerHP.set(100)
EnemyHP = tk.IntVar()
EnemyHP.set(100)
PlayerHPSubtrahend = tk.IntVar()
EnemyHPSubtrahend = tk.IntVar()
PlayerHPAddend = tk.IntVar()

#======Functions======
def enemyAttack():
    global PlayerHP
    PlayerHPSubtrahend.set(random.randint(0, 16))
    PlayerHP.set(PlayerHP.get() - PlayerHPSubtrahend.get())
    if PlayerHP.get() <= 0:
        PlayerHP.set(0)
        y.pack_forget()
        x.pack_forget()
        lose.pack()
        return
def attack():
    global EnemyHP
    EnemyHPSubtrahend.set(random.randint(0, 16))
    EnemyHP.set(EnemyHP.get() - EnemyHPSubtrahend.get())
    if EnemyHP.get() <= 0:
        EnemyHP.set(0)
        y.pack_forget()
        x.pack_forget()
        win.pack()
        return
    enemyAttack()
def heal():
    global PlayerHP
    PlayerHPAddend.set(random.randint(0,16))
    PlayerHP.set(PlayerHP.get() + PlayerHPAddend.get())
    if PlayerHP.get() >= 100:
        PlayerHP.set(100)
    enemyAttack()



#======Frames======
PlayerFrame = tk.Frame(MainWindow, bg = BgColor)
PlayerFrame.pack(fill = "both")

EnemyFrame = tk.Frame(MainWindow, bg = BgColor)
EnemyFrame.pack(fill = "both")

MainFrame = tk.Frame(MainWindow, bg = BgColor)
MainFrame.pack() #Do not use fill = "both" because it takes up as much space as possible for the buttons.

SubtrahendPlayerFrame = tk.Frame(MainWindow, bg = BgColor)
SubtrahendPlayerFrame.pack(fill = "both")

SubtrahendEnemyFrame = tk.Frame(MainWindow, bg = BgColor)
SubtrahendEnemyFrame.pack(fill = "both")

#======Content======
Label_PlayerHPText = tk.Label(PlayerFrame, text = "Your health:", font = "Arial 64", bg = BgColor, fg = FgColor)
Label_PlayerHPText.grid(row = 0, column = 0)

Label_PlayerHP = tk.Label(PlayerFrame, textvariable = PlayerHP, font = "Arial 64", bg = BgColor, fg = FgColor)
Label_PlayerHP.grid(row = 0, column = 1)

Label_EnemyHPText = tk.Label(EnemyFrame, text = "Their health:", font = "Arial 64", bg = BgColor, fg = FgColor)
Label_EnemyHPText.grid(row = 0, column = 0)

Label_EnemyHP = tk.Label(EnemyFrame, textvariable = EnemyHP, font = "Arial 64", bg = BgColor, fg = FgColor)
Label_EnemyHP.grid(row = 0, column = 1)

y = tk.Button(MainFrame, text = "Attack", font = "Arial 32", bg = BgColor, fg = FgColor, command = attack)
y.pack(side = tk.LEFT)

x = tk.Button(MainFrame, text = "Heal", font = "Arial 32", bg = BgColor, fg = FgColor, command = heal)
x.pack(side = tk.RIGHT)

Label_PlayerHPSubtrahendText = tk.Label(SubtrahendPlayerFrame, text = "Damage taken:", font = "Arial 48", bg = BgColor, fg = FgColor)
Label_PlayerHPSubtrahendText.grid(row = 0, column = 0)

Label_PlayerHPSubtrahend = tk.Label(SubtrahendPlayerFrame, textvariable = PlayerHPSubtrahend, font = "Arial 48", bg = BgColor, fg = FgColor)
Label_PlayerHPSubtrahend.grid(row = 0, column = 1)

Label_EnemyHPSubtrahendText = tk.Label(SubtrahendEnemyFrame, text = "Damage given:", font = "Arial 48", bg = BgColor, fg = FgColor)
Label_EnemyHPSubtrahendText.grid(row = 0, column = 0)

Label_EnemyHPSubtrahend = tk.Label(SubtrahendEnemyFrame, textvariable = EnemyHPSubtrahend, font = "Arial 48", bg = BgColor, fg = FgColor)
Label_EnemyHPSubtrahend.grid(row = 0, column = 1)

win = tk.Label(MainFrame, text = "You win!", font = "Arial 48", bg = BgColor, fg = FgColor)

lose = tk.Label(MainFrame, text = "You lose!", font = "Arial 48", bg = BgColor, fg = FgColor)

#======Main Window Loop======
MainWindow.mainloop()