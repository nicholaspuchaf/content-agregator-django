
from django import template


register = template.Library()

@register.filter
def getChannelKey(d, key):
    return d[key].channelKey



