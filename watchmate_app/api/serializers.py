from rest_framework import serializers
from watchmate_app.models import WatchList, StreamPlatform


class WatchListSerializers(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializers(serializers.ModelSerializer):

    watchlist = WatchListSerializers(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"



    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # description = serializers.CharField()
    # isActive = serializers.BooleanField()

    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.isActive = validated_data.get("isActive", instance.isActive)
    #     instance.save()
    #     return instance
