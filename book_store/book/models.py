from django.db import models

# Create your models here.
class BookstoreModel(models.Model):
    
    CATEGORY =(
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Sci_Fi', 'Sci_fi'),
        ('Humor','humor'),
        ('Horror','Horror'),
        
    )
    id= models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    category=models.CharField(max_length=30 ,choices= CATEGORY)
    frist_pub =models.DateTimeField(auto_now_add=True)
    last_pub =models.DateField(auto_now =True)

