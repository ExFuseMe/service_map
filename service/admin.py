from django.contrib import admin

# Register your models here.
from service.models import Rating, RatingStar, TypeOfCompany, CarService, UniquePoint

admin.site.register(TypeOfCompany)
admin.site.register(CarService)
admin.site.register(UniquePoint)
admin.site.register(RatingStar)
admin.site.register(Rating)