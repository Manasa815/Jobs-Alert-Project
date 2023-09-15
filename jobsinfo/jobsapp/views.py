from django.shortcuts import render
from jobsapp.models import HydJobs,BangloreJobs,PuneJobs
def home_view(request):
    return render(request,'jobsapp/index.html')
def hyd_view(request):
    jobs_list=HydJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/hyd.html',context=my_dict)
def Banglore_view(request):
    jobs_list=BangloreJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/banglore.html',context=my_dict)
def pune_view(request):
    jobs_list=PuneJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/pune.html',context=my_dict)