import logging

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from files.forms import UploadForm
from files.models import File
from files.tables import FileTable


logger = logging.getLogger(__name__)


def index_view(request):
    files = File.objects.all()
    file_table = FileTable(files)
    upload_form = UploadForm()

    return render(request, 'files/index.html', {
        'files': files,
        'file_table': file_table,
        'upload_form': upload_form,
    })


@require_http_methods(["POST"])
def upload_view(request):
    upload_form = UploadForm(data=request.POST, files=request.FILES)

    if upload_form.is_valid():
        upload_form.save(commit=True)
    else:
        logger.warning("Something went wrong with uploading the file.")
        logger.warning(request.POST)
        logger.warning(request.FILES)

    return redirect('files-index')
