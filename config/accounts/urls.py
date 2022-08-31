from django.urls import path
from .views import signup, num, add, addrecord
from accounts.views import signup, Login,SearchResultsView


urlpatterns = [
    path('signup/', signup.as_view(), name = 'signup'),
    path('', Login.as_view(), name = 'login'),
    path('phonebook/',num, name ='phonebook'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('add/',add, name='add'),
    path('add/addrecord/', addrecord, name='tmp/addrecord'),
]
