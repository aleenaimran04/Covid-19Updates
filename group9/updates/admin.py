from django.contrib import admin
from .models import Complaintform
from .models import registrationform
from .models import groupmembers
# Register your models here.

admin.site.register(groupmembers)
admin.site.register(Complaintform)
admin.site.register(registrationform)