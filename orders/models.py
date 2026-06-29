from django.db import models
from django.conf import settings
from products.models import Product
from django.core.exceptions import ValidationError
from django.utils import timezone

STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('SHIPPED', 'Shipped'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
]

VALID_TRANSITIONS = {
    'PENDING': ['CONFIRMED', 'CANCELLED'],
    'CONFIRMED': ['SHIPPED', 'CANCELLED'],
    'SHIPPED': ['DELIVERED'],
    'DELIVERED': [],
    'CANCELLED': [],
}

class Order(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    confirmed_at = models.DateTimeField(null=True, blank=True)
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_order = Order.objects.get(pk=self.pk)
            if old_order.status != self.status:
                allowed = VALID_TRANSITIONS.get(old_order.status, [])
                if self.status not in allowed:
                    raise ValidationError(
                        f"Invalid transition: {old_order.status} → {self.status}"
                    )

                # Set timestamps when status changes
                if self.status == 'CONFIRMED' and not self.confirmed_at:
                    self.confirmed_at = timezone.now()
                elif self.status == 'SHIPPED' and not self.shipped_at:
                    self.shipped_at = timezone.now()
                elif self.status == 'DELIVERED' and not self.delivered_at:
                    self.delivered_at = timezone.now()
                elif self.status == 'CANCELLED' and not self.cancelled_at:
                    self.cancelled_at = timezone.now()

        super().save(*args, **kwargs)



        

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
