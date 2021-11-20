from django.test import TestCase
from django.utils import timezone
from .models import Episode

# Create your tests here.
class PodCastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title="Another Python Podcast Episode",
            description="Some description",
            pub_date=timezone.now(),
            link="https://jasviers.tech",
            image="https://image.jasviers.tech",
            podcast_name="Podcast",
            guid="locotroco_guild_code",
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.description, "Some description")
        self.assertEqual(self.episode.link, "https://jasviers.tech")
        self.assertEqual(
            self.episode.guid, "locotroco_guild_code"
        )

    def test_episode_str_representation(self):
        self.assertEqual(
            str(self.episode), "Podcast: Another Python Podcast Episode"
        )

