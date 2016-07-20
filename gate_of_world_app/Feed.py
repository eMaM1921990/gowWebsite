from datetime import datetime

__author__ = 'emam'
from models import RssProviders,RssFeeds
import feedparser
import dateutil.parser

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
            if len(feed_entity['summary']) > 0:
                record.rss_description=feed_entity['summary']
            else:
                record.rss_description=None
            record.rss_link=feed_entity['link']
            record.rss_title=feed_entity['title']
            print dateutil.parser.parse(feed_entity['published'])
            record.rss_publish_date=dateutil.parser.parse(feed_entity['published'])

            if 'media_content' in feed_entity:
                for thumbnail in feed_entity['media_content']:
                    record.rss_thumbnail=thumbnail['url']
            if 'media_player' in feed_entity:
                for video in feed_entity['media_player']:
                    record
            record.save()
            print record.id






    def feedParser(self):
        listFeedProvider=self.getFeedProviders()
        for feedProvider in listFeedProvider:
            feeds=feedparser.parse(feedProvider.rss_url)
            self.addFeedToDatabase(feeds,feedProvider.rss_category)

