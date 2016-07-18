__author__ = 'emam'
from models import *
class RequestHandler():


    #Get Main page Data
    def get_main_content(self):
        context={}
        context['nav']=self.FeedCategory()
        context['last_three_feeds']=self.LastThreeFeeds()
        context['slider']=self.ListOfSuggestedFees()
        return context

    def FeedCategory(self):
        exeQuery=RssCategories.objects.filter(rss_is_active=True)
        return exeQuery

    def LastThreeFeeds(self):
        exeQuery=RssFeeds.objects.all().order_by('-rss_publish_date')[:3]
        return exeQuery

    def ListOfSuggestedFees(self):
        exeQuery=RssFeeds.objects.filter(rss_category__rss_is_suggested=True).order_by('-rss_publish_date')[:3]
        return exeQuery


