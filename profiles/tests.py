import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from django.test import Client


@pytest.mark.django_db
class TestProfiles:

    def test_profiles_index(self):
        client = Client()
        url = reverse('profiles:index')
        reponse = client.get(url)
        content = reponse.content.decode()
        resultat_attendu = "<h1>Profiles</h1>"
        assert resultat_attendu in content
        assert reponse.status_code == 200

    def test_detail_profile(self):
        client = Client()
        utilisateur = User.objects.create(username='Eulalier', first_name='Eulalie',
                                          last_name='Rajaonarivelo',
                                          email='eulalie@gmail.com',)
        Profile.objects.create(
            user=utilisateur,
            favorite_city='Tokyo',)
        url = reverse('profiles:profile', kwargs={'username': 'Eulalier'})
        reponse = client.get(url)
        content = reponse.content.decode()
        resultat_attendu = "<h1>Eulalier</h1>"
        assert resultat_attendu in content
        assert reponse.status_code == 200
