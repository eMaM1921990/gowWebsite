from datetime import datetime
import hashlib

__author__ = 'emam'
from models import RssProviders,RssFeeds
import feedparser
import dateutil.parser
import logging
logger = logging.getLogger(__name__)

class Feed():

    def getFeedProviders(self):
        try:
            providerList= RssProviders.objects.filter(rss_is_active=True)
            return providerList
        except Exception as e:
            logger.debug("Error getting providers list -- cause :"+str(e),exc_info=1)
            return None


    def addFeedToDatabase(self,feeds,feedCategoryObj):
            for feed_entity in feeds['entries']:
                try:

                    record=RssFeeds()
                    record.rss_category=feedCategoryObj

                    if 'summary' in feed_entity:
                        if len(feed_entity['summary']) > 0:
                            record.rss_description=feed_entity['summary']
                        else:
                            record.rss_description=None
                    else:
                        record.rss_description=None


                    if 'link' in feed_entity:
                        record.rss_link=feed_entity['link']
                    else:
                        record.rss_link=None


                    if 'title' in feed_entity:
                        record.rss_title=feed_entity['title']
                    else:
                        record.rss_title=None


                    if 'published' in feed_entity:
                        record.rss_publish_date=dateutil.parser.parse(feed_entity['published'])
                    else:
                        record.rss_publish_date=None


                    if 'media_content' in feed_entity:
                        for thumbnail in feed_entity['media_content']:
                            record.rss_thumbnail=thumbnail['url']

                    if 'media_player' in feed_entity:
                        record.rss_video=feed_entity['media_player']['url']

                    ### hexdigit
                    hexDigit=self.get_hexdigest(record.rss_title,record.rss_link)
                    record.rss_hex_digit=hexDigit

                    record.save()

                except Exception as e:
                    print "Error save feed -- cause :"+str(e)
                    logger.debug("Error save feed -- cause :"+str(e),exc_info=1)





    def feedParser(self):

            listFeedProvider=self.getFeedProviders()
            for feedProvider in listFeedProvider:
                try:
                    if feedProvider.rss_last_call is None:
                        feeds=feedparser.parse(feedProvider.rss_url)
                    else:
                        feeds=feedparser.parse(feedProvider.rss_url,modified=feedProvider.rss_last_call)

                    print int(feeds.status)
                    # Noticing update
                    if int(feeds.status)==200:
                        if feeds.modified:
                            self.updateProviderUpdatedTime(feedProvider,feeds.modified)
                        self.addFeedToDatabase(feeds,feedProvider.rss_category)
                    # Noticing temporary redirects
                    elif int(feeds.status)==302:
                        feeds=feedparser.parse(feeds.href)
                        if feeds.modified:
                            self.updateProviderUpdatedTime(feedProvider,feeds.modified)
                        self.addFeedToDatabase(feeds,feedProvider.rss_category)
                    # Noticing permanent redirects
                    elif int(feeds.status)==301:
                        feeds=feedparser.parse(feeds.href)
                        self.updateProviderUpdatedTime(feedProvider,feeds.modified)
                        self.addFeedToDatabase(feeds,feedProvider.rss_category)
                        self.markRssFeedIsPermenantRedirect(feedProvider.id,feeds.href)
                    # notice Gone
                    elif int(feeds.status)==410:
                        self.markRssFeedsGone(feedProvider.id)
                    # notice no updates
                    elif int(feeds.status)==304:

                        self.updateProviderUpdatedTime(feedProvider,feeds.modified)

                    else:

                        self.updateProviderUpdatedTime(feedProvider,feeds.modified)

                except Exception as e:
                    print str(e)
                    logger.debug("Error save feed for category ["+str(feedProvider.rss_category.id)+"] -- cause :"+str(e),exc_info=1)





    def updateProviderUpdatedTime(self,feedProvider,lastModified):
        try:
            print lastModified
            feedProvider.rss_last_call=dateutil.parser.parse(lastModified)
            feedProvider.save()
        except Exception as e:
            logger.debug("Error update feed ID is  ["+str(feedProvider.id)+"] -- cause :"+str(e),exc_info=1)


    def markRssFeedIsPermenantRedirect(self,id,url):
        try:
            record=RssProviders.objects.get(id=id)
            record.rss_url=url
            record.save()
        except Exception as e:
            logger.debug("Error update feed url is  ["+str(id)+"] -- cause :"+str(e),exc_info=1)


    def markRssFeedsGone(self,id):
        try:
            record=RssProviders.objects.get(id=id)
            record.delete()
        except Exception as e:
            logger.debug("Error delete feed with id :  ["+str(id)+"] -- cause :"+str(e),exc_info=1)


    def get_hexdigest(self,title,url):
        print title
        print url
        m = hashlib.md5()
        m.update(title.decode()+url.decode())
        return m.hexdigest()
