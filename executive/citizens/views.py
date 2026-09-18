import smtplib
from datetime import datetime
from django.shortcuts import render, redirect
from citizens.models import UserLogin

from citizens.models import hospital, stock, worker, assignedarea, citizen,vaccinationrequest, childInfo, vaccinationdetail, vaccinecollection, notification, dosagedetails
from django.urls import reverse


# Create your views here.




def logcheck(request):
    if request.method=="POST":
        username=request.POST.get('t1')
        password = request.POST.get('t2')
        count=UserLogin.objects.filter(username=username).count()
        if count>=1:
            udata=UserLogin.objects.get(username=username)
            request.session['username'] = username
            upass=udata.password
            utype=udata.user_type
            if upass==password:
                if utype=='executive':
                    return render(request,'executive_home.html')
                if utype=='citizens':
                    return render(request,'citizens_home.html')
                if utype == 'worker':
                    return render(request, 'worker_home.html')

            else:
                return render(request,'login.html',{'msg':'invalid password'})
        else:
            return render(request, 'login.html', {'msg': 'invalid username'})

    return render(request,'login.html')

def showworkerhome(request):
    return render(request, 'worker_home.html')

def showexecutivehome(request):
    return render(request, 'executive_home.html')

def showcitizenshome(request):
    return render(request, 'citizens_home.html')



def changepassword(request):
    uname=request.session['username']
    if request.method == 'POST':
        currentpass = request.POST.get('t1', '')
        newpass = request.POST.get('t2', '')
        confirmpass = request.POST.get('t3', '')

        ucheck = UserLogin.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and currentpass == p:
                if newpass == confirmpass:
                    UserLogin.objects.filter(username=uname).update(password=newpass)
                    base_url=reverse('logcheck')
                    msg='password has been changed successfully'
                    return redirect(base_url,msg=msg)
                else:
                    return render(request, 'changepassword.html',{'msg': 'both the usename and password are incorrect'})
            else:
                return render(request, 'changepassword.html',{'msg': 'invalid username'})
    return render(request, 'changepassword.html')


#forgot password function
def forgot(request):
    if request.method=="POST":
        email = request.POST.get('t1')
        user = UserLogin.objects.get(username=email)
        password=user.password
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('mathew011arnold@gmail.com', 'epdr olgc cmvn dcat')
        mail.sendmail('mathew011arnold@gmail.com', email, password)
        mail.close()

    return render(request, "forgot.html")



def showindex(request):
    return render(request, "index.html")


def About(request):
    return render(request, "about.html")


def Contact(request):
    return render(request, "contact.html")


def inserthosp(request):
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        hospital.objects.create(hosp_id=s1,name=s2,city=s3,address=s4,contact=s5)
        p = hospital.objects.all().order_by('id').last()
        pid = int(p.hosp_id) + 1
        return render(request,"hospitalinfo.html",{'pid':pid})
    p = hospital.objects.all().order_by('id').last()
    pid = int(p.hosp_id) + 1
    return render(request, "hospitalinfo.html",{'pid':pid})

def showhospital(request):
    userdict=hospital.objects.all()
    return render(request,"viewhospital.html",{'userdict':userdict})

def hospital_del(request,pk):
    id=hospital.objects.get(id=pk)
    id.delete()
    userdict=hospital.objects.all()
    return render(request,'viewhospital.html',{'userdict':userdict})



def insertstock(request):
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        stock.objects.create(stock_id=s1,vaccine_name=s2,quantity=s3,last_updated=s4,hosp_id=s5)
        p = stock.objects.all().order_by('id').last()
        pid = int(p.stock_id) + 1
        return render(request,"stockinfo.html",{'pid':pid})
    p = stock.objects.all().order_by('id').last()
    pid = int(p.stock_id) + 1
    return render(request, "stockinfo.html",{'pid':pid})

def showstock(request):
    userdict=stock.objects.all()
    return render(request,"viewstock.html",{'userdict':userdict})

def stock_del(request,pk):
    id=stock.objects.get(id=pk)
    id.delete()
    userdict=stock.objects.all()
    return render(request,'viewstock.html',{'userdict':userdict})

def stock_update(request, pk):
    stock_obj = stock.objects.get(id=pk)
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        # Update the stock with new quantity and today's date
        stock.objects.filter(id=pk).update(
            quantity=quantity,
            last_updated=datetime.now().strftime('%Y-%m-%d')
        )
        return redirect('showstock')
    return render(request, 'updatestock.html', {'stock': stock_obj})



def insertworker(request):
    userdict = worker.objects.all()
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        s7 = request.POST.get('t7')
        worker.objects.create(worker_id=s1,name=s2,experience=s3,email=s4,mobile_no=s5,gender=s6,hosp_id=s7)
        p = worker.objects.all().order_by('id').last()
        pid = int(p.worker_id) + 1
        userdict = worker.objects.all()
        return render(request,"workerinfo.html",{'pid':pid,'userdict':userdict})
    p = worker.objects.all().order_by('id').last()
    pid = int(p.worker_id) + 1
    return render(request, "workerinfo.html",{'pid':pid,'userdict':userdict})

def showworker(request):
    userdict=worker.objects.all()
    return render(request,"viewworker.html",{'userdict':userdict})

def worker_del(request,pk):
    id=worker.objects.get(id=pk)
    id.delete()
    userdict=worker.objects.all()
    return render(request,'viewworker.html',{'userdict':userdict})



def insertassignedarea(request):
    userdict = worker.objects.all()
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        assignedarea.objects.create(area_id=s1,area_name=s2,worker_id=s3,from_date=s4,till_date=s5)
        p = assignedarea.objects.all().order_by('id').last()
        pid = int(p.area_id) + 1
        return render(request,"assignedareainfo.html",{'pid':pid})
    p = assignedarea.objects.all().order_by('id').last()
    pid = int(p.area_id) + 1
    return render(request, "assignedareainfo.html",{'pid':pid,'userdict':userdict})

def showassignedarea(request):
    userdict=assignedarea.objects.all()
    return render(request,"viewassignedarea.html",{'userdict':userdict})

def assignedarea_del(request,pk):
    id=assignedarea.objects.get(id=pk)
    id.delete()
    userdict=assignedarea.objects.all()
    return render(request,'viewassignedarea.html',{'userdict':userdict})



def insertcitizen(request):
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        s7 = request.POST.get('t7')
        citizen.objects.create(citizen_id=s1,name=s2,address=s3,contact_no=s4,city=s5,mail=s6)
        UserLogin.objects.create(username=s6,password=s7,user_type='citizens')
        p = citizen.objects.all().order_by('id').last()
        pid = int(p.citizen_id) + 1
        return redirect('logcheck')

    p = citizen.objects.all().order_by('id').last()
    pid = int(p.citizen_id) + 1
    return render(request, "citizeninfo.html",{'pid':pid})

def showcitizen(request):
    userdict=citizen.objects.all()
    return render(request,"viewcitizen.html",{'userdict':userdict})

def citizen_del(request,pk):
    id=citizen.objects.get(id=pk)
    id.delete()
    userdict=citizen.objects.all()
    return render(request,'viewcitizen.html',{'userdict':userdict})



def insertvaccinationrequest(request):
    uname = request.session['username']
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        vaccinationrequest.objects.create(request_id=s1,citizen_id=s2,citizen_name=s3,requested_date=s4,status=s5)
        p = vaccinationrequest.objects.all().order_by('id').last()
        pid = int(p.request_id) + 1
        return render(request,"vaccinationrequestinfo.html",{'pid':pid,'uname':uname})

    today_date = datetime.now().strftime('%Y-%m-%d')
    p = vaccinationrequest.objects.all().order_by('id').last()
    pid = int(p.request_id) + 1
    return render(request, "vaccinationrequestinfo.html",{'pid':pid,'uname':uname,'today_date': today_date})


def showvaccinationrequest(request):
    userdict=vaccinationrequest.objects.all()
    return render(request,"viewvaccinationrequest.html",{'userdict':userdict})

def vaccinationrequest_del(request,pk):
    id=vaccinationrequest.objects.get(id=pk)
    id.delete()
    userdict=vaccinationrequest.objects.all()
    return render(request,'viewvaccinationrequest.html',{'userdict':userdict})




def insertchild(request):
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        childInfo.objects.create(child_id=s1,name=s2,age=s3,parent_contact=s4,location=s5,vaccine_status=s6)
        p = childInfo.objects.all().order_by('id').last()
        pid = int(p.child_id) + 1
        return render(request,"childinfo.html",{'pid':pid})
    p = childInfo.objects.all().order_by('id').last()
    pid = int(p.child_id) + 1
    return render(request, "childinfo.html",{'pid':pid})

def showchildInfo(request):
    userdict=childInfo.objects.all()
    return render(request,"viewchildInfo.html",{'userdict':userdict})

def child_del(request,pk):
    id=childInfo.objects.get(id=pk)
    id.delete()
    userdict=childInfo.objects.all()
    return render(request,'viewchildInfo.html',{'userdict':userdict})




def insertvaccinationdetail(request):
    uname = request.session['username']
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        vaccinationdetail.objects.create(record_id=s1,vaccine_name=s2,dose_num=s3,vaccination_date=s4,given_by=s5)
        p = vaccinationdetail.objects.all().order_by('id').last()
        pid = int(p.record_id) + 1
        return render(request,"vaccinationdetailinfo.html",{'pid':pid,'uname':uname})
    p = vaccinationdetail.objects.all().order_by('id').last()
    pid = int(p.record_id) + 1
    return render(request, "vaccinationdetailinfo.html",{'pid':pid,'uname':uname})

def showvaccinationdetail(request):
    userdict=vaccinationdetail.objects.all()
    return render(request,"viewvaccinationdetail.html",{'userdict':userdict})

def vaccinationdetail_del(request,pk):
    id=vaccinationdetail.objects.get(id=pk)
    id.delete()
    userdict=vaccinationdetail.objects.all()
    return render(request,'viewvaccinationdetail.html',{'userdict':userdict})




def insertcollection(request):
    uname = request.session['username']
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        vaccinecollection.objects.create(collection_id=s1,worker_id=s2,vaccine_name=s3,hosp_id=s4,quantity=s5,collection_date=s6)
        p = vaccinecollection.objects.all().order_by('id').last()
        pid = int(p.collection_id) + 1
        return render(request,"vaccinecollectioninfo.html",{'pid':pid,'uname':uname})
    p = vaccinecollection.objects.all().order_by('id').last()
    pid = int(p.collection_id) + 1
    return render(request, "vaccinecollectioninfo.html",{'pid':pid,'uname':uname})

def showvaccinecollection(request):
    userdict=vaccinecollection.objects.all()
    return render(request,"viewvaccinecollection.html",{'userdict':userdict})

def vaccinecollection_del(request,pk):
    id=vaccinecollection.objects.get(id=pk)
    id.delete()
    userdict=vaccinecollection.objects.all()
    return render(request,'viewvaccinecollection.html',{'userdict':userdict})




def insertnotification(request):
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        notification.objects.create(vaccination=s1,start_end_date=s2,start_end_time=s3,location=s4,city=s5,contact_no=s6)
        return render(request,"notificationinfo.html")
    today_date = datetime.now().strftime('%Y-%m-%d')
    return render(request, "notificationinfo.html", {'today_date': today_date})

def shownotification(request):
    userdict=notification.objects.all()
    return render(request,"viewnotification.html",{'userdict':userdict})

def notification_del(request,pk):
    id=notification.objects.get(id=pk)
    id.delete()
    userdict=notification.objects.all()
    return render(request,'viewnotification.html',{'userdict':userdict})




def insertdosagedetails(request):
    uname = request.session['username']
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        dosagedetails.objects.create(dose_id=s1,citizen_id=s2,vaccine_name=s3,dose_num=s4,vaccination_date=s5,given_by=s6)
        p = dosagedetails.objects.all().order_by('id').last()
        pid = int(p.dose_id) + 1
        return render(request,"dosagedetailsinfo.html",{'pid':pid,'uname':uname})
    p = dosagedetails.objects.all().order_by('id').last()
    pid = int(p.dose_id) + 1
    today_date = datetime.now().strftime('%Y-%m-%d')
    return render(request, "dosagedetailsinfo.html",{'pid':pid,'uname':uname, 'today_date': today_date})

def showdosagedetails(request):
    userdict=dosagedetails.objects.all()
    return render(request,"viewdosagedetails.html",{'userdict':userdict})

def showdosedetails(request):
    userdict=dosagedetails.objects.all()
    return render(request,"viewdose.html",{'userdict':userdict})

def dosagedetails_del(request,pk):
    id=dosagedetails.objects.get(id=pk)
    id.delete()
    userdict=dosagedetails.objects.all()
    return render(request,'viewdosagedetails.html',{'userdict':userdict})