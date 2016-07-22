__author__ = 'emam'
from models import *
class RequestHandler():


    #Get Main page Data
    def get_main_content(self):
        context={}
        context['nav']=self.FeedCategory()
        context['last_three_feeds']=self.LastThreeFeeds()
        context['slider']=self.ListOfSuggestedFees()
        context['adv']=self.AdvBanner()
        context['world_new']=self.ListOfWorldNews()
        context['political_news']=self.ListOfPolitical()
        context['local_news']=self.ListOfLocalNews()
        context['common_news']=self.ListOfCommonNews()
        return context


    ## Common methods

    def FeedCategory(self):
        exeQuery=RssCategories.objects.filter(rss_is_active=True)
        return exeQuery

    def LastThreeFeeds(self):
        exeQuery=RssFeeds.objects.filter(rss_category__rss_is_active=True)[:3]
        return exeQuery

    def ListOfSuggestedFees(self):
        exeQuery=RssFeeds.objects.filter(rss_category__rss_is_suggested=True,rss_category__rss_is_active=True).exclude(rss_description__isnull=True).order_by('-rss_views_no')[:3]
        return exeQuery

    def ListOfWorldNews(self):
        exeQuery=RssFeeds.objects.filter(rss_category__rss_is_world_news=True,rss_category__rss_is_active=True).exclude(rss_description__isnull=True)[:3]
        return exeQuery

    def ListOfPolitical(self):
        exeQuery=RssFeeds.objects.filter(rss_category__rss_is_political_news=True,rss_category__rss_is_active=True).exclude(rss_description__isnull=True)[:3]
        return exeQuery

    def ListOfLocalNews(self):
        exeQuery=RssFeeds.objects.filter(rss_category__rss_is_local_news=True,rss_category__rss_is_active=True).exclude(rss_description__isnull=True)[:3]
        return exeQuery

    def ListOfCommonNews(self):
        exeQuery=RssFeeds.objects.filter(rss_category__rss_is_world_common_news=True,rss_category__rss_is_active=True).order_by('-rss_views_no')[:24]
        return  exeQuery

    def AdvBanner(self):
        exeQuery=Adv.objects.all()
        return exeQuery


    #Get news page
    def get_news_pages(self,catId):
        context={}
        context['nav']=self.FeedCategory()
        context['common_news']=self.ListOfCommonNews()
        context['adv']=self.AdvBanner()
        context['news_feed']=self.getCategoryNew(catId)
        print catId
        return context

    ## Internal common method
    def getCategoryNew(self,catId):
        exeQuery=RssFeeds.objects.filter(rss_category__rss_slug=int(catId))
        return exeQuery
