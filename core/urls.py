from django.urls import path
from core.views import ProfileView, ActivateAccount, signup
from . import views as function_views
urlpatterns = [
    path('signup/', function_views.signup, name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),

    path('activate/<uidb64>/<token>/',
         ActivateAccount.as_view(), name='activate'),
]
