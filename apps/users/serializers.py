from django.contrib.auth import get_user_model
from django.serializers import UserSerializer
from django_countries import CountryField
from phonenumber_field.serializersfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ImageField(source="profile.profile_photo")
    country= CountryField(source="profile.country")
    city= serializers.CharField(source="profile.city")
    top_seller= serializers.BooleanField(source="profile.top_seller")
    first_name= serializers.SerializerMethodField()
    last_name= serializers.SerializerMethodField()
    full_name= serializers.SerializerMethodField(source='get_full_name')

    class Meta:
        model = User
        fields = ['id',
        'first_name',
        'last_name', 
        'username',
        'gender',
        'email',
        'phone_number', 
        'profile_photo',
        'country',
        'city', 
        'top_seller',
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()
    
    def get_last_name(self, obj):
        return obj.last_name.title()

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreationModel.Meta):
        model = User
        fields = ['id', 
        'username', 
        'email', 
        'firstname',
        'lastname',
        'password',
        ]

