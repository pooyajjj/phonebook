from django.urls import path
from .views import signup, num
from accounts.views import signup, Login,SearchResultsView

urlpatterns = [
    path('signup/', signup.as_view(), name = 'signup'),
    path('', Login.as_view(), name = 'login'),
    path('phonebook/',num, name ='phonebook'),
    path("search/", SearchResultsView.as_view(), name="search_results"),

]
