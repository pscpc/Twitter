import tweepy
from datetime import datetime
import time
# assign the values accordingly

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


now = datetime.now()
current_time = now.strftime("%d/%m/%Y - %H:%M:%S")
file=open("log.txt","a")
file.write(f"\t\t{current_time}")

total_takipci=0
personel_total=0

def run(personel_adi,personel):
	x=open("log.txt","a",encoding="utf-8")
	x.write(f"\t\t\t{personel_adi}\n")
	x.close()
	for i in personel:
		hesapla(i)
	global personel_total
	x=open("log.txt","a",encoding="utf-8")
	x.write(str(f"\tTotal Followers:\t{personel_total}\n"))
	personel_total=0

def hesapla(kullanici):
	global total_takipci
	global personel_total
	a=api.get_user(screen_name=kullanici)
	hesapadi = a.screen_name
	takipedilen = a.friends_count
	takipci  = a.followers_count
	tweetsayisi = a.statuses_count
	total_takipci=total_takipci+takipci
	personel_total=personel_total+takipci
	result=(f"{hesapadi:30s}\t= \t{takipedilen} following \t{takipci} followers \t{tweetsayisi} tweet")
	x=open("log.txt","a",encoding="utf-8")
	x.write(f"{result}\n")
	x.close()
	print(result)

first_list=["neiltyson","BillGates","JeffBezos","jack","MrBeast"]
second_list=["dogecoin","SpaceX","Tesla","BillNye"]


run("First List",first_list)
run("Second List",second_list)








time.sleep(21600)