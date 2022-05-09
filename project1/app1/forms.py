from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


        labels = {
            'bid':'Book Id',
            'bname':'Book Name',
            'author': 'Author Name',
            'price': 'Book Price',
            'Qty': 'Book Qty'
        }

        widgets ={
            'bid': forms.NumberInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Enter Student ID',
            })
        }