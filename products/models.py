from django.db import models
from base.models import  BaseModel
from django.utils.text import slugify



class Category(BaseModel):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category_image=models.ImageField(upload_to="categories")

    def save(self , *args , **kwargs):
        self.slug = slugify(self.category_name)
        super(Category ,self).save(*args , **kwargs)

    def __str__(self) -> str:
        return self.category_name
    

class ColorVariant(BaseModel):
    color_name= models.CharField(max_length=100)
    price=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.color_name

class SizeVarient(BaseModel):
    size_name=models.CharField(max_length=100)
    price=models.IntegerField(default=0) 

    def __str__(self) -> str:
        return self.size_name

class Products(BaseModel):
    products_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price=models.IntegerField()
    products_descriptions=models.TextField()
    color_name=models.ManyToManyField(ColorVariant,blank=True)
    size_variant=models.ManyToManyField(SizeVarient,blank=True)



    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.products_name)
        super(Products ,self).save(*args , **kwargs)

    def __str__(self) -> str:
        return self.products_name
    
    


class ProductImage(BaseModel):
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="product_images")
    image=models.ImageField(upload_to="product")



class Coupon(BaseModel):
    coupon_code=models.CharField(max_length=18)
    is_expired=models.BooleanField(default=False)
    discount_price=models.ImageField(default=100)
    minimum_amount=models.IntegerField(default=500)
