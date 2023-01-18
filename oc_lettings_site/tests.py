from django.urls import reverse


def test_dummy():
    assert 1


def test_index_url(client):
    url = reverse("index")
    assert url == "/"
    reponse = client.get(url)
    content = reponse.content.decode()
    reponse_attendu = "<title>Holiday Homes</title>"
    assert reponse.status_code == 200
    assert reponse_attendu in content
