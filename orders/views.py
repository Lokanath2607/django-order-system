from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'product']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=user)




