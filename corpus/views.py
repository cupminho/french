from django.shortcuts import render, get_object_or_404

# Create your views here.
from corpus.models import File, Sentence
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.shortcuts import render
from .forms import UploadFileForm

import logging
import ast


class IndexView(generic.ListView):
    template_name = 'corpus/index.html'
    context_object_name = 'file_list'

    def get_queryset(self):
        return File.objects.order_by('id')

class DetailView(generic.DetailView):
    model = File
    template_name = 'corpus/detail.html'


class TaggingView(generic.DetailView):
    model = Sentence
    template_name = 'corpus/tagging.html'

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect(reverse('corpus:index'))
    else:
        form = UploadFileForm()
    return render(request, 'corpus/index.html', {'form': form})