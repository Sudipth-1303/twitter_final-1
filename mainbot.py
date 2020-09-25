import tweepy
import os # operating system library

def create_api():
  consumer_key = os.getenv('consumer_key')
  consumer_secret = os.getenv('consumer_secret')
  access_token = os.getenv('access_token')
  access_token_secret = os.getenv('access_token_secret')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
  
# Complete code
import time

def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]# Used to seperate 

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers

api = create_api()

while True:
  import tweepy
import os # operating system library

def create_api():
  consumer_key = 'X0Ih7jz88OPADl4NGM6nGsOq6'
  consumer_secret = 'EuSskI1thRYbvTDat1IGK02tMu3ZA9jER64r9ez2wROmpexF9E'
  access_token = '1153660531607101440-Z1lxYp3wXsFhQb8FM9OAyuaoXrsLBv'
  access_token_secret = '0Sq1G9EFX3lr5N6LmyeMVyOIvcxxQs6D3GaH9iNciN5a4'

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
  
# Complete code
import time

def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]# Used to seperate 

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers

api = create_api()

while True:
    user = api.get_user('Sudipth1303')# change your username
    api.update_profile(name=f'SUDIPTH|{follower_count(user)} Followers')
    print(f'Updating Twitter Name : SUDIPTH|{follower_count(user)} Followers')
    print('Waiting to refresh')
    time.sleep(60)
                                                                                             
                
