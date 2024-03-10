from django.urls import path, re_path
from portfolio.views import Homepage
from .views import ContactView

app_name='portfolio'

urlpatterns = [
    re_path(r'^$', Homepage.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]
