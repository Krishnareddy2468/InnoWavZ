from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.id, filename)

class category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cat', alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="category")
    image = models.ImageField(upload_to=user_directory_path, default="category.png")
    description = models.TextField(null=True, blank=True, default="this is a category")

    class Meta:
        verbose_name_plural = "category"

    def category_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    def __str__(self):
        return self.title

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='ven', alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="vendor")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.png")
    description = models.TextField(null=True, blank=True, default="this is a vendor")
    chat_response = models.TextField(null=True, blank=True)
    shipping = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    authentication = models.ImageField(upload_to=user_directory_path)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    def __str__(self):
        return self.title

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='prd', alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="product")
    image = models.ImageField(upload_to=user_directory_path, default="product.png")
    description = models.TextField(null=True, blank=True, default="this is a product")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True)
    specification = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='prdi', alphabet="abcdefgh12345")
    image = models.ImageField(upload_to=user_directory_path, default="productimage.png")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

    def product_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    def __str__(self):
        return self.pid