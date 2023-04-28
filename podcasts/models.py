from django.db import models

#from django.utils import timezone

# Create your models here.

class Channel(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.CharField(max_length=150)
    link = models.URLField()
    channelKey=models.CharField(max_length=200) #tem que comecar com letra para virar id de html
    numberOfEpisode = models.IntegerField()
    register_date = models.DateTimeField()
    creator = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.title}"

    def guidNum(self) -> int:
        return self.guid
    



class Episode(models.Model):
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    pub_date = models.DateTimeField()
    #pub_date_sec = models.BigIntegerField()
    time_span = models.CharField(max_length=30)
    link = models.URLField()
    image = models.CharField(max_length=100) # ARRUMAR DEPOIS PARA ADICIONAR IMAGEM
    podcast_name = models.CharField(max_length=150)
    guid = models.CharField(max_length=30)
    creator = models.CharField(max_length=100)


    def __str__(self) -> str:
        return f"{self.podcast_name} : {self.title}"
    


class New(models.Model):

    title = models.CharField(max_length=250)

