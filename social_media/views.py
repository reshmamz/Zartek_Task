from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Feed, Image, Like
from .serializers import FeedSerializer,ImageSerializer, LikeSerializer, FeedListSerializer

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedListSerializer
    permission_classes = [AllowAny]

