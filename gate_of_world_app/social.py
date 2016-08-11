from django.conf import settings
import facebook
import json
import requests
import tweepy


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

def postFacebookPage(post,post_id,img_url):
    try:
        access_token=settings.FB_LONG_TERM_ACCESS_TOKEN
        graph = facebook.GraphAPI(access_token)
        #upload image first
        img=img_url if img_url else settings.DEFAULT_IMG
        shortUrl=short_url(settings.SITE_NAME+str(post_id))
        graph.put_object(settings.FB_PAGE_ID,"photos",message=post+"\n"+shortUrl+"\n"+settings.HASH_TAG,url=img)

        # attachment =  {}
        # # attachment['name']='Link name'
        # attachment['link']='www.gateofworld.net'
        # # attachment['caption']='Check out this example'
        # # attachment['description']='This is a longer description of the attachment'
        # attachment['picture']='http://cache.albayan.com/polopoly_fs/1.2690215.1470235195!/image/628069473.jpg_gen/derivatives/rectangular_320/628069473.jpg'
        # # graph.put_wall_post(settings.FB_PAGE_ID,message='Check this out...', attachment=attachment)
        # # x=graph.put_object(settings.FB_PAGE_I D, "feed", message=post+"\n"+settings.HASH_TAG,picture='http://cache.albayan.com/polopoly_fs/1.2690215.1470235195!/image/628069473.jpg_gen/derivatives/rectangular_320/628069473.jpg')
        # graph.put_wall_post(profile_id=settings.FB_PAGE_ID,message=post+"\n"+settings.HASH_TAG, object_attachment=return_json)

    except Exception as e:
        print str(e)


def postTweeter(post,post_id,img_url):
      try:
          auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
          auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
          api=tweepy.API(auth)
          img=img_url if img_url else settings.DEFAULT_IMG
          shortUrl=short_url(settings.SITE_NAME+str(post_id))
          filename = settings.MEDIA_ROOT+settings.ADV_URL+'temp.jpg'
          request = requests.get(img, stream=True)
          if request.status_code == 200:
                with open(filename, 'wb') as image:
                    for chunk in request:
                        image.write(chunk)
          api.update_with_media(filename,post+"\n"+shortUrl+"\n"+settings.HASH_TAG)
          # api.update_status('tweepy + oauth!')


      except Exception as e:
          print 'cannot post to twitter cause '+str(e)


