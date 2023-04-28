import feedparser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution


import logging
from django.conf import settings
from django.core.management.base import BaseCommand


from django.utils import timezone

from dateutil import parser

from podcasts.models import Episode, Channel


logger = logging.getLogger(__name__)




class Command(BaseCommand):

    def handle(self, *args, **options):
        print("It works!")


        #inp = "https://anchor.fm/s/a5637400/podcast/rss"
        inp = input("Digite o RSS de podcast que deseja adicionar : ")

        feed = feedparser.parse(inp) #RSS DO FLOW
        
        # podcast_title = feed.channel.title
        # podcast_description = feed.channel.description
        # podcast_image = feed.channel.image["href"]
        
        print(feed.entries[0])

        for item in feed.entries:

            if not Channel.objects.filter(channelKey=f"a{hash(item.author)}").exists():

                channel = Channel(
                    title = feed.channel.title,
                    description = feed.channel.description,
                    image = feed.channel.image["href"],
                    link = feed.channel.link,
                    channelKey = f"a{hash(feed.channel.author)}",
                    numberOfEpisode = len(feed.entries),
                    register_date = timezone.now(),
                    creator = feed.channel.author, #creator in databese
                )



            if not Episode.objects.filter(guid=item.guid).exists():

                episode = Episode(
                    title = item.title,
                    description = item.description,
                    pub_date = self.convertTimeToString(item.published_parsed),
                    #pub_date = self.convertTimeToString(item.published_parsed),
                    #pub_date_sec = self.convertTimeToSec(item.published_parsed),
                    time_span = self.tryAcessItem(["duration"], item),
                    link = item.link,
                    image = self.tryAcessItem(["image['href']"], item),  
                    guid = item.guid,
                    creator = item.author, #creator in database

                )


                channel.save()
                episode.save()



    def tryAcessItem(self, args:list, item):
        try:
            for l in args:
                return item.l
            
        except(AttributeError):
            return "None - Sem Atributo"
        except Exception as e:
            print(e)
            return "None - outro erro"




    def convertTimeToString(self, time):
        # time.struct_time(tm_year=2023, tm_mon=4, tm_mday=20, tm_hour=22, tm_min=0, tm_sec=32, tm_wday=3, tm_yday=110, tm_isdst=0)
        return str(time.tm_year) + "-" + str(time.tm_mon) + "-" + str(time.tm_mday) + " " + str(time.tm_hour) +":"+str(time.tm_min)+":"+str(time.tm_sec)

        #YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]



    def convertTimeToSec(self, time):
        res = (((time.tm_mon * 30 + time.tm_mday )* 24 + time.tm_hour ) * 60 + time.tm_min )* 60 + time.tm_sec
        #print(res)
        return res




    def delete_old_job_executions(max_age=604_800):

        DjangoJobExecution.objects.delete_old_job_executions(max_age)
        
