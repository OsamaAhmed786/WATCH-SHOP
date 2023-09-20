from django.db import models

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField(null=True, blank=True)
    
    NIKE = 'NIKE'
    HUBLOT = 'HUBLOT'
    GSHOK = 'G-SHOK'
    ROLEX = 'ROLEX'
    ADDIDAS = 'ADDIDAS'
    
    BRAND_TYPE_CHOICES = [
        (NIKE, 'NIKE'),
        (HUBLOT, 'HUBLOT'),
        (GSHOK, 'G-SHOK'),
        (ROLEX, 'ROLEX'),
        (ADDIDAS, 'ADDIDAS')
    ]

    brand = models.CharField(max_length=20, choices=BRAND_TYPE_CHOICES, default=NIKE)


    Category_Quantity = models.IntegerField()
    Stock_availble = models.BooleanField(default=True)


    def __str__(self):
        return self.Name




# this is Product  model

class Product(models.Model):
    P_Name = models.CharField(max_length=100)

    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    X_LARGE = 'x-large'

    SIZE_TYPE_CHOICES = [
        (SMALL , 'small'),
        (MEDIUM , 'medium'),
        (LARGE , 'large'),
        (X_LARGE , 'x-large')
    ]

    Size = models.CharField(max_length=30, choices=SIZE_TYPE_CHOICES, default=SMALL)

    BLACK = 'black'
    WHITE =  'white'

    COLOUR_TYPE_CHOICES = [
        (BLACK , 'black'),
        (WHITE,  'white')
    ]

    Colour = models.CharField(max_length=30, choices=COLOUR_TYPE_CHOICES, default=BLACK)
    Price = models.PositiveIntegerField()
    Rating = models.PositiveIntegerField()
    Add_To_favourite = models.BooleanField(default=True)
    
    ELECTRONICS = 'Electronics'
    CLOTHING = 'Clothing'
    WATCH = 'watch'

    PRODUCT_TYPE_CHOICES = [
        (ELECTRONICS, 'Electronics'),
        (CLOTHING, 'Clothing'),
        (WATCH, 'watch'),
    ]

    Product_Type = models.CharField(
        max_length=20,
        choices=PRODUCT_TYPE_CHOICES,
        default=ELECTRONICS,  # You can set a default value if needed
    )

    Description = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.P_Name




class Contact(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100) 
    Email = models.EmailField(unique=True)
    massage = models.TextField()
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
    
    

