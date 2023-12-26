from django.db import models

# Create your models here.
class recipes(models.Model):
    
    recipe_name = models.CharField( max_length = 200 )
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to = "recipe")

    