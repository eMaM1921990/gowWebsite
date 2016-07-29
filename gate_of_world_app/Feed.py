# encoding=utf8
import re
import sys
import urllib2
from BeautifulSoup import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

from datetime import datetime
import hashlib
import urllib

__author__ = 'emam'
from models import RssProviders,RssFeeds
import feedparser
import dateutil.parser
import logging
from social import *
logger = logging.getLogger(__name__)

class Feed():

    def getFeedProviders(self):
        try:
            providerList= RssProviders.objects.filter(rss_is_active=True)
            return providerList
        except Exception as e:
            logger.debug("Error getting providers list -- cause :"+str(e),exc_info=1)
            return None


    def addFeedToDatabase(self,feeds,feedCategoryObj,Providers):
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
                            print thumbnail['url']
                            record.rss_thumbnail=thumbnail['url']

                    ## overwrite
                    elif 'media_thumbnail' in feed_entity:
                        print 'media thumbnail'
                        for thumbnail in feed_entity['media_thumbnail']:
                            record.rss_thumbnail=thumbnail['url']
                    else:
                        record.rss_thumbnail=None

                    if 'media_player' in feed_entity:
                        record.rss_video=feed_entity['media_player']['url']

                    ### hexdigit
                    hexDigit=self.get_hexdigest(record.rss_title,record.rss_link)
                    record.rss_hex_digit=hexDigit

                    ## Parse HTML
                    # print Providers
                    # self.ParseHTML(record.rss_link,record.rss_description,Providers.rss_parent_tag,Providers.rss_child_tag,Providers.rss_child_class_tag)

                    # s=postFacebookPage(record.rss_title)

                    record.save()



                except Exception as e:
                    print str(e)
                    logger.debug("Error save feed -- cause :"+str(e),exc_info=1)





    def feedParser(self):

            listFeedProvider=self.getFeedProviders()
            for feedProvider in listFeedProvider:
                try:
                    if feedProvider.rss_last_call is None:
                        feeds=feedparser.parse(feedProvider.rss_url)
                    else:
                        feeds=feedparser.parse(feedProvider.rss_url,modified=feedProvider.rss_last_call)

                    # Noticing update
                    if int(feeds.status)==200:
                        if hasattr(feeds,'modified'):
                            self.updateProviderUpdatedTime(feedProvider,feeds.modified)
                        self.addFeedToDatabase(feeds,feedProvider.rss_category,feedProvider)
                    # Noticing temporary redirects
                    elif int(feeds.status)==302:
                        feeds=feedparser.parse(feeds.href)
                        if hasattr(feeds,'modified'):
                            self.updateProviderUpdatedTime(feedProvider,feeds.modified)
                        self.addFeedToDatabase(feeds,feedProvider.rss_category,feedProvider)
                    # Noticing permanent redirects
                    elif int(feeds.status)==301:
                        feeds=feedparser.parse(feeds.href)
                        self.updateProviderUpdatedTime(feedProvider,feeds.modified)
                        self.addFeedToDatabase(feeds,feedProvider.rss_category,feedProvider)
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
        url=urllib.unquote(url).decode('utf8')
        title=title.decode('utf-8')
        m = hashlib.md5()
        m.update(title.decode()+url.decode())
        return m.hexdigest()



    # def ParseHTML(self,url,desc,Tag,Tag2,classTag):
    #
    #
    #     fullText=''
    #     url=urllib.unquote(url).decode('utf8')
    #     soup = BeautifulSoup(urllib2.urlopen(url).read())
    #     # retrieve all of the paragraph tags
    #     if Tag:
    #         paragraphs = soup.find(Tag).find(Tag2, {'class': classTag}).find_all('p')
    #     else:
    #         paragraphs = soup.findAll({'class': 'story-body__inner'}).find_all('p')
    #     print classTag
    #     print len(paragraphs)
    #     for paragraph in paragraphs:
    #         print paragraph.string
    #         fullText=fullText+paragraph.string
    #     print fullText
    #     return fullText


