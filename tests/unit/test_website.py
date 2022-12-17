from django.urls import resolve, reverse
from books.pages.views import HomeView


def test_verify_root_url_maps_to_HomeView():
    match = resolve(reverse("pages:home"))
    assert match.func.view_class == HomeView


def test_homepage_context_is_correctly_set(rf):
    request = rf.get('/')
    view = HomeView()
    view.setup(request)

    context = view.get_context_data()
    assert "title" in context
    assert context['title'] == 'Ma librarie | Acceuil'
