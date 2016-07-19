from django.contrib import admin
from models import *
# Register your models here.

#category
class RSSCategory(admin.ModelAdmin):
    list_display = ('id', 'rss_category', 'rss_slug','rss_is_active' )
    list_editable = ( 'rss_category', 'rss_slug','rss_is_active')
    list_per_page = 10
    list_filter = ( 'rss_category',)
    search_fields = ('id', 'rss_category', 'rss_slug')


    class Meta:
        verbose_name='RSS Categories'
        verbose_name_plural='RSS Categories'

#RSS Provider
class RSSProviders(admin.ModelAdmin):
    list_display = ['id', 'rss_url', 'rss_is_active','rss_category','rss_last_call']
    list_per_page = 10
    list_filter = ['rss_category',]
    search_fields = ['id', 'rss_url', 'rss_is_active','rss_category','rss_last_call']




#RSS FEED
class Feed(admin.ModelAdmin):
    list_display = ('admin_image','feed_title','rss_publish_date')
    list_per_page = 10
    list_filter = ( 'rss_category',)
    search_fields = ('id', 'rss_link', 'rss_title','rss_publish_date')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



class Advertise(admin.ModelAdmin):
    list_display=['adv_image','position']
    list_per_page = 10
    list_filter = ['position']
    search_fields = ['position']


admin.site.register(RssCategories,RSSCategory)
admin.site.register(RssProviders,RSSProviders)
admin.site.register(RssFeeds,Feed)
admin.site.register(Adv,Advertise)

