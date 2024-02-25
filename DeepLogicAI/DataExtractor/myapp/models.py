from django.db import models

# Create your models here.

class ImageFile(models.Model):
    file = models.ImageField(upload_to='images/')  # Field to store the image file

    def __str__(self):
        return self.file.name


class PDFFile(models.Model):
    file = models.FileField(upload_to='pdf_files/')  # Field to store the PDF file

    def __str__(self):
        return self.file.name
        
    
