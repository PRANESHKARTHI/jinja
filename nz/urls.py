from django.urls import path
from nz.views import *
app_name="anything"
urlpatterns=[
    path("data_render_nz/",data_render_nz,name="data_render_nz"),
]