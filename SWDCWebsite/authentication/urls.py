from django.urls import path
from . import views
urlpatterns = [
    path('', views.VolunteerRegistrationView, name='vreg'),
    path('coord-registration', views.CoordRegistrationView, name='creg'),
    path('login', views.LoginView, name='login'),
    path('logout', views.LogoutView, name='logout')
]
