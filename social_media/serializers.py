from rest_framework import serializers
from django.utils import timezone

class TagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    weight = serializers.IntegerField()

class FeedSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length = 200)
    # tag = serializers.ManyToManyField('Tag')
    created = serializers.DateTimeField(default=timezone.now)

class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url='task\image')
    feed = FeedSerializer()

class LikeSerializer(serializers.Serializer):
    feed = FeedSerializer()
    # user = serializers.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    like = serializers.BooleanField()

class FeedListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    image = ImageSerializer()
    tag = TagSerializer()
    created = serializers.DateTimeField(default=timezone.now)

    # def validate(self, data):
    #     """
    #     Check that start is before finish.
    #     """
    #     if data['start'] > data['finish']:
    #         raise serializers.ValidationError("finish must occur after start")
    #     return data