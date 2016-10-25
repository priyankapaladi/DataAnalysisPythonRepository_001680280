# Most frequent tweeter about the topic

searchWord = input("Please enter a search term: ")
filepath = searchWord.replace(" ","").lower() 

with open(filepath+'.json', 'r') as fr:
    data = json.load(fr)
user_id_all = {}
user_screenname_all = []
for id in data:
    user = data[id]['user']
    if user['id_str'] is not None or user['screen_name'] is not None: 
        if user['id_str'] in user_id_all:
            user_id_all[user['id_str']] += 1
        else: 
            user_id_all[user['id_str']] = 1
        user_screenname_all.append(user['screen_name'])
print('User ids and their tweet numbers:',user_id_all)
#print(len(user_id_all))
for key, value in sorted(user_id_all.items(), key=lambda x: x[1], reverse = True)[:10]:
    print('User ID:',key,'--- Number of tweets on the topic', value, '\n')
screen_name_unique = list(set(user_screenname_all))
#print(screen_name_unique)
print(len(screen_name_unique))
#print(sorted(user_id_all, key=lambda x: user_id_all[x]))
