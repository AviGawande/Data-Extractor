from django.contrib import admin
from . models import ImageFile,PDFFile 

# Register your models here.
admin.site.register(ImageFile)
admin.site.register(PDFFile)