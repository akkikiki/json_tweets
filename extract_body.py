import json
from cleansing_tweet import clean_escapes

DOC_NAME = "iran_2013_earthquake.jsonl"
f_json = open(DOC_NAME)
f_out = open(DOC_NAME + "_tweets.txt", "w")

for i, line in enumerate(f_json):
    tweet = json.loads(line)['body']
    f_out.write(clean_escapes(tweet) + "\n")

    #if i == 10:
    #    break
