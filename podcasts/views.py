from django.shortcuts import render

# Create your views here.


from django.views.generic import ListView

from .models import Episode, Channel


class HomePageView(ListView):

    template_name = "homepage.html"
    model = Episode

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 

        context["channels"] = {}
        context["channelsInfo"] = {} #Channel.objects.filter().order_by("register_date")[:10]
        #context["names"] = [x.title for x in Channel.objects.filter().order_by("register_date")]

        for item in Channel.objects.filter().order_by("register_date"):
            
            #temp = 
            context["channelsInfo"][item.creator] = item
            context["channels"][item.creator] = Episode.objects.filter(creator=item.creator).order_by("-pub_date")[:10] #author in the json recieved

        #context["episodes"] = Episode.objects.filter().order_by("-pub_date")[:10]
        #context["channels"] = Channel.objects.filter().order_by("register_date")[:5]
        return context


    def chooseRightEpisodes(self, listOfEpisodes : list, nameOfPodcast : str):
        """ Esta funcao irá selecionar os episodeos de determinado podcast para que fique cada episodeo em sua aba.
            O algoritmo não será o ideal mas será otimizado depois. Por enquanto o problema será que terá que ler todos os episodeos
            para separar de qual canal que é.
        """
        listaToReturn = []        
        for item in listOfEpisodes:

            if item.title == nameOfPodcast:
                listaToReturn.append(item)

        return listaToReturn
