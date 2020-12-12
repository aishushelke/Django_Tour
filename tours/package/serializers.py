from rest_framework import serializers
from .models import package



class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=package
        fields= ["id","pname","ptype","plocation","price"]

class UpdatePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = package
        fields = ["id", "pname","ptype","plocation","price"]

