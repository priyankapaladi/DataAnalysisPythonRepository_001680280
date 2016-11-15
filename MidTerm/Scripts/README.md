getQuestions.py 
1. Can fetch questions by using request API.
2. Fetches 2500 files.

getUsersForQuestions.py
1. Get user ID for the questions that have been collected by iterating through all files
2. Store the user ID in txt file for further use.

getUserProfiles.py
1. Read all the user IDs from the text file and check if the user profiles have been collected already.
2. If the user profiles are not present, use request API to fetch data for those IDs

getBadgesFromUsers.py
1. Gets the badges associated with the users that have been stored.

getAnswers.py
1.Get all the answers to questions that have been collected.

getTags.py
1. Get all the tags using request API.
2. Fetches 1500 files



## Feedback
* A lot of code is repetative. Create a function for that. 
* Analysis are good but you can come up with more.
* Make your analysis bit more generic. Use argparse to get input from users.
* While saving the data, try to save it more granularly.



