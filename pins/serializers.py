from rest_framework import serializers
from .models import Category, Pin, Board, SavedPin


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = "__all__"


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class SavedPinSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedPin
        fields = "__all__"

class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = '__all__'