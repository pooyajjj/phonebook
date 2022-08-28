from django.urls import path
from .views import signup, View

urlpatterns = [
    path('signup/',signup, name = 'accounts' ),
    path('login/',View.as_view(), name = 'login')
    
]

#error 504