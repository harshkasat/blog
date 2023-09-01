from django.shortcuts import render
from .models import Post,magic
# Create your views here.
def index(request):
   posts=Post.objects.all()
   magics=magic.objects.all()
   return render(request, 'index.html',{'posts':posts, 'magics':magics})
def post(request,pk):
   post=Post.objects.get(id=pk)
   return render(request,'post.html',{'post':post})