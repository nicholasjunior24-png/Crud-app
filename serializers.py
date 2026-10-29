from.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'created_at', 'updated_at']

        read_only_fields = ['id', 'created', 'updated_at']

    def validate_name(self, value):
        if not value.stripe():
            raise serializers.ValidationError(
                "Product cannot be empty!!"
            )
        return value.stripe()

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price cannot be less than zero"
            )
        return value

            