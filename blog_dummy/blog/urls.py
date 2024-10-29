from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path("",views.index,name="index"),
    path("post/<str:path_id>",views.detail,name="detail"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("oldUrlpage",views.oldUrl,name="oldurl"),
    path("newUrl",views.newUrl,name="newurl"),
    path("contact",views.contact,name="contact")
    
]
