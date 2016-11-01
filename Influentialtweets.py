# get the id's of users who have retweeted the status id
#retweeteduser = {}
searchWord = input("Please enter a search term: ")
filepath = searchWord.replace(" ","").lower() 

with open(filepath+'.json', 'r') as fr:
    data = json.load(fr)

influential_tweets = {}
for key in data:
    #print('key: ',key)
    #print('retweet', data[key]['retweet_count'])
    if data[key]['retweet_count'] > 0:
        retweet_count = data[key]['retweet_count']
        #print('retweet_count > 0: ' , retweet_count)
        
        followers_count = data[key]['user']['followers_count']
        #print('followers_count: ' , followers_count )
        product = retweet_count * followers_count
        influential_tweets[key] = product
        #print('Product:', product)
print("Below are the tweets which are influential with their value of influence = retweet_count * followers_count")
for key, value in sorted(influential_tweets.items(), key=lambda x: x[1], reverse = True)[:10]:
    print('Status ID: ',key,'\n',data[key]['text'],'\n','Value of Influence:', value, '\n','\n')

    #if data[key]['retweet_count'] > 0:
     #   getReTweetedId = 'https://api.twitter.com/1.1/statuses/retweeters/ids.json?id='+key+'&count=100&stringify_ids=true'
          #response = requests.get(getReTweetedId, auth=auth)
        #response = response.json()
        #print(response)
    #sleep(1)
    
# to calculate the engagement of a tweet
fav_count = {}
length_tweet = {}
# for every key- status id in influential tweet find favorite count
for key, value in sorted(influential_tweets.items(), key=lambda x: x[1], reverse = True)[:10]:
    print('Status ID: ',key,'\n','length of the tweet:', len(data[key]['text']),'\n','Favourite count: ',data[key]['user']['favourites_count'],'\n','Value of Influence:', value, '\n','\n')

    fav_count[key] = data[key]['user']['favourites_count']
    length_tweet[key] = len(data[key]['text'])
print(fav_count,'\n')
print('length of tweet', length_tweet)

# engagement can be length of the tweet for the influential value


#print(retweeteduser['id'])# get the id's of users who have retweeted the status id
#retweeteduser = {}
searchWord = input("Please enter a search term: ")
filepath = searchWord.replace(" ","").lower() 

with open(filepath+'.json', 'r') as fr:
    data = json.load(fr)

influential_tweets = {}
for key in data:
    #print('key: ',key)
    #print('retweet', data[key]['retweet_count'])
    if data[key]['retweet_count'] > 0:
        retweet_count = data[key]['retweet_count']
        #print('retweet_count > 0: ' , retweet_count)
        
        followers_count = data[key]['user']['followers_count']
        #print('followers_count: ' , followers_count )
        product = retweet_count * followers_count
        influential_tweets[key] = product
        #print('Product:', product)
print("Below are the tweets which are influential with their value of influence = retweet_count * followers_count")
for key, value in sorted(influential_tweets.items(), key=lambda x: x[1], reverse = True)[:10]:
    print('Status ID: ',key,'\n',data[key]['text'],'\n','Value of Influence:', value, '\n','\n')

    #if data[key]['retweet_count'] > 0:
     #   getReTweetedId = 'https://api.twitter.com/1.1/statuses/retweeters/ids.json?id='+key+'&count=100&stringify_ids=true'
          #response = requests.get(getReTweetedId, auth=auth)
        #response = response.json()
        #print(response)
    #sleep(1)
    
# to calculate the engagement of a tweet
fav_count = {}
length_tweet = {}
# for every key- status id in influential tweet find favorite count
for key, value in sorted(influential_tweets.items(), key=lambda x: x[1], reverse = True)[:10]:
    print('Status ID: ',key,'\n','length of the tweet:', len(data[key]['text']),'\n','Favourite count: ',data[key]['user']['favourites_count'],'\n','Value of Influence:', value, '\n','\n')

    fav_count[key] = data[key]['user']['favourites_count']
    length_tweet[key] = len(data[key]['text'])
print(fav_count,'\n')
print('length of tweet', length_tweet)

# engagement can be length of the tweet for the influential value


#print(retweeteduser['id'])