# coding=windows-1251
"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import AnketaForm 

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'�������� ��������',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'��������',
            'message':'���� �������� ���������.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'� ���������',
            'message':'�������� � ��������� ������ ����������.',
            'year':datetime.now().year,
        }
    )
def anketa(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': '�������', '2': '�������', '3': '������'}
    evaluation = {'1': '1', '2': '2', '3': '3','4': '4', '5': '5'}
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['username'] = form.cleaned_data['username']
            data['gender'] = gender[form.cleaned_data['gender']]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = '��'
            else: 
                  data['notice'] = '���'
            data['email'] = form.cleaned_data['email'] 
            data['suggestion'] = form.cleaned_data['suggestion'] 
            form = None
    else:
        form = AnketaForm()
    return render(
        request,
        'app/anketa.html',
        {
            'form':form,
            'data': data
        }
        )