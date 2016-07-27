from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gate_of_world_app.Feed import Feed
import logging
logger = logging.getLogger(__name__)
__author__ = 'emam'

@never_cache
@api_view(['GET'])
def fetchFeeds(request):
    resp={}
    resp['status']=False
    try:
        feedInstace=Feed()
        feedInstace.feedParser()
        resp['status']=True
    except Exception as e:
        logger.debug(str(e))

    return Response(resp)

