from django.db import models
from datetime import date
# Create your models here.
import json

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import timedelta
from django.utils.translation import ugettext_lazy as _

from dateutil import rrule
from django_libs.models import ColorField
from filer.fields.image import FilerImageField
from datetime import date, timedelta as td
from .utils import OccurrenceReplacer
from datetime import datetime
from django.utils.timezone import datetime, now, timedelta, utc


class Todo(models.Model):
    """TODO MODEL"""
    PRIORITY=(
         (1, 'High'),
         (2, 'Medium'),
         (3, 'Low'),
        )
    TASK_STATUS=(
         (1, 'Todo'),
         (2, 'Doing'),
         (3, 'Done'),
        )
    name=models.CharField(max_length=100, help_text="Name of todo")
    description=models.CharField(max_length=200, help_text="description of todo")
    priority=models.IntegerField(choices=PRIORITY, default=2, help_text="Priority")
    task_status=models.IntegerField(choices=TASK_STATUS, default=1)
    due_date=models.DateField()
    start_date=models.DateField()
    def is_due(self):
        return date.today() > self.due_date
    def get_duration(self):
        holiday=Holiday.objects.all().values_list('hdate', flat=True) 
        s_date=self.start_date
        i=0		
        total_days=(self.due_date-self.start_date).days
        for i in range(total_days + 1):
            da=s_date + td(days=i)
            current = False
            if da:
                date = datetime(year=da.year, month=da.month, day=da.day,
                                tzinfo=utc)
                days=date.weekday()
                tdate=date
                if tdate.date() in holiday or days > 4 :
                    pass
                else:
                    i=i+1
                if tdate.date() in holiday and days > 4:
                    pass
        total_days=i*8
        return total_days

class Holiday(models.Model):
	"""HOLIDAY"""
	hdate=models.DateField()
