from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.id, filename) #this will guess the id of the user and create a directory for each user and save the file in that directory
    
    
class Category(models.Model):
    cid = ShortUUIDField(unique=True,length=10,max_length=20,prefix='cat',alphabet="abcdefgh12345")
    title = models.CharField(max_length=100,default="category")
    image = models.ImageField(upload_to="user_directory_path",default="category.png")
    description = models.TextField(null=True, blank=True,default="this is a category")

    class Meta:
        verbose_name_plural = "Categories"
    def category_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

def __str__(self):
    return self.title

class Vendor(models.Model): # this class is for vendors registration and separate id will be generated for each vendor
    vid = ShortUUIDField(unique=True,length=10,max_length=20,prefix='ven',alphabet="abcdefgh12345")
    title = models.CharField(max_length=100,default="vendor")
    image = models.ImageField(upload_to="user_directory_path",default="vendor.png")
    description = models.TextField(null=True, blank=True,default="this is a vendor")
    chat_response = models.TextField(null=True, blank=True)
    shipping = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    authentication = models.ImageField(upload_to="user_directory_path")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # this will create a foreign key relationship with the user model and set the user to null if the user is deleted')

    class Meta:
        verbose_name_plural = "Vendors"
    def category_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    def __str__(self):
        return self.title

class Product(models.Model): # this class is for products registration and separate id will be generated for each product
    pid = ShortUUIDField(unique=True,length=10,max_length=20,prefix='prd',alphabet="abcdefgh12345")
    title = models.CharField(max_length=100,default="product")
    image = models.ImageField(upload_to="user_directory_path",default="product.png")
    description = models.TextField(null=True, blank=True,default="this is a product")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)# this will create a foreign key relationship with the category model and set the category to null if the category is deleted')
    specification = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"
    def category_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    def __str__(self):
        return self.title


class ProductImage(models.Model): # this class is for product images and separate id will be generated for each product image
    pid = ShortUUIDField(unique=True,length=10,max_length=20,prefix='prdi',alphabet="abcdefgh12345")
    image = models.ImageField(upload_to="user_directory_path",default="productimage.png")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True) # this will create a foreign key relationship with the product model and delete the product image if the product is deleted')  
    date = models.DateTimeField(auto_now_add=True) # this will create a date field and set the date to the current date and time when the product image is created

    class Meta:
        verbose_name_plural = "Product Images"
    def category_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    def __str__(self):
        return self.title
    
#create class order when needed
#product class when needed
#wishlist class when needed
#cart class when needed
#address class when needed

