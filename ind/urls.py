from ind.views import *
from django.urls import path
app_name="some_thing"

urlpatterns=[
    path("data_render_ind/",data_render_ind,name="data_render_ind"),
]   