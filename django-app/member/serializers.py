from django.contrib.auth import get_user_model
from rest_framework import serializers, generics

User = get_user_model()


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'nickname',
            'img_profile',
        )


class UserCreationSerializer1(serializers.Serializer):
    email = serializers.CharField()
    nickname = serializers.CharField(max_length=20)
    img_profile = serializers.ImageField()
    username = serializers.CharField(max_length=20)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exist')
        return email

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords didn\'t match')
        return data

    def create(self, validated_data):
        username = self.validated_data.get('username', '')
        nickname = self.validated_data.get('nickname', '')
        email = self.validated_data.get('email', '')
        img_profile = self.validated_data.get('img_profile', '')
        password = self.validated_data.get('password1', '')
        user = User.objects.create_user(
            username=username,
            nickname=nickname,
            email=email,
            password=password,
            img_profile=img_profile,

        )
        return user


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'nickname',
            'img_profile',
            'username',
            'password',
            'password2',
        )

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exist')
        return email

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords didn\'t match')
        return data


    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            **validated_data
        )
        return user
