from django.contrib import admin
from django.forms import Textarea
from models import *
# Register your models here.

#category
class RSSCategory(admin.ModelAdmin):
    fields = ('rss_category','rss_is_active',)
    list_display = ('id', 'rss_category', 'rss_slug','rss_is_active' )
    list_per_page = 10
    list_filter = ( 'rss_category',)
    search_fields = ('id', 'rss_category', 'rss_slug')


    class Meta:
        verbose_name='RSS Categories'
        verbose_name_plural='RSS Categories'

#RSS Provider
class RSSProviders(admin.ModelAdmin):
    fields = ['rss_url', 'rss_is_active','rss_category','rss_add_at']
    list_display = ('id', 'rss_url', 'rss_is_active','rss_category','rss_last_call')
    list_per_page = 10
    list_filter = ( 'rss_category',)
    search_fields = ('id', 'rss_url', 'rss_is_active','rss_category','rss_last_call')
    readonly_fields=['rss_add_at']




#RSS FEED
class Feed(admin.ModelAdmin):
    fields = ('thumbnail','feed_title','rss_link','rss_description','rss_category')
    list_display = ('thumbnail','feed_title','rss_publish_date','rss_category')
    list_per_page = 10
    list_filter = ( 'rss_category',)
    search_fields = ('id', 'rss_link', 'rss_title','rss_publish_date')
    readonly_fields = ('thumbnail','feed_title','rss_link','rss_description','rss_category',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 10,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }



    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



admin.site.register(RssCategories,RSSCategory)
admin.site.register(RssProviders,RSSProviders)
admin.site.register(RssFeeds,Feed)
