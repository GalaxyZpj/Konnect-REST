from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from core.models import Profile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    gender = serializers.ChoiceField(choices=GENDER, required=True)
    dob = serializers.DateField(format="%Y-%m-%d", required=True)
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'gender', 'dob', 'mobile',
                  'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        user = get_user_model().objects.create_user(**{
            'username': validated_data['username'],
            'email': validated_data['email'],
            'mobile': validated_data['mobile'],
            'password': validated_data['password']
        })
        profile = Profile(
            user=user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            dob=validated_data['dob'],
        )
        profile.save()
        return user
    
    def update(self, instance, validated_data):
        """Updates the user and profile model for the user"""
        profile = Profile.objects.get(user=instance)
        profile.first_name = validated_data['first_name']
        profile.last_name = validated_data['last_name']
        profile.dob = validated_data['dob']
        profile.gender = validated_data['gender']
        profile.save()
        return instance

    def to_representation(self, instance):
        """Used to modify the serializer output"""
        # ret =  super().to_representation(instance)
        # ret =  super().to_representation(get_user_model().objects.get(username=instance.username))
        if self.context['request'].method == 'POST':
            ret = {
                "message": "success",
                "username": instance.username
            }
        else:
            profile = Profile.objects.get(user=instance)
            ret = {
                'username': profile.user.username,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'gender': profile.gender,
                'dob': profile.dob,
                'mobile': profile.user.mobile,
                'email': profile.user.email
            }
        return ret
