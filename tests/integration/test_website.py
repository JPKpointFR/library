from django.urls import reverse


def test_my_website_is_online(client):
    '''Description détaillée du test.'''
    response = client.get(reverse("pages:home"))
    assert response.status_code == 200


def test_homepage_context_contains_a_title(client):
    '''Description détaillée du test.'''
    response = client.get(reverse("pages:home"))
    assert "title" in response.context
    assert response.context['title'] == 'Ma librarie | Acceuil'
