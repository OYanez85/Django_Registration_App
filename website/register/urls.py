from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.index, name='index'),
    # path('', views.reg_view, name='reg_view'),
    path('', views.RegFormView.as_view(), name='reg_view'),
    # Add the following line for the signup view
    path('signup/', views.signup_view, name='signup_view'),
    path('reg_complete/', views.reg_complete, name='reg_complete'),
    #path('signup/', views.SignupFormView.as_view(), name='signup')
    
]