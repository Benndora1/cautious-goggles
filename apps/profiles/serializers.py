from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from apps.ratings.serializers import RatingSerializer
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username =  serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

