from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()
    status = models.BooleanField()
    featured = models.BooleanField()
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SizeGroup(models.Model):
    name = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50)
    sizegroup = models.ForeignKey(SizeGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField()
    image = models.URLField()
    veg = models.BooleanField()
    sizegroup = models.ForeignKey(SizeGroup, on_delete=models.CASCADE, )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Variant(models.Model):
    name = models.CharField(max_length=50)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.JSONField()
    tags=models.JSONField()
    default = models.BooleanField()
    image = models.URLField()
    cookingTime = models.TimeField()
    addOns = models.JSONField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name