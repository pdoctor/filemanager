from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from fm.models import Document
from django.forms.models import modelform_factory, modelform_factory
from django.template import RequestContext
from fm.forms import DocumentForm
from datetime import datetime 

def index(request):
    return HttpResponse('index')

def list(request):
    latest_document_list = Document.objects.order_by('-date_uploaded')[:5]
    context = {'latest_document_list': latest_document_list}
    return render(request, 'fm/list.html', context)

def manage_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(document_file = request.FILES['docfile'],
                name = request.POST['doc_name'],
                description = request.POST['doc_description'],
                #date_created = datetime.strptime(request.POST['doc_date_created'], '%m/%d/%Y'),
                date_created = request.POST['doc_date_created'],
                date_uploaded = datetime.utcnow())
            newdoc.save()
            return HttpResponseRedirect(reverse('filemanager:detail', args=(new_document.id,)))
    else:
        form = DocumentForm()
    return render_to_response("fm/manage_document.html", {
        "form": form,
    },
    context_instance=RequestContext(request))



def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'fm/detail.html', {'document': document})

def results(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'fm/results.html', {'document': document})

