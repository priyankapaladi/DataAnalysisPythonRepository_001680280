# Top 10 zones who have tweeted about the topic - Time zones
#TimeZones
searchWord = input("Please enter a search term: ")
filepath = searchWord.replace(" ","").lower() 

with open(filepath+'.json', 'r') as fr:
    data = json.load(fr)
time_zone_all = {}
user_count = 0
for id in data:
    user = data[id]['user']
    #user_count += 1
    if user['time_zone'] is not None: 
        if user['time_zone'] in time_zone_all:
            time_zone_all[user['time_zone']] += 1
        else:
            time_zone_all[user['time_zone']] = 1

print(time_zone_all)

#print(sorted(time_zone_all, key=lambda x: time_zone_all[x], reverse = True))

top10 = sorted(time_zone_all, key=lambda x: time_zone_all[x], reverse = True)
print(top10)
#print(user_count)