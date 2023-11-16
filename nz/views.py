from django.shortcuts import render

# Create your views here.
def data_render_nz(request):
    d={"country": "New Zealand" , "captain": "Kane Williamson"}
    return render(request,"data_render_nz.html",context=d)