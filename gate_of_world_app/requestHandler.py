__author__ = 'emam'
from models import *
from datetime import datetime as dt, timedelta
import logging
logger = logging.getLogger(__name__)


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
        context['quick_news']=self.ListCurrentNews()
        context['video']=self.get_video()
        return context


    ## Common methods

    def FeedCategory(self):
        try:
            exeQuery=RssCategories.objects.filter(rss_is_active=True)
            return exeQuery
        except Exception as e:
            logger.debug("Error getting feeds categories list -- cause :"+str(e),exc_info=1)


    def LastThreeFeeds(self):
        try:
            exeQuery=RssFeeds.objects.filter(rss_category__rss_is_active=True)[:3]
            return exeQuery
        except Exception as e:
            logger.debug("Error getting last 3 feeds list -- cause :"+str(e),exc_info=1)

    def ListOfSuggestedFees(self):
        try:
            exeQuery=RssFeeds.objects.filter(rss_category__rss_is_suggested=True,rss_category__rss_is_active=True).exclude(rss_description__isnull=True).order_by('-rss_publish_date')[:5]
            return exeQuery
        except Exception as e:
            logger.debug("Error getting suggested feeds  list -- cause :"+str(e),exc_info=1)

    def ListOfWorldNews(self):
        try:
            exeQuery=RssFeeds.objects.filter(rss_category__rss_is_world_news=True,rss_category__rss_is_active=True).exclude(rss_description__isnull=True)[:3]
            return exeQuery
        except Exception as e:
            logger.debug("Error getting last word news  list -- cause :"+str(e),exc_info=1)

    def ListOfPolitical(self):
        try:
            exeQuery=RssFeeds.objects.filter(rss_category__rss_is_political_news=True,rss_category__rss_is_active=True).exclude(rss_description__isnull=True)[:3]
            return exeQuery
        except Exception as e:
            logger.debug("Error getting political news  list -- cause :"+str(e),exc_info=1)

    def ListOfLocalNews(self):
        try:
            exeQuery=RssFeeds.objects.filter(rss_category__rss_is_local_news=True,rss_category__rss_is_active=True).exclude(rss_description__isnull=True)[:3]
            return exeQuery
        except Exception as e:
            logger.debug("Error getting  local news  list -- cause :"+str(e),exc_info=1)

    def ListOfCommonNews(self):
        try:
            exeQuery=RssFeeds.objects.filter(rss_category__rss_is_world_common_news=True,rss_category__rss_is_active=True).order_by('-rss_views_no')[:24]
            return  exeQuery
        except Exception as e:
            logger.debug("Error getting last common news  list -- cause :"+str(e),exc_info=1)

    def ListCurrentNews(self):
        try:
            exeQuery=RssFeeds.objects.filter(rss_category__rss_is_active=True)[:12]
            return exeQuery
        except Exception as e:
            logger.debug("Error getting  current news  list -- cause :"+str(e),exc_info=1)

    def AdvBanner(self):
        try:
            exeQuery=Adv.objects.all()
            return exeQuery
        except Exception as e:
            logger.debug("Error getting advs -- cause :"+str(e),exc_info=1)

    def get_video(self):
        try:
            exeQuery=RssFeeds.objects.filter(rss_category__rss_is_active=True,rss_video__isnull=False)[:1]
            print exeQuery.query
            return exeQuery
        except Exception as e:
            logger.debug("Error getting video -- cause :"+str(e),exc_info=1)


    #Get news page
    def get_sections(self,catId):
        context={}
        context['nav']=self.FeedCategory()
        context['last_three_feeds']=self.LastThreeFeeds()
        context['adv']=self.AdvBanner()
        context['quick_news']=self.ListCurrentNews()
        context['news_feed']=self.getCategoryNew(catId)
        return context

    ## Internal common method
    def getCategoryNew(self,catId):
        try:
            exeQuery=RssFeeds.objects.filter(rss_category__rss_slug=int(catId))
            return exeQuery
        except Exception as e:
            logger.debug("Error getting section news  list -- cause :"+str(e),exc_info=1)

    #Get article
    def get_article_page(self,article_id):
        context={}
        context['nav']=self.FeedCategory()
        context['last_three_feeds']=self.LastThreeFeeds()
        context['adv']=self.AdvBanner()
        context['quick_news']=self.ListCurrentNews()
        context['article_feeds']=self.get_article_details(article_id)
        return context


    def get_article_details(self,article_id):
        try:
            ##udate seen
            self.update_article_as_seen(article_id)
            exeQuery=RssFeeds.objects.get(id=int(article_id))
            return exeQuery
        except Exception as e:
            logger.debug("Error getting article details -- cause :"+str(e),exc_info=1)

    def update_article_as_seen(self,article_id):
        try:
            record=RssFeeds.objects.get(id=int(article_id))
            record.rss_views_no=record.rss_views_no+1
            record.save()
        except Exception as e:
            logger.debug("Error during update feeds seen -- cause :"+str(e),exc_info=1)




    #Get latest news
    def get_latest_news(self):
        context={}
        context['nav']=self.FeedCategory()
        context['last_three_feeds']=self.LastThreeFeeds()
        context['adv']=self.AdvBanner()
        context['quick_news']=self.ListCurrentNews()
        context['news_feed']=self.get_today_news()
        return context



    def get_today_news(self):
        try:

            enddate=datetime.date.today()
            feeds=RssFeeds.objects.filter(rss_publish_date__gte=enddate)
            print feeds.query
            if feeds:
                return feeds
            else:
                return []
        except Exception as e:
            print str(e)
            logger.debug("Error getting latest news  list -- cause :"+str(e),exc_info=1)
            return []


