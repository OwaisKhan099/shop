from rest_framework import serializers
from .models import CustomUser



class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop("password",None)
        print("in serializer  ____ ",password)
        # password = validated_data.pop("password","no")
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    def update(self, instance, validated_data):
        for attr,value in validated_data:
            if attr == "password":
                instance.set_password(value)
            else:
                setattr(instance,attr,value)
    class Meta:
        model = CustomUser
        extra_kwargs = {"password":{"write_only":True}}
        fields = ("name", "email", "phone", "session_token", "password", "is_active", "is_staff", "is_superuser")
