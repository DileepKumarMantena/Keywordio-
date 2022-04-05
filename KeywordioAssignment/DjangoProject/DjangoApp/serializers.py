from rest_framework import serializers

from .models import *


class AdminRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminTable
        fields = "__all__"


class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminTable
        fields = ['id','Email', 'Password']
        extra_kwargs = {'Password': {'write_only': True}}

    def create(self, validated_data):
        user = AdminTable.objects.get(Email=validated_data['Email'])
        user.save()
        return user


class BooksEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksTable
        fields = "__all__"
