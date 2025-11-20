# products/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    # Required Fields
    name = models.CharField(max_length=255)
    
    # ForeignKey to Category (on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="products" 
    )
    
    # DecimalField with two decimal places
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Optional Fields
    description = models.TextField(blank=True, null=True) 
    
    # ImageField, upload_to='products/'
    image = models.ImageField(
        upload_to='products/', 
        blank=True, 
        null=True
    )
    
    # Automatic timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    # __str__ method
    def __str__(self):
        return self.name

    # Helper for template display
    def get_display_price(self):
        return f"${self.price:,.2f}"