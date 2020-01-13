from mint_choc.views import HomePage, AboutPage
from django.urls import path

urlpatterns = [
	path('', HomePage.as_view(), name = 'home'),
	path('about/', AboutPage.as_view(), name='about')
]