import json, os

path_to_json = 'F:/Python_DataAnalysis_Assignments/DataAnalysisPythonRepository_001680280/MidTerm/Questions/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


tags = []
taglist = []
answers_count = {}
question_count = {}
tagcount = {}
answercount_fortag = {}
page = 0
for js in json_files:
    with open(os.path.join(path_to_json, js)) as json_file:
        data = json.load(json_file)
    users = data['items']
    for item in users:
        try:
            answers_count[item['question_id']] = item['answer_count']
            tags = item['tags']
            question_count[item['question_id']] = tags
            
            for tag in tags:
                if tag in tagcount:
                    tagcount[tag] += 1
                    
                else:
                    tagcount[tag] = 1
                    
                
                if tag in answercount_fortag:
                    answercount_fortag[tag] += item['answer_count']
                else:
                    answercount_fortag[tag] = item['answer_count']
                if tag not in taglist:
                    taglist.append(tag)
        except KeyError:
            continue
print('done')
print('Tag count')
print(tagcount)
print('answercount_fortag')

