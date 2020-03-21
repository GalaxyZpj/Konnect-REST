from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('rest_auth/', include('rest_framework.urls')),
    path('user/', include('authentication.urls')),
] 

# OAuth2 provided urls

# base_urlpatterns = [
#     url(r"^authorize/$", views.AuthorizationView.as_view(), name="authorize"),
#     url(r"^token/$", views.TokenView.as_view(), name="token"),
#     url(r"^revoke_token/$", views.RevokeTokenView.as_view(), name="revoke-token"),
#     url(r"^introspect/$", views.IntrospectTokenView.as_view(), name="introspect"),
# ]


# management_urlpatterns = [
#     # Application management views
#     url(r"^applications/$", views.ApplicationList.as_view(), name="list"),
#     url(r"^applications/register/$", views.ApplicationRegistration.as_view(), name="register"),
#     url(r"^applications/(?P<pk>[\w-]+)/$", views.ApplicationDetail.as_view(), name="detail"),
#     url(r"^applications/(?P<pk>[\w-]+)/delete/$", views.ApplicationDelete.as_view(), name="delete"),
#     url(r"^applications/(?P<pk>[\w-]+)/update/$", views.ApplicationUpdate.as_view(), name="update"),
#     # Token management views
#     url(r"^authorized_tokens/$", views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
#     url(r"^authorized_tokens/(?P<pk>[\w-]+)/delete/$", views.AuthorizedTokenDeleteView.as_view(),
#         name="authorized-token-delete"),
# ]
