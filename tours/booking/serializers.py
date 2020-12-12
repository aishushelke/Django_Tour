from rest_framework import serializers
from .models import booking



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=booking
        fields= ["id","package_id","user_id","fromdate","todate"]
