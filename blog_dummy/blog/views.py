from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import Http404, HttpResponse
from blog.models import LPost,aboutusdb
from django.core.paginator import Paginator
from .forms import contactform
import logging

# Create your views here.
#static data
# post_title=[
#         {'id':1,'title':"Title 1",'content':"Content for post 1"},
#         {'id':2,'title':"Title 2",'content':"Content for post 2"},
#         {'id':3,'title':"Title 3",'content':"Content for post 3"},
#         {'id':4,'title':"Title 4",'content':"Content for post 4"}
#     ]
def index(request):

    blog_title="Latest Post"
    post_title =LPost.objects.all()
    paginator=Paginator(post_title,5) 
    page_number=request.GET.get('page') #Brings the current page number
    page_obj=paginator.get_page(page_number)
    return render(request,'blog/index.html',{'blog_title':blog_title,'post_title':page_obj})

def detail(request,path_id):
    try:
        post=LPost.objects.get(d_slug=path_id)
        related_post=LPost.objects.filter(d_category_id=post.d_category_id).exclude(pk=post.id)
    except LPost.DoesNotExist:
        raise Http404("post does not exist !")
    return render(request,'blog/detail.html',{'post':post,'related_post':related_post})


def aboutus(request):
    content=aboutusdb.objects.first().content
    return render(request,'blog/aboutus.html',{'content':content})

def oldUrl(request):
    return redirect(reverse('blog:newurl'))

def newUrl(request):
    return HttpResponse("this is the new URL")

def contact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        logger = logging.getLogger("Testing")
        if form.is_valid():
            logger.debug(f'post data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            success_message="Form submitted succesfully!!!"
            return render(request,'blog/contact.html',{'form':form,'name':name,'email':email,'message':message,'success_msg':success_message})
        else:
            logger.debug('Form validation failed')
            return render(request,'blog/contact.html',{'form':form,'name':name,'email':email,'message':message})
    return render(request,'blog/contact.html') # get return
