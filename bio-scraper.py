import tweepy


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

count=0
for i in tweepy.Cursor(api.get_followers, screen_name="input username").items(300): #getting followers of user
        followers=i.screen_name
        b=api.get_user(screen_name=followers) #getting infos of followers
        c=b.description #define description as c
        count+=1
        print(f"{count}-{c}")
        with open(f'bio-scraper-data/bios.txt', 'a', encoding="utf-8") as f:
            f.write(f"{c}\n")
print("------------------- Done -------------------")