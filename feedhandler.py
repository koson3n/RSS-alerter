import feedparser
import time as t

def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

def getTitles(keywords, sUrl):
    
    alert = False
    
    #url = "https://bbs.io-tech.fi/forums/prosessorit-emolevyt-ja-muistit.73/index.rss"
    url = sUrl
        
    feed = feedparser.parse(url)

    currList = []

    if len(keywords) > 0:
    
        for entry in feed.entries:
            
            for word in keywords:
                
                if entry.title.find(word) >= 0:
                
                    if search(currList, entry.title) == False:
                    
                        currList.append(entry.title)
    else:
    
        for entry in feed.entries:
            
            if search(currList, entry.title) == False:
                    
                currList.append(entry.title)
                    
    return currList
    
    
#while True:
#
#   listList = []
#
#    listList = getTitles([], 'https://www.is.fi/rss/tuoreimmat.xml')
#    
#    for i in range(5):
#        print(listList[i] + '\n')
#        
#    print('\n\n')
#              
#    t.sleep(5)
