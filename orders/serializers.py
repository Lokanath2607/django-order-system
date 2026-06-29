from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, attrs):
        quantity = attrs.get("quantity", getattr(self.instance, "quantity", None))
        product = attrs.get("product", getattr(self.instance, "product", None))

        if product is None:
            raise serializers.ValidationError({"product": "Product is required."})

        if self.instance is None:
            if quantity > product.stock:
                raise serializers.ValidationError(
                    {"quantity": f"Sorry, only {product.stock} {product.name}s left in stock."}
                )
        else:
            old_quantity = self.instance.quantity
            difference = quantity - old_quantity
            if difference > 0 and difference > product.stock:
                raise serializers.ValidationError(
                    {"quantity": f"Sorry, only {product.stock} {product.name}s left in stock."}
                )

        return attrs


