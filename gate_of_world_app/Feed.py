from datetime import datetime

__author__ = 'emam'
from models import RssProviders,RssFeeds
import feedparser

class Feed():

    #GET FEED PROVIDERS FROM DATABASE
    def getFeedProviders(self):
        try:
            return RssProviders.objects.filter(rss_is_active=True)
        except Exception as e:
            return None


    def addFeedToDatabase(self,feeds,feedCategoryObj):
        for feed_entity in feeds['entries']:
            print feed_entity
            record=RssFeeds()
            record.rss_category=feedCategoryObj
            record.rss_description=feed_entity['summary']
            record.rss_link=feed_entity['link']
            record.rss_title=feed_entity['title']
            # record.rss_publish_date=datetime.strptime(feed_entity['published'], "%a,%d %b %Y %H:%M:%S %Z") #Tue, 28 Jun 2016 13:47:25 +0400
            if 'media_content' in feed_entity:
                for thumbnail in feed_entity['media_content']:
                    record.rss_thumbnail=thumbnail['url']
            record.save()
            print record.id






    def feedParser(self):
        listFeedProvider=self.getFeedProviders()
        for feedProvider in listFeedProvider:
            feeds=feedparser.parse(feedProvider.rss_url)
            self.addFeedToDatabase(feeds,feedProvider.rss_category)

