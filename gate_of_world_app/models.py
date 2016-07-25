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
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.text import slugify
from gowWebsite import settings
from PIL import Image as Img
import StringIO



MANAGED=True

class RssCategories(models.Model):
    rss_category = models.CharField(unique=True, max_length=225,verbose_name='Rss Category')
    rss_slug = models.CharField(unique=True, max_length=45)
    rss_is_active = models.BooleanField(blank=True,default=True)  # This field type is a guess.
    rss_is_suggested=models.BooleanField(blank=True,default=True,verbose_name='Suggested')
    rss_is_world_news=models.BooleanField(blank=True,default=False,verbose_name='World News')
    rss_is_political_news=models.BooleanField(blank=True,default=False,verbose_name='Political News')
    rss_is_local_news=models.BooleanField(blank=True,default=False,verbose_name='Local News')
    rss_is_world_common_news=models.BooleanField(blank=True,default=False,verbose_name='Common News')
    rss_order=models.IntegerField(default=0,verbose_name='Order')
    rss_show_in_footer=models.BooleanField(blank=True,default=False,verbose_name='Show in Footer')

    def save(self):
        super(RssCategories, self).save()
        self.rss_slug = '%s' % (
            slugify(self.id)
        )
        super(RssCategories, self).save()

    def __unicode__(self):
        return self.rss_category

    class Meta:
        managed = MANAGED
        db_table = 'rss_categories'
        ordering=('rss_order',)
        verbose_name_plural='RSS Categories'


class RssFeeds(models.Model):
    rss_link = models.CharField(max_length=255, blank=True,unique=True)
    rss_title = models.CharField(max_length=255, blank=True)
    rss_description = models.CharField(max_length=255, blank=True,null=True)
    rss_thumbnail = models.CharField(max_length=255, blank=True,null=True)
    rss_publish_date = models.DateTimeField(blank=True, null=True)
    rss_category = models.ForeignKey(RssCategories, db_column='rss_category', blank=True, null=True)
    rss_id= models.CharField(max_length=255, blank=True)
    rss_views_no=models.IntegerField(default=0)
    rss_video=models.CharField(max_length=255, blank=True,default=None,null=True)
    rss_image=models.CharField(max_length=255, blank=True,null=True)

    def thumbnail(self):
        return '<img src="%s" style="width:50px;height:50px"/>' % self.rss_thumbnail
    thumbnail.allow_tags = True

    def feed_title(self):
        return '<a href="%s" >%s </a>' %(self.rss_link,self.rss_title)
    feed_title.allow_tags = True

    def __unicode__(self):
        return self.rss_title

    class Meta:
        managed = MANAGED
        db_table = 'rss_feeds'
        ordering=('-rss_publish_date',)
        verbose_name_plural='Posts'
        # unique_together=['rss_link','rss_title']


class RssProviders(models.Model):
    rss_url = models.CharField(unique=True, max_length=100)
    rss_is_active = models.BooleanField(blank=True,default=True)  # This field type is a guess.
    rss_category = models.ForeignKey(RssCategories, db_column='rss_category')
    rss_add_at = models.DateTimeField(blank=True, null=True)
    rss_last_call = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'rss_providers'
        verbose_name_plural='RSS Providers'


class Adv(models.Model):
    position = models.CharField(unique=True, max_length=45,choices=[('1','One'),('2','Two'),('3','Three'),('4','Four'),('5','Five')])
    url=models.ImageField(upload_to=settings.ADV_URL)

    def adv_image(self):
        return '<img src="%s" />' % self.url.url
    adv_image.allow_tags = True

    def save(self, *args, **kwargs):
        if self.url:
            img = Img.open(StringIO.StringIO(self.url.read()))
            # if img.mode != 'RGB':
            #     img = img.convert('RGB')
            # img.thumbnail((self.url.width/1,self.url.height/1), Img.ANTIALIAS)
            output = StringIO.StringIO()
            img.save(output, format='JPEG', quality=90)
            output.seek(0)
            self.url= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.url.name.split('.')[0], 'image/jpeg', output.len, None)
        super(Adv, self).save(*args, **kwargs)

    class Meta:
        managed = MANAGED
        db_table = 'adv'
        verbose_name_plural='Advertising'
