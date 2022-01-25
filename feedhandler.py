import feedparser

#Checking if item already exists in a list
def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False
       
#Main logical function that return filtered or non filtered list of feed items
def getTitles(keywords, sUrl, sensitive):
    
    alert = False
    
    url = sUrl
        
    feed = feedparser.parse(url)

    currList = []

    if len(keywords) > 0 and sensitive == True:
    
        for entry in feed.entries:
            
            for word in keywords:
                
                if entry.title.find(word) >= 0:
                
                    if search(currList, entry.title) == False:
                    
                        currList.append(entry.title)
    
    elif len(keywords) > 0 and sensitive == False:
    
        for entry in feed.entries:
            
            for word in keywords:
                                
                if entry.title.lower().find(word.lower()) >= 0:
                
                    if search(currList, entry.title) == False:
                    
                        currList.append(entry.title)
    else:
    
        for entry in feed.entries:
            
            if search(currList, entry.title) == False:
                    
                currList.append(entry.title)
                    
    return currList
    
#returns all kinds of info about feed item. commonly available in most rss feeds
def getAllInfo(item, url):
        
    feed = feedparser.parse(url)
    
    string = item[0]
    
    for entry in feed.entries:
    
        if entry.title == string:
            
            infoList = [entry.link, entry.title, entry.published, entry.summary]
  
            return infoList
        
    return []
        
  
