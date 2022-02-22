import re
import json


with open('websiteData.txt') as file:
    all_contents = [lines for lines in file]

emails = [i for i in all_contents if '@' in i]
cleared = []

for i in emails:
    filtered = re.split(';|, | |\n',i)
    cleared+=filtered

#checking if the string contains @ and the length is greater than 5 because @.com takes 5 spaces
emails = [i for i in cleared if '@' in i and len(i)>5]

def classify_emails(email):
    prefix = email[:email.index('@')]
    if '.' in prefix or len(prefix)>8:
        return 'Human'
    else:
        return 'Non-Human'

keys = []
values = []

for email in emails:
    keys.append(email)
    dic_keys = ['Occurance','EmailType']
    dic_values = [emails.count(email),classify_emails(email)]
    values.append({k:v for (k,v) in zip(dic_keys, dic_values)})


data = {k:v for (k,v) in zip(keys, values) }

with open('result.json', 'w') as json_file:
    json.dump(data, json_file)