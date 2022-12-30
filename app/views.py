from django.shortcuts import render

# Create your views here.

def filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'fIne WhaT aBout U','dt':dt,'c':1}
    return render(request,'filters.html',d)

def usdf(request):
    d={'data':'HI Python HoW R yoU'}
    return render(request,'usdf.html',d)