from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CustomUser, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'phone_number', 'is_email_verified', 'is_phone_verified']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.is_email_verified = validated_data.get('is_email_verified', instance.is_email_verified)
        instance.is_phone_verified = validated_data.get('is_phone_verified', instance.is_phone_verified)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'secret_question', 'secret_answer', 'sex', 'date_of_birth']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user_profile = UserProfile.objects.create(user=user, **validated_data)
            return user_profile
        else:
            raise serializers.ValidationError(user_serializer.errors)


    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.secret_question = validated_data.get('secret_question', instance.secret_question)
        instance.secret_answer = validated_data.get('secret_answer', instance.secret_answer)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.age = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()

        user_serializer = UserSerializer(user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()

        return instance

class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def save(self, **kwargs):
        user = self.context['user']
        user.set_password(self.validated_data['new_password'])
        user.save()
