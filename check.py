import re
def url(url):
    urls = str(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url))
    if urls:
        return urls
    else:
        return False



