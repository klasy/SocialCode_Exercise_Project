from filetransfers.api import prepare_upload
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from .models import UploadModel
from .forms import UploadForm

import subprocess

# Create your views here.

def upload_handler(request):
    view_url = reverse('image_recognition.views.upload_handler')
    recognized = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            instance = UploadModel(file=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect(view_url)

    files = UploadModel.objects.all()
    if files:
        last = UploadModel.objects.latest('file')
        file_path = settings.MEDIA_ROOT + last.file.name
        recognized = subprocess.check_output(["/usr/bin/gocr", file_path])

    files.delete()

    upload_url, upload_data = prepare_upload(request, view_url)
    form = UploadForm()
    return render_to_response(
            'image_recognition/upload.html',
            {'form': form, 'upload_url': upload_url,
             'upload_data': upload_data, 'recognized': recognized},
            context_instance=RequestContext(request)
    )
