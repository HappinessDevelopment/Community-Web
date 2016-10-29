from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .. import serializers
from rest_framework import viewsets

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.group.GroupSerializer