from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from craftbar.beer_catalogue.models import Beer
from craftbar.beer_catalogue.serializers import UserSerializer, GroupSerializer, BeerSerializer
from craftbar.beer_catalogue.permissions import IsOwnerOrReadOnly

from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class BeerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows beers to be viewed or edited.
    """
    queryset = Beer.objects.all().order_by('id')
    serializer_class = BeerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
