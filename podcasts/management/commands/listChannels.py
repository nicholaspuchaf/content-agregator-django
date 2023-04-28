


from django.conf import settings
from django.core.management.base import BaseCommand

from podcasts.models import Episode, Channel


class Command(BaseCommand):


    def handle(self, *args, **options):
        print("Listing episodes by channel")
        i = 0
        keyMap = {}
        for item in Channel.objects.filter().order_by("register_date"):
            i = i + 1
            print(item.title)
            print(f"{i} : {item.channelKey}")
            keyMap[i] = item.channelKey
            


        #ESCOLHER UM CANAL ESPECIFICO E MOSTRAR INFORMACOES SOBRE ESTE CANAL

        while 1:
            try:
                whichChannel = int(input("Digite qual canal deseja acessar : "))

                itemWished = Channel.objects.filter(channelKey = keyMap[whichChannel])

                break

            except Exception as err:
                print(err)
                inp = input("Tentar novamente ? (y/n)")

                if inp == 'n':
                    break
        

        wannaShowChannel = input("Deseja ver canal ? (y/n)")

        if wannaShowChannel == 'y':

            print(itemWished)

        
        #MOSTRAR EPISODEOS DO CANAL


        while 1:
            wannaShowEpisodesHowMany = input("Quantos episodios deseja ver ? (int)")
            

            try:    
                if wannaShowEpisodesHowMany > 0:
                    
                    for item in Episode.objects.filter(creator=item.creator).order_by("-register_date")[wannaShowEpisodesHowMany]:
                        print(item)
                break

                    
            except Exception as err:
                print(err)

                inp = input("Quer rodar novamente ? (y/n) ")
                if inp == 'n':
                    break
            
        
        