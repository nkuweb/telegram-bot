import re
from urllib.parse import urlparse
def url(url):
    x = urlparse(url)
    if (x.scheme == "http" or  x.scheme == "https") and (x.hostname is not None):
        return True
    else:
        return False
