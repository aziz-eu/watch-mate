from rest_framework import serializers
from watchmate_app.models import Movie


class MovieSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too small")

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
