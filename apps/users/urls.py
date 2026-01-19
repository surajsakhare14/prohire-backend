from django.urls import path
from .views import home, MeView

urlpatterns = [
    path('', home, name='home'),

    path('me/', MeView.as_view(), name='me'),
]