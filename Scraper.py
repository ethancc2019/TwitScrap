import os
from twitterscraper import query_tweets


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return li[0]

def parseString(keywords):

    keywordList = str(keywords).split(',')
    returnStr = ""
    length = len(keywordList)

    for i in keywordList:
        returnStr += i + " OR "
    returnStr = rreplace(returnStr,"OR","",1)

    return returnStr

if __name__ == "__main__":
    print("Enter the twitter username")
    username = input()
    print("Enter keywords or phrases separated by a comma")
    keywords = input()
    #keywords = "football,chargers"
    serchTerms = parseString(keywords)

    if (os.path.exists("tweet.json")):
        os.remove("tweet.json")

    command = "twitterscraper \"" + serchTerms + " from:" + username + "\" -o tweet.json -l 100"
    output = "tweet.json"
    os.system(command)