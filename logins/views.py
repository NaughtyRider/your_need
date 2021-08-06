from .models import Customer_Signup, Helper_Signup , works_by_helpers , real_work
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("You are in hello Login")


def index(request):
    # return HttpResponse("You are in hello Login page")
    return render(request, 'logins/index.html')


def helper_signup(request):
    works = works_by_helpers.objects.order_by('-work')
    print('here: ', works)
    print("type: ",type(works))
    for x in works:
        print('here: ', x.work)
    lis = {
        'work_lis':works,
    }

    return render(request, 'logins/helper_signup.html',lis)


def helper_signin(request):
    return render(request, 'logins/helper_signin.html')



def customer_signup(request):
    return render(request, 'logins/customer_signup.html')


def customer_signin(request):
    return render(request, 'logins/customer_signin.html')


def cust_work(request,q_id):
    works = works_by_helpers.objects.order_by('-work')
    print('here: ', works)
    print("type: ", type(works))
    for x in works:
        print('here: ', x.work)
    lis = {
        'work_lis': works,
        'name':q_id,
    }
    return render(request,'logins/customer_work.html',lis )


def add(request):
    if(request.method) == 'POST':
        #works1 = works_by_helpers.objects.order_by('-work')

        helper = Helper_Signup()
        #works = works_by_helpers()

        helper.u_name = request.POST['hname']
        helper.u_email = request.POST['uemail']
        helper.u_password = request.POST['password']
        #wor_lis = [x.work for x in works1]
       # print(wor_lis)
        """ if request.POST['work'] not in wor_lis:
            works.work = request.POST['work']
            works.save()"""
        helper.save()
        lin = works_by_helpers.objects.only('id').get(work=request.POST['work']).id
        helper.u_work.add(lin)
    return render(request,'logins/done_log.html')

def add_cus(request):
    if request.method == 'POST':
        customer= Customer_Signup()
        customer.u_name = request.POST['cname']
        customer.u_email = request.POST['cemail']
        customer.u_password = request.POST['password']
        customer.save()
    return render(request, 'logins/done_log.html')


def check_cus(request):
    customer_email = Customer_Signup.objects.order_by('-u_email')
    if request.method =='POST':
        em = [x.u_email for x in customer_email]
        print(em)
        email = request.POST['email']
        print(request.POST['email'])
        if(request.POST['email'] in em ) and request.POST['password']==Customer_Signup.objects.only('u_password').get(u_email=request.POST['email']).u_password:
            c_name= Customer_Signup.objects.only('u_name').get(u_email=request.POST['email']).u_name
            a_cid= Customer_Signup.objects.only('Customer_id').get(u_name=c_name).Customer_id
            works = works_by_helpers.objects.order_by('-work')
            status = Customer_Signup.objects.only('w_status').get(u_email=request.POST['email']).w_status

            try:
                if (real_work.objects.only('status').get(cid=a_cid).status == True):
                    rel_hid = real_work.objects.only('hid').get(cid=a_cid).hid
                    ts = rel_hid.all()[0].u_name
                else:
                    ts=None
               # print("Here helper: test12 ", ts)
               # h_name = Helper_Signup.objects.only('u_name').get(Helper_id= ts).u_name
            except real_work.DoesNotExist:
                ts = None



            print('here: ', works)
            print("type: ", type(works))

            for x in works:
                print('here: ', x.work)
            lis = {
                'work_lis': works,
                'name': c_name,
                'status':status,
                'email':email,
                'rel_hid':ts,
            }
            return render(request, 'logins/customer_work.html', lis)
            #cust_work(request,c_name)
        else:
            print("Not present")
            return HttpResponse("No your thing is not present")
    #return render(request, 'logins/done_log.html')

def check_hel(request):
    helper_email = Helper_Signup.objects.order_by('-u_email')
    if request.method =='POST':
        em = [x.u_email for x in helper_email]
        if(request.POST['email'] in em ) and request.POST['password']==Helper_Signup.objects.only('u_password').get(u_email=request.POST['email']).u_password:
            h_name = Helper_Signup.objects.only('u_name').get(u_email=request.POST['email']).u_name
            a_hid = Helper_Signup.objects.only('Helper_id').get(u_name=h_name).Helper_id
            helper_det = Helper_Signup.objects.get(u_email=request.POST['email'])
            works = helper_det.u_work.all()
            print('work name: ', works)
            print('python workid: ',works," = ",id(works))
            print("Works 12:" , works[0].id)
            works=str(works)
            r_work=[]
            r_id=[]
            c=0
            for x in real_work.objects.all():
                y= str(x.wid.all())
                if (y == works) and (x.status==False):
                    c=1
                    r_work.append(x)
                    r_id.append(x.id)

            #status = [id(x.wid.all()) for x in real_work.objects.all() if (x.status==False  ) ]
            print(r_work)
            print(r_id)
            lis ={
                'h_name':h_name,
                'a_hid':a_hid,
                'r_work':r_work,
                'email':request.POST['email'],
                'r_id':r_id,
                'c':c,
                'stat':helper_det.cur_stat,
            }
            #demo of geting name from cid
          #  print("name : ",r_work[0].cid.values("u_name").first()['u_name'],type(r_work[0].cid.values("u_name").first()))
           # print(dir(r_work[0].cid.values("u_name")))

            return render(request,'logins/helper_work.html', lis)






        else:
            print("Not present")
            return HttpResponse("No your thing is not present")
    return render(request, 'logins/done_log.html')



def after_cus(request):
    if request.method =='POST':
        rwork = real_work()
        email = request.POST['wemail']
        cus_det = Customer_Signup.objects.get(u_email=email)
        cus_det.w_status = request.POST['wstatus']
        cus_det.save()
        rwork.save()# so that field'id' none error dont occur
        rwork.cid.add(Customer_Signup.objects.only('Customer_id').get(u_email=request.POST['wemail']).Customer_id)
       # rwork.cid.add(cus_det.Customer_id) both working
        print(rwork.cid)
        show_work = request.POST['work']# for getting work_id
        print(show_work)
        rwork.wid.add(works_by_helpers.objects.only('id').get(work=show_work).id)

        return render(request, 'logins/done_log.html')



def after_hel(request):
    if request.method =='POST':
        email = request.POST['wemail']
        cid = request.POST['work']

        print("cid: ", cid)
        rwork = real_work.objects.get(id=request.POST['work'])
        rwork.hid.add(Helper_Signup.objects.only('Helper_id').get(u_email=email).Helper_id)
        rwork.status=request.POST['wstatus']

        hel_det = Helper_Signup.objects.get(u_email=email)
        hel_det.cur_stat= True
        rwork.save()#save other wise things will revert
        hel_det.save()
        #rel_id= rwork.cid
        return render(request, 'logins/done_log.html')



def done_cus(request):
    if request.method == 'POST':

        email = request.POST['wemail']
        cus_det = Customer_Signup.objects.get(u_email=email)
        r_id_with_cus_id= real_work.objects.get(cid=cus_det.Customer_id)
        print("test : " , r_id_with_cus_id.hid)
        rel_hid= real_work.objects.only('hid').get(cid=cus_det.Customer_id).hid
        ts = rel_hid.all()[0].Helper_id
        r_hid_with_id = Helper_Signup.objects.get(Helper_id=ts )
        r_hid_with_id.total_success+=1
        r_hid_with_id.cur_stat = False
        r_hid_with_id.save()
        cus_det.w_status = 0
        cus_det.save()
        r_id_with_cus_id.delete()
        return render(request, 'logins/done_log.html')

