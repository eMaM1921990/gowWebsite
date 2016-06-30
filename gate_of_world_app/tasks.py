from celery.task.base import periodic_task

__author__ = 'emam'
from djcelery import celery
from Feed import *
from celery import shared_task


@celery.task
def SyncFeed():
    feedInstace=Feed()
    feedInstace.feedParser()

@celery.task
def add(x, y):
    print x + y


