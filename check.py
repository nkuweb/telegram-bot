import re
import urllib
from urllib.parse import urlparse
def url(url):
    x = urlparse(url)
    if (x.scheme == "http" or  x.scheme == "https") and (x.hostname is not None):
        return True
    else:
        return False

def chechurl(url):
    if(urllib.urlopen(url).getcode()==200):
        return True
    else:
        return False

