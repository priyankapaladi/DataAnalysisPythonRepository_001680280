#pre processing
import nltk
import re
#nltk.download('punkt')

from nltk.tokenize import word_tokenize

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
searchWord = input("Please enter a search term: ")
filepath = searchWord.replace(" ","").lower() 

with open(filepath+'.json', 'r') as fr:
    data = json.load(fr)


tweets_tokenized = []
for id in data:
    tweet = data[id]['text']
    tweets_tokenized.append(preprocess(tweet))


print(tweets_tokenized)



# To remove stop words and calculate frequency of words
#to remove stop words
import nltk
from nltk import bigrams 

from nltk.corpus import stopwords
#nltk.download()
from collections import Counter
 

import string
 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
count_all = Counter()
terms_stop = []
for line in tweets_tokenized:
    for term in line:
        if term not in stop and not term.startswith(('#', '@')):
            terms_stop.append(term)
    #terms_stop = [term for term in line if term not in stop]
    #terms_stop.append(terms_stop)
            count_all.update(terms_stop)

# for word in terms_stop:
#     count_all += 1
# print(count_all)
print(count_all.most_common(50))

#terms_bigram = []
#terms_bigram = bigrams(terms_stop) 
#print(terms_bigram)
#print(terms_stop[:100])