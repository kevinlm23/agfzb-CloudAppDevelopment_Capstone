from django.contrib import admin
from .models import CarModel, CarMake


# Register your models here.

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'car_type', 'year', 'dealer_id')
    list_filter = ('car_make', 'car_type', 'year')
    search_fields = ('name', 'car_make__name', 'dealer_id')

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [CarModelInline]


# Register models here
