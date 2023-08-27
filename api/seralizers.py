from rest_framework import serializers

from .models import category, product, productLine, productImage, attribute, attributeValue

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class productSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = product
        fields = '__all__'

class productLineSerializer(serializers.ModelSerializer):
    attributeValue = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = productLine
        fields = '__all__'
        
class productImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = productImage
        fields = '__all__'

class attributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = attribute
        fields = '__all__'

class attributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = attributeValue
        fields = '__all__'
