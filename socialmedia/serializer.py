from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserAdminAccessSerializer(serializers.ModelSerializer):

    def get_follow_status(self, to_user):
        loggedin_user = self.context['request'].user
        return loggedin_user.get_follow_status(to_user=to_user)

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'avatar',
            'is_verified',

        )
        read_only_fields = ('id', 'avatar',)


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['avatar']


class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'avatar',
            'is_verified',
        )
        read_only_fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'avatar',
            'is_verified',
        )


class UserMinimalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'avatar',
            'is_verified',
        )
