from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.


"""
def home(request):
    title = 'pages'
    heading = 'bienvenue'
    return render(request, 'pages/home.html', {'title': title, 'h1': heading})
"""


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ma librarie | Acceuil'
        context['h1'] = 'ma liBRARIE dddddddddddd ddddddddddddddddd ddddddddddddddddddddd'
        return context


"""
def about(request):
    return render(request, 'pages/about.html', )
"""


class AboutView(TemplateView):
    template_name = "pages/about.html"
