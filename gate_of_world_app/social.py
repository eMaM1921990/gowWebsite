import urllib
import urlparse
from django.conf import settings
import facebook
import subprocess

__author__ = 'emam'


def getAccessToken():
    # Trying to get an access token. Very awkward.
    oauth_args = dict(client_id     = settings.FB_APP_ID,
                      client_secret = settings.FB_APP_SECRET,
                      grant_type    = 'client_credentials')
    oauth_curl_cmd = ['curl','https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]
    oauth_response = subprocess.Popen(oauth_curl_cmd,
                                      stdout = subprocess.PIPE,
                                      stderr = subprocess.PIPE).communicate()[0]
    try:
        oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
        return oauth_access_token
    except KeyError:
        print('Unable to grab an access token!')
        exit()


def postFacebookPage(post):
    try:
        access_token=getAccessToken()
        print access_token
        graph = facebook.GraphAPI(access_token)
        x=graph.put_object(settings.FB_PAGE_ID, "feed", message=post)
        print x
    except Exception as e:
        print str(e)
