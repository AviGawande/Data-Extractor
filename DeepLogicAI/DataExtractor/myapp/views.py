# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import ImageFile
# from .models import PDFFile
# from PIL import Image
# import numpy as np
# from io import StringIO

# def myapp(request):
#     return render(request, 'home.html')

# def images(request):
#     if request.method == 'POST':
#         image_file = request.FILES.get('imageInput')  # Get the uploaded file from request.FILES
#         if image_file:
#             ImageFile.objects.create(file=image_file)
#             # Generate CSV file from image here
#             img = Image.open(image_file)
#             arr = np.asarray(img)
#             lst = []
#             for row in arr:
#                 tmp = []
#                 for col in row:
#                     tmp.append(','.join(map(str, col)))
#                 lst.append(tmp)
#             csv_data = StringIO()
#             with csv_data as f:
#                 for row in lst:
#                     f.write(','.join(row) + '\n')
#             response = HttpResponse(csv_data.getvalue(), content_type='text/csv')
#             response['Content-Disposition'] = 'attachment; filename="image_data.csv"'
#             return render(request, 'image_download.html', {'csv_url': response})
#     return render(request, 'images.html')

# def documents(request):
#     if request.method == 'POST':
#         pdf_file = request.FILES.get('pdfInput')  # Get the uploaded file from request.FILES
#         if pdf_file:
#             PDFFile.objects.create(file=pdf_file)
#             return redirect('documents')  
#     return render(request, 'documents.html')

# def generate_csv_from_image(request):
#     if request.method == 'POST':
#         # Assuming the input field in the form is named 'imageInput'
#         image_file = request.FILES.get('imageInput')
#         if image_file:
#             img = Image.open(image_file)
#             arr = np.asarray(img)
            
#             # Convert 3D array to 2D list of lists
#             lst = []
#             for row in arr:
#                 tmp = []
#                 for col in row:
#                     tmp.append(','.join(map(str, col)))
#                 lst.append(tmp)
            
#             # Generate CSV file
#             csv_data = StringIO()
#             with csv_data as f:
#                 for row in lst:
#                     f.write(','.join(row) + '\n')
            
#             response = HttpResponse(csv_data.getvalue(), content_type='text/csv')
#             response['Content-Disposition'] = 'attachment; filename="image_data.csv"'
            
#             # Redirect to image_download.html for downloading the result
#             return render(request, 'download-pdf-csv', {'csv_url': response})
    
#     return HttpResponse("Error: No image file provided.")


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ImageFile
from PIL import Image
import numpy as np
from io import StringIO

def myapp(request):
    return render(request, 'home.html')

def images(request):
    if request.method == 'POST':
        image_file = request.FILES.get('imageInput')  # Get the uploaded file from request.FILES
        if image_file:
            ImageFile.objects.create(file=image_file)
            return redirect('generate_csv_from_image')  # Redirect to generate CSV
    return render(request, 'images.html')

def documents(request):
    if request.method == 'POST':
        pdf_file = request.FILES.get('pdfInput')  # Get the uploaded file from request.FILES
        if pdf_file:
            PDFFile.objects.create(file=pdf_file)
            return redirect('documents')  
    return render(request, 'documents.html')

def generate_csv_from_image(request):
    if request.method == 'GET':
        # Retrieve the last uploaded image
        last_image = ImageFile.objects.last()
        if last_image:
            img = Image.open(last_image.file)
            arr = np.asarray(img)
            lst = []
            for row in arr:
                tmp = []
                for col in row:
                    tmp.append(','.join(map(str, col)))
                lst.append(tmp)
            csv_data = StringIO()
            with csv_data as f:
                for row in lst:
                    f.write(','.join(row) + '\n')
            response = HttpResponse(csv_data.getvalue(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="image_data.csv"'
            return response
    return HttpResponse("No image data available to generate CSV.")
