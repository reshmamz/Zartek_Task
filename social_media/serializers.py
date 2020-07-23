from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.utils import timezone
from .models import Like,Feed,Image,Tag
from django.contrib.auth.models import User


class TagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    weight = serializers.IntegerField()

class FeedSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length = 200)
    tag = serializers.StringRelatedField(many=True)
    created = serializers.DateTimeField(default=timezone.now)
    image = serializers.SerializerMethodField('get_image')
    # like = serializers.SerializerMethodField('get_like')
    like_count = serializers.SerializerMethodField('get_like_count')
    dislike_count = serializers.SerializerMethodField('get_dislike_count')

    def get_image(self,obj):
        data = Image.objects.filter(feed=obj.id)
        serializer = ImageSerializer(data,many=True)
        return serializer.data

    def get_like_count(self,obj):
        like_count = Like.objects.filter(feed=obj.id,like=1).count()
        return like_count

    def get_dislike_count(self,obj):
        dislike_count = Like.objects.filter(feed=obj.id,like=0).count()
        return dislike_count

    # def get_like(self,obj):
    #
    #     data = Like.objects.filter(feed=obj.id,user=1)
    #     serializer = LikesSerializer(data,many=True)
    #     print('lllllllllllllllllllllllllllllllllll')
    #     print(obj.id)
    #     print(serializer.data)
    #     pass

class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField(use_url=True)
    # feed = serializers.PrimaryKeyRelatedField(queryset=Feed.objects.all())

class LikesSerializer(serializers.Serializer):
    feed = serializers.PrimaryKeyRelatedField(queryset=Feed.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    like = serializers.BooleanField()

    def create(self, validated_data):
        return Like.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.feed = validated_data.get('feed', instance.feed)
        instance.user = validated_data.get('user', instance.user)
        instance.like = validated_data.get('like', instance.like)
        instance.save()
        return instance