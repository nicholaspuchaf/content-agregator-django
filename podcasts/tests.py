from django.test import TestCase,RequestFactory

from django.utils import timezone

from django.urls.base import reverse

from datetime import datetime

from .models import Episode


# Create your tests here.



class PodcastsTests(TestCase):

    def setUp(self):
        self.episode = Episode.objects.create(
            title="MRG ESPECIAL DE NATAL",
            description="MRG ESPECIAL DE NATAL DESCRICAO",
            pub_date=timezone.now(),
            link="https://spotify.com/MRG",
            image="httos://spotify.com/MRG/image",
            podcast_name="MRG",
            guid=hash("MRG ESPECIAL DE NATAL"),#TITLE
            time_span = 3600
        )
        self.factory = RequestFactory()
        


    def test_episode_content(self):
        self.assertEqual(self.episode.description, "MRG ESPECIAL DE NATAL DESCRICAO")
        self.assertEqual(self.episode.link, "https://spotify.com/MRG")
        self.assertEqual(self.episode.guid, hash("MRG ESPECIAL DE NATAL"))

    def test_episode_str_representation(self):
        self.assertEqual(
        str(self.episode), "MRG : MRG ESPECIAL DE NATAL"
        )

    def test_home_page_status_code(self):
        response = self.client.get('/podcasts')
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('homepage', urlconf="podcasts.urls"))
        self.assertEqual(response, "homepage.html")

    def test_home_page_list_content(self):
        response = self.client.get(reverse('homepage',urlconf="podcasts.urls"))
        self.assertContains(response, "MRG ESPECIAL DE NATAL")


