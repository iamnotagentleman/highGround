from rest_framework import serializers
from apps.mainsite.app_models.users import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'address', 'note', 'phone_number', 'birth_date', 'job', 'gender', 'current_education', 'experience', 'emergency_contact_information', 'profile_photo')