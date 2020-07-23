from rest_framework import viewsets,status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Feed, Image, Like
from .serializers import FeedSerializer,ImageSerializer,LikesSerializer
from rest_framework.decorators import action


# class FeedViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Feed.objects.all()
#     serializer_class = FeedSerializer
#     permission_classes = [AllowAny]

class FeedViewSet(viewsets.ViewSet):
    serializer_class = FeedSerializer

    def list(self, request):
        feed = Feed.objects.all()
        serializer = FeedSerializer(feed,many=True)

        # like = Like.objects.filter(feed__in=feed,user=request.user)
        # serializer = LikesSerializer(like,many=True)

        print(serializer.data)

        return Response(serializer.data)





    # class LikeViewSet(viewsets.ViewSet):
#
#     serializer_class = LikesSerializer
#
#     def create(self,request):
#         serializer = LikesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'Success'})
#
#         else:
#             return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#
#     def update(self,request,pk=None):
#         like = Like.objects.get(pk=pk)
#         serializer = LikesSerializer(instance=like, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#
#         return Response({'http_method':'PUT'})
# #


class LikeViewSet(viewsets.ViewSet):
    serializer_class = LikesSerializer

    def create(self,request):
        serializer = LikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Success'})
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        like = Like.objects.get(pk=pk)
        serializer = LikesSerializer(like)
        return Response(serializer.data)

    def update(self,request,pk=None):
        like = Like.objects.get(pk=pk)
        serializer = LikesSerializer(instance=like,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def list(self, request):
        like = Like.objects.all()
        serializer = LikesSerializer(like,many=True)
        print(serializer.data)

        return Response(serializer.data)


