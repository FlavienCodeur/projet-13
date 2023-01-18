import pytest
from django.urls import reverse

from .models import Letting, Address


@pytest.fixture
def address():
    address = Address.objects.create(number="3",
                                     street="Vac", city="Pitsburgh",
                                     state="Pensilvanya", zip_code="47850", country_iso_code="142")
    return address


@pytest.fixture
def letting(address):
    letting = Letting.objects.create(title="Villa", address=address)
    print(letting.address)
    return letting


class TestLettingsView:
    @pytest.mark.django_db
    def test_letting_index(self, client, letting):
        reponse = client.get(reverse('lettings:index'))
        assert reponse.status_code == 200
        assert b'<title>Lettings</title>' in reponse.content

    @pytest.mark.django_db
    def test_detail_letting(self, client, letting):
        reponse = client.get(reverse('lettings:letting', args=[letting.id]))
        assert reponse.status_code == 200
        assert b'<title>Villa</title>' in reponse.content
