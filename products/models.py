class Category(models.Model):
    """
    Category model for organizing products into groups.
    
    Attributes:
        name (str): Internal name used in queries and filtering
        friendly_name (str): User-facing name displayed on the site
    """
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """Returns the user-friendly name of the category"""
        return self.friendly_name


class Product(models.Model):
    """
    Product model representing books and items sold in the store.
    
    Attributes:
        category (ForeignKey): Reference to Category model
        name (str): Name of the product/book
        description (TextField): Detailed description
        price (Decimal): Price in store currency
        rating (Decimal): Customer rating from 0-5
        image_url (URLField): Optional external image URL
        image (ImageField): Optional uploaded product image
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=350)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
