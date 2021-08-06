from django.urls import path
from . import views

app_name= 'logins'

urlpatterns = [
    path('',views.index,name='index'),
path('helper_signup/',views.helper_signup,name='h_signup'),
path('helper_signin/',views.helper_signin,name='h_signin'),
path('customer_signup/',views.customer_signup,name='c_signup'),
path('customer_signin/',views.customer_signin,name='c_signin'),
#path('customer_work/',views.cust_work,name='c_work'),
path('add/',views.add,name='h_add'),
path('add_cus/',views.add_cus,name='c_add'),
path('check_customer/',views.check_cus,name='c_check'),
path('check_helper/',views.check_hel,name='h_check'),
path('customer_done/',views.after_cus,name='c_after'),
path('helper_done/',views.after_hel,name='h_after'),
path('done_cus/',views.done_cus,name='done_cus'),




]