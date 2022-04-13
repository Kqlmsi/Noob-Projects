from tkinter import *
import pytube
from pytube import YouTube


#SETTING WINDOW RESOLUTON & APP TITLE
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('Youtube Video Downloader')

#SETTING THE FONT OF THE TEXT IN SAID WINDOW
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

#VARIABLE THAT STORES THE YOUTUBE LINK THAT YOU INPUT
link = StringVar()

#
Label(root, text = 'Paste link here:', font = 'arial 15 bold').place(x=160 , y=60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

#DOWNLOAD FUNCTION -- MUST INSERT VIDEO DIRECTORY IN LINE 26 IN PARENTHESES
def Downloader():
	url = YouTube(str(link.get()))
	video = url.streams.get_highest_resolution()
	video.download()
	Label(root, text='DOWNLOADED', font = 'arial 15').place(x=180,y=210)

#BUTTON
Button(root,text='DOWNLOAD', font='arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180,y=150)

root.mainloop()
