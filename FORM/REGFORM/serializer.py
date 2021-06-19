from rest_framework import serializers
from . models import registration, complaint

class registrationserializer(serializers.Serializer):
    firstname=serializers.CharField(max_length=30)
    lastname=serializers.CharField(max_length=30)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=30)
    cnic=serializers.CharField(max_length=30)

    def create(self, validated_data):
        return registration.objects.create(**validated_data)

class complaintserializer(serializers.Serializer):
    firstname=serializers.CharField(max_length=30)
    lastname=serializers.CharField(max_length=30)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=30)
    city=serializers.CharField(max_length=30)
    desc=serializers.CharField(max_length=30)

    def create(self, validated_data):
        return complaint.objects.create(**validated_data)
