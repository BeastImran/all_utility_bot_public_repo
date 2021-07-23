import pyshorteners
import os 

#An API-KEY would be required for bit.ly
#This key can be obtained from the bitly website https://app.bitly.com
shortener = pyshorteners.Shortener(api_key=os.environ['bitly_key'])

def shorten_link(url):
    """This function takes in the users url and returns with
    the shortened version of the link. The link is shortened 
    using the bitly shortening service.
    """
    shortened_link = shortener.bitly.short(url)
    return shortened_link

