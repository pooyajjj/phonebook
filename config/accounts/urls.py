from django.urls import path
from .views import signup, num, add, addrecord, delete
from accounts.views import signup, Login,SearchResultsView
from . import views


urlpatterns = [
    path('signup/', signup.as_view(), name = 'signup'),
    path('', Login.as_view(), name = 'login'),
    path('phonebook/',num, name ='phonebook'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('add/',add, name='add'),
    path('add/addrecord/', addrecord, name='tmp/addrecord'),
    path('phonebook/delete/<int:id>', views.delete, name='delete'),
    path('phonebook/update/<int:id>', views.update, name='update'),
    path('phonebook/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
