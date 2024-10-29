from django.db import models
from django.utils.text import slugify
# Create your models here.
class LCategory(models.Model):
    d_category_name=models.CharField(max_length=1000)

    def __str__(self):
        return self.d_category_name


class LPost(models.Model):
    d_title=models.CharField(max_length=1000)
    d_content=models.TextField()
    d_img_url=models.URLField(blank=True)
    d_created_at=models.DateField(auto_now_add=True)
    d_slug=models.SlugField(unique=True)
    d_category_id=models.ForeignKey(LCategory,on_delete=models.CASCADE)



    def __str__(self):  #Magic Function
        return self.d_title
    
    def save(self, *args,**kwargs):
        self.d_slug=slugify(self.d_title) #Creating the Slug based on Title
        return super().save(*args,**kwargs)

class aboutusdb(models.Model):
    content=models.TextField()  
