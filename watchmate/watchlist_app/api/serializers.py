from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        #fields = ["id", "name", "description"]
        #exclude = ["name"]

    def validate_name(self, name):
        if len(name) < 2:
            raise serializers.ValidationError("Movie name must be at least 2 characters long")
        return name

    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError("Movie name must be different to it's description")
        return data

# # Validator for the description
# def description_validator(value):
#     if len(value) < 5:
#         raise serializers.ValidationError("Movie description must be at least 5 characters long")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_validator])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance


#     # Level-field validation
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Movie name must be at least 2 characters long")
#         return value

#     # Object-level validation
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Movie name must be different to it's description")
#         return data

