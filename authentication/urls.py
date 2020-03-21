from django.urls import path

from .views import *


user_list = UserListViewSet.as_view({ 'get': 'list'} )
user_signup = UserSignupViewSet.as_view({ 'post': 'create' })
user_details = UserDetailsViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy'
})


urlpatterns = [
    path('list/', user_list, name='user-list'),
    path('details/<slug:username>/', user_details, name='user-details'),
    path('register/', user_signup, name='user-register'),
]
