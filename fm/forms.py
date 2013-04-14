# -*- coding: utf-8 -*-
from django import forms
from datetime import date


class DocumentForm(forms.Form):
    doc_name = forms.CharField(max_length=200, label='Document Name')
    doc_description = forms.CharField(max_length=200, label='Document Description', widget=forms.Textarea)
    doc_date_created = forms.CharField(label='Document Created On')
    docfile = forms.FileField(label='Select a file')
