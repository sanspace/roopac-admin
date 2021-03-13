from django.db import models
from django.urls import reverse

ORDER_STATUS = (
    ('n', 'new'),
    ('d', 'design'),
    ('r', 'po-raised'),
    ('a', 'po-accepted'),
    ('c', 'po-complete'),
    ('o', 'out-for-delivery'),
    ('s', 'delivery-complete'),
    ('x', 'complete'),
)

PO_STATUS = [
    ('c', 'created'),
    ('a', 'accepted'),
    ('s', 'completed'),
]

class RooBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RooPersonModel(RooBaseModel):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)

    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

    class Meta:
        ordering = ['name']

class RooOrderModel(RooBaseModel):
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(blank=True, null=True)


    class Meta:
        ordering = ['start_date']

class Customer(RooPersonModel):
    ...

class Supplier(RooPersonModel):
    ...

class Order(RooOrderModel):
    status = models.CharField(choices=ORDER_STATUS, default='n', max_length=15)
    customer = models.ForeignKey('Customer', on_delete=models.RESTRICT, null=False)

    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'{self.start_date} {self.status}'

class PurchaseOrder(RooOrderModel):
    status = models.CharField(choices=PO_STATUS, default='c', max_length=15)
    base_order = models.ForeignKey('Order', on_delete=models.RESTRICT, null=False, verbose_name='Order')
    supplier = models.ForeignKey('Supplier', on_delete=models.RESTRICT, null=False)

    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'{self.start_date} {self.status}'
