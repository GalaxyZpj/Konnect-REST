from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from oauth2_provider.contrib.rest_framework import TokenHasScope

from .serializers import UserSerializer
from core.models import User, Profile


class UserListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Lists all Users"""
    serializer_class = UserSerializer
    queryset = Profile.objects.all()
    permission_classes = [TokenHasScope, ]
    required_scopes = ['read',]

class UserDetailsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """Retrieves, Updates, Deletes User"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [TokenHasScope, ]
    required_scopes = ['profile',]
    lookup_field = 'username'

class UserSignupViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
