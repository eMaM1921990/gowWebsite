from datetime import datetime

__author__ = 'emam'
from models import RssProviders,RssFeeds
import feedparser
import dateutil.parser
import logging
logger = logging.getLogger(__name__)

class Feed():




    #GET FEED PROVIDERS FROM DATABASE
    def getFeedProviders(self):
        try:
            providerList= RssProviders.objects.filter(rss_is_active=True)
            return providerList
        except Exception as e:
            logger.debug("Error getting providers list -- cause :"+str(e),exc_info=1)
            return None

    #save feed in database
    def addFeedToDatabase(self,feeds,feedCategoryObj):
        try:
            for feed_entity in feeds['entries']:
                record=RssFeeds()
                record.rss_category=feedCategoryObj

                ##check if summary in feed entity
                if 'summary' in feed_entity:
                    if len(feed_entity['summary']) > 0:
                        record.rss_description=feed_entity['summary']
                    else:
                        record.rss_description=None
                else:
                    record.rss_description=None

                ## check if link in feed entity
                if 'link' in feed_entity:
                    record.rss_link=feed_entity['link']
                else:
                    record.rss_link=None

                #check if title in feed entity
                if 'title' in feed_entity:
                    record.rss_title=feed_entity['title']
                else:
                    record.rss_title=None

                #check if published date in feed entity
                if 'published' in feed_entity:
                    record.rss_publish_date=dateutil.parser.parse(feed_entity['published'])
                else:
                    record.rss_publish_date=None

                #check if media_content in feed
                if 'media_content' in feed_entity:
                    for thumbnail in feed_entity['media_content']:
                        record.rss_thumbnail=thumbnail['url']

                #check if media_player in feed_entity
                if 'media_player' in feed_entity:
                    record.rss_video=feed_entity['media_player']['url']

                record.save()
        except Exception as e:
            logger.debug("Error save feed -- cause :"+str(e),exc_info=1)





    # fetch feeds
    def feedParser(self):
        try:
            listFeedProvider=self.getFeedProviders()
            for feedProvider in listFeedProvider:
                if feedProvider.rss_last_call is None:
                    feeds=feedparser.parse(feedProvider.rss_url)
                else:
                    feeds=feedparser.parse(feedProvider.rss_url,modified=feedProvider.rss_last_call)

                #Noticing no update
                if(feeds.status!=304):
                    self.updateProviderUpdatedTime(feedProvider,feeds.modified)
                    self.addFeedToDatabase(feeds,feedProvider.rss_category)
                #Noticing temporary redirects
                elif feeds.status==302:
                    feeds=feedparser.parse(feeds.href)
                    self.updateProviderUpdatedTime(feedProvider,feeds.modified)
                    self.addFeedToDatabase(feeds,feedProvider.rss_category)
                #Noticing permanent redirects
                elif feeds.status==301:
                    feeds=feedparser.parse(feeds.href)
                    self.updateProviderUpdatedTime(feedProvider,feeds.modified)
                    self.addFeedToDatabase(feeds,feedProvider.rss_category)
                    self.markRssFeedIsPermenantRedirect(feedProvider.id,feeds.href)

                elif feeds.status==410:
                    self.markRssFeedsGone(feedProvider.id)
                else:
                    logger.debug('Logged status'+str(feeds.status))


        except Exception as e:
            logger.debug("Error save feed for category ["+feedProvider.rss_category.id+"] -- cause :"+str(e),exc_info=1)




    # update last call time
    def updateProviderUpdatedTime(self,feedProvider,lastModified):
        try:
            feedProvider.rss_last_call=dateutil.parser.parse(lastModified)
            feedProvider.save()
        except Exception as e:
            logger.debug("Error update feed ID is  ["+feedProvider.id+"] -- cause :"+str(e),exc_info=1)

    # call when permenant rediect
    def markRssFeedIsPermenantRedirect(self,id,url):
        try:
            record=RssProviders.objects.get(id=id)
            record.rss_url=url
            record.save()
        except Exception as e:
            logger.debug("Error update feed url is  ["+id+"] -- cause :"+str(e),exc_info=1)


    # call when marked as gone
    def markRssFeedsGone(self,id):
        try:
            record=RssProviders.objects.get(id=id)
            record.delete()
        except Exception as e:
            logger.debug("Error delete feed with id :  ["+id+"] -- cause :"+str(e),exc_info=1)
