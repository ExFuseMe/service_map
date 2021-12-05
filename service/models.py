from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, PositiveSmallIntegerField, SlugField, TimeField, URLField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class UniquePoint(models.Model):
    image = ImageField(upload_to = "unique_points/")
class TypeOfCompany(models.Model):
    name = CharField(max_length=40)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Вид услуг'
        verbose_name_plural = 'Виды услуг'
        
class CarService(models.Model):
    position = CharField(max_length=15)
    name = CharField(max_length=40)
    type_of_company = ForeignKey(TypeOfCompany, on_delete=CASCADE)
    working_start = TimeField()
    working_end = TimeField()
    images = ImageField(upload_to = "imgs/")
    unique_point = ForeignKey(UniquePoint, on_delete=CASCADE)
    Website = URLField(unique=True, max_length=200, null=True)
    def __str__(self):
        return self.name

class RatingStar(models.Model):
    value = PositiveSmallIntegerField(default=1)
    class Meta:
        verbose_name = 'Звезды рейтинга'

class Rating(models.Model):
    ip = CharField(max_length=15)
    star = ForeignKey(RatingStar, on_delete=CASCADE)
    car_service = ForeignKey(CarService, on_delete=CASCADE)
    def __str__(self):
        return f"{self.star}-{self.car_service}"
    class Meta:
        verbose_name = 'Рейтинг'