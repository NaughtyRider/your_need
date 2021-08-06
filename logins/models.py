from django.db import models



# Create your models here.


class Customer_Signup(models.Model):
    Customer_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=200,null=False)
    u_email = models.CharField(max_length= 200,unique=True)
    u_password = models.CharField(max_length= 200,null=False)
    w_status = models.IntegerField(default=0)

    def __str__(self):
        return "Name: %s Id: %s" % (self.u_name, self.Customer_id)


class works_by_helpers(models.Model):
    work = models.CharField(max_length=200)




class Helper_Signup(models.Model):
    Helper_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=200,null=False)
    u_email = models.CharField(max_length= 200,unique=True)
    u_password = models.CharField(max_length= 200)
    u_work =  models.ManyToManyField(works_by_helpers)
    cur_stat = models.BooleanField(default=False)
    total_success = models.IntegerField(default=0)

    def __str__(self):
        return "Name: %s \n Id: %s" % (self.u_name, self.Helper_id)

class real_work(models.Model):
    status = models.BooleanField(default=False)
    cid= models.ManyToManyField(Customer_Signup)
    hid = models.ManyToManyField(Helper_Signup)
    wid = models.ManyToManyField(works_by_helpers)





