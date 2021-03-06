from rest_framework import serializers
from .models import Category, Subcategory, Ad

class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'