from django import forms
from .models import Barang

class PostForm(forms.ModelForm):

   class Meta:
       model = Barang
       fields = ('nama', 'gambar','harga',)
