from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from puzzlesocweb.puzzlehunt.models import Document
from puzzlesocweb.puzzlehunt.models import DocumentType

def document_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'document_upload.html', {
        'form': form
    })

