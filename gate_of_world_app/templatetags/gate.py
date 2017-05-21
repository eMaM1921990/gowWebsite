import urllib2

__author__ = 'emam'
from django import template
from django.template.defaultfilters import stringfilter
import re


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


@register.filter
@stringfilter
def youtube(url):
    regex = re.compile(r"^(https://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})")
    match = regex.match(url)
    if not match: return url
    video_id = match.group('id')
    return """
    https://www.youtube.com/embed/{}
     """.format(video_id)
youtube.is_safe = True  # Don't escape HTML