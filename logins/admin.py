from django.contrib import admin
from .models import real_work,Helper_Signup,works_by_helpers,Customer_Signup
# Register your models here.
admin.site.register(real_work)
admin.site.register(Helper_Signup)
admin.site.register(works_by_helpers)
admin.site.register(Customer_Signup)