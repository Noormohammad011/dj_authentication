from django.urls import path
from core.views import ProfileView
from . import views as function_views
urlpatterns = [
    path('signup/', function_views.signup, name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),

    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         function_views.activate, name='activate'),
]
