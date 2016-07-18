# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


MANAGED=True

class RssCategories(models.Model):
    rss_category = models.CharField(unique=True, max_length=225)
    rss_slug = models.CharField(unique=True, max_length=45)
    rss_is_active = models.BooleanField(blank=True,default=True)  # This field type is a guess.
    rss_is_suggested=models.BooleanField(blank=True,default=True)

    def __unicode__(self):
        return self.rss_category

    class Meta:
        managed = MANAGED
        db_table = 'rss_categories'


class RssFeeds(models.Model):
    rss_link = models.CharField(max_length=255, blank=True)
    rss_title = models.CharField(max_length=255, blank=True)
    rss_description = models.CharField(max_length=255, blank=True)
    rss_thumbnail = models.CharField(max_length=255, blank=True)
    rss_publish_date = models.DateTimeField(blank=True, null=True)
    rss_category = models.ForeignKey(RssCategories, db_column='rss_category', blank=True, null=True)
    rss_id= models.CharField(max_length=255, blank=True)
    rss_views_no=models.IntegerField(default=0)

    def admin_image(self):
        return '<img src="%s" style="width:50px;height:50px"/>' % self.rss_thumbnail
    admin_image.allow_tags = True

    def feed_title(self):
        return '<a href="%s" >%s </a>' %(self.rss_link,self.rss_title)
    feed_title.allow_tags = True

    class Meta:
        managed = MANAGED
        db_table = 'rss_feeds'


class RssProviders(models.Model):
    rss_url = models.CharField(unique=True, max_length=45)
    rss_is_active = models.BooleanField(blank=True,default=True)  # This field type is a guess.
    rss_category = models.ForeignKey(RssCategories, db_column='rss_category')
    rss_add_at = models.DateTimeField(blank=True, null=True)
    rss_last_call = models.DateTimeField(blank=True, null=True)


    class Meta:
        managed = MANAGED
        db_table = 'rss_providers'


class Adv(models.Model):
    position = models.CharField(unique=True, max_length=45)
    url=models.ImageField(upload_to='')

    class Meta:
        managed = MANAGED
        db_table = 'adv'
