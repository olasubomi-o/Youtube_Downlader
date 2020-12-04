#Tkinter for GUI, pytube for youtube downloading

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


Folder_Name = "" # Sort of placeholder for the folder path

#file location
def openLocation():
    global Folder_Name # We are calling the folder  name/path placeholder which is outside the function
    Folder_Name=filedialog.askdirectory() # prompt user to choose a file path
    if (len(Folder_Name) >1): #if statement to make sure a folder path is selected
        locationError.config(text=Folder_Name,fg='green')
    else:
        locationError.config(text="Please Choose Folder!!",fg="red")


#Download video
def DownloadVideo():
    choice=ytdchoices.get() #Choice video quality
    url=ytdEntry.get() #Get Url

    if(len(url)>1):
        ytdError.config(text="")
        yt= YouTube(url)

        if(choice==choices[0]):
            select= yt.streams.filter(progressive=True).first()
        elif(choice==choices[1]):
            select = yt.streams.filter(progressive=True).last()
        elif (choice==choices[2]):
            select=yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Paste Link Again!!",fg="red")

#download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed")

root = Tk()# To generate tkinter functions
root.title ("YTD Downloader")# Title
root.geometry("350x400") #set window size
root.columnconfigure(0,weight=1) # set all content to center, play with it later

#YTD Link Label

ytdLabel= Label(root,text="Enter the URL of the Video", font=("jost",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar=StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error MSg
ytdError= Label(root,text='Error MSg',fg="red",font=("jost",10))
#Save Label
saveLabel= Label(root,text="Save the video File", font=("jost",15,"bold"))
saveLabel.grid()

#btn of Change path
saveEntry= Button(root,width=10,fg="red",bg="red",text='Choose Path',command=openLocation)
saveEntry.grid()

locationError= Label(root,text="Error message of path", fg="red", font=('jost',10))
locationError.grid()

#Download Quality
selectQuality= Label(root,text='Select Quality', fg='black', font=("jost",15))
selectQuality.grid()

#Choosequality
choices=['720p','144p','only audio']
ytdchoices= ttk.Combobox(root,values=choices)
ytdchoices.grid()

#download btn
downloadbtn= Button(root,text="Download",width=10,bg="red",fg='Black',command=DownloadVideo)
downloadbtn.grid()

#Developer Label

developerLabel= Label(root, text="Olasubomi Olawepo",font=("jost",10))
developerLabel.grid()

root.mainloop()