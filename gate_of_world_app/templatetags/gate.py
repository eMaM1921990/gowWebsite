import urllib2

__author__ = 'emam'
from django import template

register = template.Library()

@register.simple_tag
def get_or_404(url):
    try:
        ret = urllib2.urlopen(url)
        if ret.code == 200:
            return True
    except Exception as e:
        return False
    return False