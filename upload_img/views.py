from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageFileUploadForm

# Create your views here.

def image_upload_method(request):
    if request.method == "POST":
        form = ImageFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'error':False, 'message': 'Uploaded Successfully.'})
        else:
            return JsonResponse({'error':True, 'errors': form.errors})
    else:
        form = ImageFileUploadForm()
        return render(request, 'upload_ui.html', {'form': form})