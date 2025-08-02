from .views import signup_view, signin_view, signout_view, home_view
from django.urls import path

urlpatterns = [
    path('', home_view, name='home'),  
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('signout/', signout_view, name='signout'),
]
