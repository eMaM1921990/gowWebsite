import urllib
import urlparse
from django.conf import settings
import facebook
import subprocess
import json
import requests


__author__ = 'emam'


# def longLivedAccessToken():
#     # Trying to get an access token. Very awkward.
#     oauth_args = dict(client_id     = settings.FB_APP_ID,
#                       client_secret = settings.FB_APP_SECRET,
#                       grant_type    = 'fb_exchange_token',
#                       fb_exchange_token=settings.FB_ACCESS_TOKEN)
#     oauth_curl_cmd = ['curl','https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]
#     oauth_response = subprocess.Popen(oauth_curl_cmd,
#                                       stdout = subprocess.PIPE,
#                                       stderr = subprocess.PIPE).communicate()[0]
#     try:
#         oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
#         return oauth_access_token
#     except KeyError:
#         print('Unable to grab an access token!')
#         exit()
#
#
#
# def getUserIdFrom():
#


def short_url(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key='+settings.API_KEY
    params = json.dumps({'longUrl': url})
    response = requests.post(post_url,params,headers={'Content-Type': 'application/json'})
    return response.json()['id']

def postFacebookPage(post,post_id):
    try:
        access_token=settings.FB_LONG_TERM_ACCESS_TOKEN
        graph = facebook.GraphAPI(access_token)
        x=graph.put_object(settings.FB_PAGE_ID, "feed", message=post+short_url(settings.site_name+str(post_id))+settings.hash_tag)
    except Exception as e:
        print str(e)
