import requests
from urllib.parse import urlparse
def url(url):
    x = urlparse(url)
    if (x.scheme == "http" or  x.scheme == "https") and (x.hostname is not None):
        r = requests.head(url)
        return r.status_code == 200
    else:
        return False


