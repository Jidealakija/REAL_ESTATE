from django.db import models
import uuid

PROPERTY_STATUS = (
    ('Sales', 'Sale'),
    ('Rent', 'Rent'),
    ('Lease', 'Lease'),
)

PROPERTY_TYPE = (
    ('Terrace', 'Terrace'),
    ('Bungalow', 'Bungalow'),
    ('Duplex', 'Duplex'),
)

class Properties(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    type = models.CharField(choices=PROPERTY_TYPE, max_length=30)
    status = models.CharField(max_length=100, choices=PROPERTY_STATUS)
    address = models.TextField()
    price = models.DecimalField(max_digits=21, decimal_places=2)
    image = models.ImageField(upload_to='property_images')
    other_images = models.ImageField(upload_to='property_images', blank=True, null=True)
    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()
    land_size = models. CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return str(self.id)