# coding=windows-1251
"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='���� ���', min_length=2, max_length= 50)
    username = forms.CharField(label='��� ������������', min_length=2, max_length= 50)
    gender = forms.ChoiceField(label='��� ���', choices=[('1', '�������'),('2', '�������'),('3', '������')], 
                            widget=forms.RadioSelect, initial=1)
    interests = forms.MultipleChoiceField(label='��� �� �������������', choices=[('1', '����'), ('2', '�������'), 
                                                                       ('3', '������������'), ('4', '�����'), 
                                                                       ('5', '�������'), ('6', '�����'), 
                                                                       ('7', '������')], 
                            widget=forms.CheckboxSelectMultiple())
    evaluation = forms.ChoiceField(label='������� ������ ����� �� ����� �� 1 �� 5', choices=[('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')], 
                            widget=forms.RadioSelect, initial=1)
    notice = forms.BooleanField(label='�������� ������� � ����� �� e-mail?', 
                                required=False)
    email = forms.EmailField(label='��� e-mail',min_length=8)
    suggestion = forms.CharField(label='������ � ���������', widget=forms.Textarea(attrs={'row':12, 'cols':20}))
    
    
    