from django.db import models

# Create your models here.

class Article(models.Model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    image=models.ImageField(default='null')
    public= models.BooleanField()
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f" {self.id} Titulo :{self.title } creado el {self.created_at} contenido : {self.content}"

class Category(models.Model):
    name= models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    crated_at=models.DateField()