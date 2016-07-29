from django.conf import settings
import facebook

__author__ = 'emam'


def postFacebookPage(post):
    try:
        graph = facebook.GraphAPI(settings.FB__PAGE_ACCESS_TOKEN)
        graph.put_object(settings.FB_PAGE_ID, "feed", message=post)
    except Exception as e:
        print str(e)
