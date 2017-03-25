#can be converted into .exe file using py2exe and place into her laptop and trick her to open it.
from Tkinter import *
from PIL import ImageTk,Image
import tkMessageBox as msg
import emoji
from time import sleep
import threading
from threading import Thread
import pyttsx as pt
import mp3play as mp3
import emoji
import os
def play_music():
    a=os.getcwd()
    os.chdir(a)
    #store a mp3 file bsng2.mp3 in the same directory as this
    f=open('bsng2.mp3')
    clip=mp3.load(f.name)
    clip.play()
    sleep(64)
    clip.stop()
    en=pt.init()
    rate=en.getProperty('rate')
    en.setProperty('rate',rate-80)
    #enter name to be pronounced
    en.say("Hey name , I Have One Request; Please TakeCare Of  those ravishing eyes looking at the computer screen and Irresistible Smile Of Yours which are More Precious Than Kohinoor")
    en.runAndWait()
    rate=en.getProperty('rate')
    en.setProperty('rate',rate-80)
    en.say("And Yes I Forgot Tell One Most Important Thing That These Are Not Just For Flirt I Mean All These")
    en.runAndWait()
    sleep(02)
    rate=en.getProperty('rate')
    en.setProperty('rate',rate-80)
    en.say("And One Thing Please Don't Worry About Weight You Are Perfect The Way You Are")
    en.runAndWait()
    sleep(01)
    rate=en.getProperty('rate')
    en.setProperty('rate',rate-80)
    en.say("Hey!............. I .. Have Done Such A Great, Work Don't I Deserve A Smile")
    en.runAndWait()
    sleep(01)
    rate=en.getProperty('rate')
    en.setProperty('rate',rate-80)
    en.say("That's Nice")
    en.runAndWait()
    

def close_window():
    master.destroy()
# in "Name here enter his or her name.
def show_entry_fields():
        global wsh
        print("You Made A Wish For : %s And The Wish Is: %s" % (e1.get(), e2.get()))
        wsh='HEY "Name Here" YOU MADE AN WISH FOR '+(e1.get())+' '+'LAST YEAR :'+(e2.get())

def cde():
    a=Tk()
    msg.showinfo("Title",message=emoji.emojize((":birthday:HAPPY BIRTHDAY SERIOUSLYYYYYYYYYY..............................:cocktail::cocktail:"),use_aliases=True))
    msg.showinfo("HAPPY BIRTHDAY",message=emoji.emojize(("HEY CHASMISS!I COULD NOT THINK OF ANYTHING WITH MY CHARMING WAY :wink::wink:\nSo I Made This"),use_aliases=True))
    msg.showinfo("HAPPY BIRTHDAY",message="Please Never Ever Close The opened Command Prompt window During This Programme Execution (black window)")
    sleep(02)
    a.destroy()
    root=Tk()
    img=ImageTk.PhotoImage(Image.open("sersly.jpg"))
    panel=Label(root,image=img)
    panel.pack(side="top",fill="both",expand="yes")
    msg.showinfo("BDAY",message="Jaldi Picture Close Kar Nhin To Tasveer Bura Manjayegi")
    msg.showinfo("HAPPY BIRTHDAY",message="Please Never Close The opened Command Prompt window (black window)")
    root.mainloop()
    msg.showinfo("For You....",message="Gote Sexy And Passionate Wish Kar")
    master = Tk()
    Label(master, text="FOR WHOM").grid(row=0)
    Label(master, text="WISH").grid(row=1)
    global e1
    e1 = Entry(master)
    global e2
    e2 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
    msg.showinfo("For YOU...",message="please do me a favour by closing all the windows after doing a sexy wish")
    msg.showinfo("HAPPY BIRTHDAY",message="Please Never Close The opened Command Prompt window (black window)")
    master.mainloop()
    a=msg.askyesno("For You....",message=emoji.emojize("Bhala Laguchi Ta ?? :confused::confused: ",use_aliases=True))
    if a:
        b=msg.askyesno("For Me",message="Ebe Ta Jibu Mo saha Baharaku ??")
        if b:
            msg.showinfo("thanks",message="Pura Aneiki Basithilu")

        else:
            f=msg.askyesno("For Me....",message="Do U Always Say No??")
            if f:
                g=msg.askyesno("For Me....",message="R U A SerialKiller or WHAT....??")
                if g:
                    msg.showinfo("For Me....",message="Please Manija Please....")
                    msg.showinfo("For Me....",message="Thank UUUUUUUUUUU")
                else:
                    msg.showinfo("NO....",message="You Are A Killer And A Theif Too\n So Yes Kaha Nhele FIR Kridebi To Against Re because u hve smthng whch belngs to me withut any permission")
            else:
                msg.showinfo("Awsome....",message="Thank UUUUUUUUUUUU")
    else:
        msg.showinfo('Ok',message="This Is Just Beginning Pare Ahuri Excited Things Achi Khali Han Kahide..........")

    msg.showinfo("Hey....",message="8260340709 number re miss call de")


if __name__=='__main__':
    Thread(target=cde).start()
    Thread(target=play_music).start()
