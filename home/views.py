from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Barang
from .forms import PostForm

# Create your views here.
def home(request):
    mybarang = Barang.objects.all()
    return render(request, 'home/daftar_home.html',{'mybarang':mybarang})

def input_barang(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_home')
    else:
        form = PostForm()
    return render(request, 'home/post_new.html', {'form':form})

# def blog_detail(request, blog_id):
#     blogging = Blog.objects.get(pk=blog_id)
#     return render(request, 'blog/blog_detail.html', {'b':blogging})