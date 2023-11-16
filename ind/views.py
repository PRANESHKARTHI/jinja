from django.shortcuts import render

# Create your views here.
def data_render_ind(request):
    d={"country": "India" , "captain": "Mahindra Singh Dhoni"}
    return render(request,"data_render_ind.html",context=d)
