from django.contrib import admin
from .models import *
# Register your models here.

# Customize the Image_Category admin interface
class ImageCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the list view
    search_fields = ('name',)  # Add a search bar for the name field

# Customize the Gallery admin interface
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'category')  # Display image and category fields in the list view
    list_filter = ('category',)  # Add filtering by category
    search_fields = ('category__name',)  # Add a search bar for the category name

# Register the models with the admin interface
admin.site.register(Image_Category, ImageCategoryAdmin)
admin.site.register(Gallery, GalleryAdmin)

admin.site.register(HeroSection)
admin.site.register(HostelRommCard)
admin.site.register(Testimonial)
admin.site.register(Contact)