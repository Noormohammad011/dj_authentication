from django.urls import path
from core.views import ProfileView
from . import views as function_views
urlpatterns = [
    path('signup/', function_views.signup, name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),

    path('activate/<uidb64>/<token>/',
         function_views.activate, name='activate'),
]
