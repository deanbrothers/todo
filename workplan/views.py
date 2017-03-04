from django.shortcuts import render
from django.views.generic import View
from workplan.models import *
from django.contrib.auth import authenticate
import datetime
# Create your views here.
"""Views for the ``calendarium`` app."""
import calendar
from dateutil.relativedelta import relativedelta

from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.utils.decorators import method_decorator
from django.utils.timezone import datetime, now, timedelta, utc
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from .utils import monday_of_week

SHIFT_WEEKSTART = getattr(settings, 'CALENDARIUM_SHIFT_WEEKSTART', 0)



class CalendariumRedirectView(RedirectView):
    """View to redirect to the current month view."""
    permanent = False

    def get_redirect_url(self, **kwargs):
        return reverse('calendar_month', kwargs={'year': now().year,
                                                 'month': now().month})


class MonthView(TemplateView):
    """month view"""
    template_name = 'calendar_month.html'

    def dispatch(self, request, *args, **kwargs):
        self.month = int(kwargs.get('month'))
        self.year = int(kwargs.get('year'))
        print "hellow"
        if self.month not in range(1, 13):
            raise Http404
        if request.method == 'POST':
            if request.POST.get('next'):
                new_date = datetime(self.year, self.month, 1) + timedelta(
                    days=31)
                kwargs.update({'year': new_date.year, 'month': new_date.month})
                return HttpResponseRedirect(
                    reverse('calendar_month', kwargs=kwargs))
            elif request.POST.get('previous'):
                new_date = datetime(self.year, self.month, 1) - timedelta(
                    days=1)
                kwargs.update({'year': new_date.year, 'month': new_date.month})
                return HttpResponseRedirect(
                    reverse('calendar_month', kwargs=kwargs))
            elif request.POST.get('today'):
                kwargs.update({'year': now().year, 'month': now().month})
                return HttpResponseRedirect(
                    reverse('calendar_month', kwargs=kwargs))
        if request.is_ajax():
            self.template_name = 'partials/calendar_month.html'
        return super(MonthView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        firstweekday = 0 + SHIFT_WEEKSTART
        while firstweekday < 0:
            firstweekday += 7
        while firstweekday > 6:
            firstweekday -= 7

        ctx = {}
        month = [[]]
        week = 0
        start = datetime(year=self.year, month=self.month, day=1, tzinfo=utc)
        end = datetime(
            year=self.year, month=self.month, day=1, tzinfo=utc
        ) + relativedelta(months=1)

        cal = calendar.Calendar()
        holiday=Holiday.objects.all().values_list('hdate', flat=True) 
        cal.setfirstweekday(firstweekday)
        for day in cal.itermonthdays(self.year, self.month):
            current = False
            if day:
                date = datetime(year=self.year, month=self.month, day=day,
                                tzinfo=utc)
                days=date.weekday()
                tdate=date
                if date.date() == now().date():
                    current = True
                if tdate.date() in holiday or days > 4 :
                    hday=False
                else:
                    hday=True
                if tdate.date() in holiday and days > 4:
					print("I am")
					hday=True
                 
            else:
                days=''
                tdate=''
                hday=False
            month[week].append((day, current, days, tdate, hday))
            if len(month[week]) == 7:
                month.append([])
                week += 1
        calendar.setfirstweekday(firstweekday)
        weekdays = [_(header) for header in calendar.weekheader(10).split()]
        ctx.update({'month': month, 'date': date, 'weekdays': weekdays, 'holiday': holiday})
        return ctx




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
        today_date=datetime.now().date
        return render(request, template_name, locals())

class Workplan(View):
    def get(self, request, *args, **kwargs):
        template_name="workplan.html"
        workobjs=Todo.objects.all()
        return render(request, template_name, locals())
    def post(self, request, *args, **kwargs):
        name=request.POST.get('name')
        description=request.POST.get('description')
        priority=request.POST.get('priority')
        status=request.POST.get('status')
        enddate=request.POST.get('enddate')
        startdate=request.POST.get('startdate')
        workid=request.POST.get('workid')
        try:
            work_obj=Todo.objects.get(id=workid)
        except:
            work_obj=Todo()
        work_obj.name=name
        work_obj.description=description
        work_obj.priority=priority
        work_obj.task_status=status
        work_obj.due_date=enddate
        work_obj.start_date=startdate        
        work_obj.save()
        workobjs=Todo.objects.all()
        template_name="workplan.html"
        return render(request, template_name, locals())

def holiday(request):
    """Holiday"""
    if request.method == 'POST':
        date=request.POST.get('date')
        opt=request.POST.get('opt')
        print("hday", date, opt)
        if opt== '0':
            hl_obj=Holiday()
            hl_obj.hdate=date
            hl_obj.save()
        else:
			Holiday.objects.filter(hdate=date).delete()
        return HttpResponse('sucess')        
        

