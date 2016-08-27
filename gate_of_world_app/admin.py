from django.contrib import admin
from django.forms import Textarea
from models import *
# Register your models here.

# category
class RSSCategory(admin.ModelAdmin):
    fields = ['rss_category', 'rss_is_active', 'rss_is_suggested', 'rss_is_world_news', 'rss_is_political_news',
              'rss_is_local_news', 'rss_is_world_common_news', 'rss_show_in_footer', 'rss_order']
    list_display = ['id', 'rss_category', 'rss_is_active', 'rss_is_suggested', 'rss_is_world_news',
                    'rss_is_political_news', 'rss_is_local_news', 'rss_is_world_common_news', 'rss_show_in_footer',
                    'rss_order']
    list_per_page = 10
    list_filter = ['rss_category', 'rss_is_suggested', 'rss_is_world_news', 'rss_is_political_news',
                   'rss_is_local_news', 'rss_is_world_common_news', 'rss_show_in_footer', 'rss_order']
    list_editable = ['rss_category', 'rss_is_suggested', 'rss_is_active', 'rss_is_world_news', 'rss_is_political_news',
                     'rss_is_local_news', 'rss_is_world_common_news', 'rss_show_in_footer', 'rss_order']
    search_fields = ('id', 'rss_category',)


    class Meta:
        verbose_name = 'RSS Categories'
        verbose_name_plural = 'RSS Categories'


# RSS Provider
class RSSProviders(admin.ModelAdmin):
    fields = ['rss_url', 'rss_is_active', 'rss_category', 'rss_add_at', 'rss_parent_tag', 'rss_child_tag',
              'rss_child_class_tag']
    list_display = ['id', 'rss_url', 'rss_is_active', 'rss_category', 'rss_parent_tag', 'rss_child_tag',
                    'rss_child_class_tag', 'rss_last_call']
    list_per_page = 10
    list_filter = ( 'rss_category',)
    search_fields = ('id', 'rss_url', 'rss_is_active', 'rss_category', 'rss_last_call')
    readonly_fields = ['rss_add_at']


# RSS FEED
class Feed(admin.ModelAdmin):
    fields = ('thumbnail', 'feed_title', 'rss_link', 'rss_description', 'rss_category', 'rss_views_no', 'rss_video',
              'rss_full_article',)
    list_display = ('thumbnail', 'feed_title', 'rss_publish_date', 'rss_category', 'rss_views_no', 'rss_video',)
    list_per_page = 10
    list_filter = ( 'rss_category',)
    search_fields = ('id', 'rss_link', 'rss_title', 'rss_publish_date')
    readonly_fields = (
        'thumbnail', )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 10,
                   'cols': 40,
                   'style': 'height: 1em;'})},
    }


    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


#Adv
class Advertise(admin.ModelAdmin):
    list_display = ['adv_image', 'position']
    list_per_page = 10
    list_filter = ['position']
    search_fields = ['position']


admin.site.register(RssCategories, RSSCategory)
admin.site.register(RssProviders, RSSProviders)
admin.site.register(RssFeeds, Feed)
admin.site.register(Adv, Advertise)
