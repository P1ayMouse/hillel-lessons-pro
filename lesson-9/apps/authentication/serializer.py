from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']


class RegistrationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'username']

    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password2 != password:
            raise serializers.ValidationError({'detail': 'Password mismatch'})
        elif len(password) < 6:
            raise serializers.ValidationError({'detail': 'Password is too small'})

        username = self.validated_data['username']
        if len(username) < 6:
            raise serializers.ValidationError({'detail': 'Username is too small'})

        user.save()
        return user


# class UpdateUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['email', 'password', 'password2', 'username']
#         read_only_fields = ['email', ]
#
#     def update(self, instance, validated_data):
#         password = validated_data.get('password')
#         password2 = validated_data.get('password2')
#         email = validated_data.get('email')
#         username = validated_data.get('username')
#
#         if password != password2:
#             raise serializers.ValidationError({'detail': 'Password mismatch'})
#         elif len(password) < 6:
#             raise serializers.ValidationError({'detail': 'Password is too small'})
#         elif email != instance.email:
#             raise serializers.ValidationError({'detail': 'Email mismatch'})
#         elif username != instance.username:
#             raise serializers.ValidationError({'detail': 'Username mismatch'})
#         else:
#             instance.email = email
#             instance.username = username
#             instance.set_password(password)
#             instance.save()
#             return instance
