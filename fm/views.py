from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from fm.models import Document
from django.template import RequestContext
from fm.forms import DocumentForm
from datetime import datetime
from django.forms.util import ErrorList
import os
from django.conf import settings


def index(request):
    """Will eventually contain search UI"""
    latest_document_list = Document.objects.order_by('date_created')[:10]
    return render_to_response('fm/list.html', {"latest_document_list": latest_document_list})


@login_required
def manage_document(request):
    """This method handles the logic of the file upload form"""
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid() and file_does_not_exist(request, form):
            new_doc = Document(document_file=request.FILES['docfile'],
                               name=request.FILES['docfile'].name,
                               content_type=request.FILES['docfile'].content_type,
                               description=request.POST['doc_description'],
                               date_created=request.POST['doc_date_created'],
                               date_uploaded=datetime.utcnow())
            new_doc.save()
            # todo, add a try catch for unique name violation
            return HttpResponseRedirect(reverse('filemanager:detail', args=(new_doc.id,)))
    else:
        form = DocumentForm()
    return render_to_response("fm/manage_document.html", {
        "form": form,
    },
        context_instance=RequestContext(request))


def file_does_not_exist(request, form):
    """Checks if a files with the same name exists, if so, creates an error.
    Not a safe way to handle it if there are concurrent users, but right now
    business requirements are a single user, so not a problem"""
    name_count = Document.objects.filter(name=request.FILES['docfile'].name).count()
    if name_count > 0:
        errors = form._errors.setdefault("docfile", ErrorList())
        errors.append(u"File with same name already exists")
        return False
    else:
        return True


def detail(request, document_id):
    """Returns document details and download link"""
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'fm/detail.html', {'document': document})


def download(request, document_id):
    """This method returns the file as an attachment"""
    document = get_object_or_404(Document, pk=document_id)
    filename = os.path.join(settings.MEDIA_ROOT, document.document_file.name)
    if not os.path.isfile(filename):
        raise Exception, "file " + filename + " not found."
    file_to_send = open(filename, 'rb')
    response = HttpResponse(read_in_chunks(file_to_send), mimetype=document.content_type)
    response["Content-Disposition"] = "attachment; filename=\"%s\"" % document.name
    return response


def read_in_chunks(file_object, chunk_size=65536):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 65536"""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data
