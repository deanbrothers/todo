from django.shortcuts import render
from django.views.generic import View
from workplan.models import *
from django.contrib.auth import authenticate
import datetime
# Create your views here.
class Index(View):
    template_name="index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())
    def post(self, request, *args, **kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        print(username, password, user)
        if user is not None:
            template_name="workplan.html"
            workobjs=Todo.objects.all()
        else:
            template_name="index.html"	
        today_date=datetime.datetime.now().date
        return render(request, template_name, locals())

class Workplan(View):
    def post(self, request, *args, **kwargs):
        name=request.POST.get('name')
        description=request.POST.get('description')
        priority=request.POST.get('priority')
        status=request.POST.get('status')
        date=request.POST.get('date')
        workid=request.POST.get('workid')
        try:
            work_obj=Todo.objects.get(id=workid)
        except:
            work_obj=Todo()
        work_obj.name=name
        work_obj.description=description
        work_obj.priority=priority
        work_obj.task_status=status
        work_obj.due_date=date
        work_obj.save()
        workobjs=Todo.objects.all()
        template_name="workplan.html"
        return render(request, template_name, locals())
