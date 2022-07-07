from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
from turtle import left
from sqlalchemy import within_group
import tweepy
import wget
from PIL import ImageTk, Image
import os
import webbrowser

"""
anchor
n   -   up
s   -   down
e   -   right
w   -   left
ne  -   up right
nw  -   up left
se  -   bottom right
sw  -   bottom left
center  -   center
"""
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
# calling the api 
api = tweepy.API(auth, wait_on_rate_limit=True)
form = Tk()
form.minsize(700,600)
form.maxsize(700,600)
form.resizable(False,False)

lines=[]
def yukle():
    text_file=filedialog.askopenfilename(title="Open Text File", filetypes=(("Text Files","*.txt"),)) #open txt of usernames
    text_file=open(text_file, 'r')
    a=text_file.readlines()
    link['values']=a

#adding labels
link=Combobox(form,font="Arial 14",values=lines)
link.place(x=200,y=530,height=50,width=200)

bannerframe=LabelFrame(form).place(x=20,y=10,width=660,height=220)
ppframe=LabelFrame(form).place(x=40,y=180,width=200,height=200)


takipedilen_label_frame=LabelFrame(form).place(x=240,y=230,width=220,height=75)
takipedilen_label=Label(form,text='Following',font='Arial 14 underline bold').place(x=305,y=235)
takipedilen_text=Label(form,text="",font='Arial 14')
takipedilen_text.place(x=350,y=280,anchor="center")


takipci_label_frame=LabelFrame(form).place(x=460,y=230,width=220,height=75)
takipci_label=Label(form,text='Followers',font='Arial 14 underline bold').place(x=520,y=235)
takipci_text=Label(form,text="",font='Arial 14')
takipci_text.place(x=570,y=280,anchor="center")

tweets_label_frame=LabelFrame(form).place(x=240,y=305,width=220,height=75)
tweets_label=Label(form,text='Tweets',font='Arial 14 underline bold').place(x=315,y=310)
tweets_text=Label(form,text="",font='Arial 14')
tweets_text.place(x=350,y=355,anchor="center")

fav_label_frame=LabelFrame(form).place(x=460,y=305,width=220,height=75)
fav_label=Label(form,text='Favorites',font='Arial 14 underline bold').place(x=525,y=310)
fav_text=Label(form,text="",font='Arial 14')
fav_text.place(x=570,y=355,anchor="center")


description_text=Label(form,text="",font='Arial 14')
description_text.place(x=40,y=455)

username_text=Label(form,text="",font='Arial 14')
username_text.place(x=40,y=420)

nickname_text=Label(form,text="",font='Arial 15 bold')
nickname_text.place(x=40,y=395)

def submit():
    hesap=link.get()
    try:
        a=api.get_user(screen_name=hesap)
    except:
        messagebox.showerror(title="Hata", message="User not found.")
    username="@"+a.screen_name
    nickname=a.name
    followers=a.followers_count
    following=a.friends_count
    desc=a.description
    fav=a.favourites_count
    tweets=a.statuses_count
    pp=a.profile_image_url#[:64]+a.profile_image_url[71:]
    #updating labels
    takipedilen_text.configure(text=following) 
    description_text.configure(text=desc,font="Arial 14",wraplength=600) 
    takipci_text.configure(text=followers)
    username_text.configure(text=username) 
    nickname_text.configure(text=nickname)
    fav_text.configure(text=fav)
    tweets_text.configure(text=tweets)


    if hasattr(a,'description')==True: #check description if its
        description_text.configure(text=desc,font="Arial 14",wraplength=600)  
    else: #else error
        description_text.configure(text="***No description***",font="Arial 14 bold ",width=600)
    if a.protected == True: #checks for protected account, if its protected adding username bold and underline
        nickname_text.configure(fg='red',font='Arial 15 bold underline') 
    else:
        nickname_text.configure(fg='black',font='Arial 15 bold') 

    #banner -----------------------------------------------------------
    #download banner,resize and set it in label
    if hasattr(a,'profile_banner_url')==True:
        try:
            os.remove("tkinter-profile-check-data/banner.png")
        except:
            pass
        banner=a.profile_banner_url
        wget.download(banner,'tkinter-profile-check-data/banner.png')
        banner = Image.open('tkinter-profile-check-data/banner.png')
        banner = banner.resize((657, 217), Image.ANTIALIAS)
        banner = ImageTk.PhotoImage(banner)
        banner_panel = Label(form, image=banner)
        banner_panel.image = banner
        banner_panel.place(x=20,y=9)
    #if there is no banner set the pplabel to"nobanner.png" 
    else:    
        banner = Image.open('tkinter-profile-check-data/nobanner.png')
        banner = banner.resize((657, 217), Image.ANTIALIAS)
        banner = ImageTk.PhotoImage(banner)
        banner_panel = Label(form, image=banner)
        banner_panel.image = banner
        banner_panel.place(x=20,y=9)


    #pp -----------------------------------------------------------
    #download pp,resize and set it in label
    try:
        os.remove("tkinter-profile-check-data/pp.png")
    except:
        pass
    try:
        wget.download(pp,'tkinter-profile-check-data/pp.png')
        img = Image.open('tkinter-profile-check-data/pp.png')
        img = img.resize((196, 196), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        img_panel = Label(form, image=img)
        img_panel.image = img
        img_panel.place(x=40,y=190)
    #if there is no pp set the pplabel to"nopp.png" 
    except:
        img = Image.open('tkinter-profile-check-data/nopp.png')
        img = img.resize((196, 196), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        img_panel = Label(form, image=img)
        img_panel.image = img
        img_panel.place(x=40,y=190)


def profil():
    hesap=link.get()
    webbrowser.open(f'http://twitter.com/{hesap}')

button=Button(form,text='Find Profile',command=submit)
button.place(x=410,y=530,height=50)

profilegit=Button(form,text='Go To Profile',command=profil)
profilegit.place(x=510,y=530,height=50)

dosyayukle=Button(form,text='Import Accounts',command=yukle)
dosyayukle.place(x=70,y=530,height=50)
form.attributes('-topmost',True)
form.mainloop()