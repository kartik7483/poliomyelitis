"""
URL configuration for executive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from citizens import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logcheck',views.logcheck,name='logcheck'),
    path('',views.showindex,name='showindex'),
    path('About',views.About,name='About'),
    path('Contact', views.Contact, name='Contact'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('forgot',views.forgot,name='forgot'),
    path('showworkerhome',views.showworkerhome,name='showworkerhome'),
    path('showcitizenshome',views.showcitizenshome,name='showcitizenshome'),
path('showexecutivehome',views.showexecutivehome,name='showexecutivehome'),

    path('showdosagedetails',views.showdosagedetails,name='showdosagedetails'),
    path('showdosedetails', views.showdosedetails, name='showdosedetails'),
    path('insertdosagedetails',views.insertdosagedetails,name='insertdosagedetails'),
    path('dosagedetails_del/(?P<pk>\d+)/$', views.dosagedetails_del, name='dosagedetails_del'),

    path('inserthosp',views.inserthosp,name='inserthosp'),
    path('insertstock',views.insertstock,name='insertstock'),
    path('insertworker',views.insertworker,name='insertworker'),
    path('insertassignedarea',views.insertassignedarea,name='insertassignedarea'),
    path('insertcitizen', views.insertcitizen, name='insertcitizen'),
    path('insertvaccinationrequest', views.insertvaccinationrequest, name='insertvaccinationrequest'),
    path('insertchild', views.insertchild, name='insertchild'),
    path('insertvaccinationdetail', views.insertvaccinationdetail, name='insertvaccinationdetail'),
    path('insertcollection', views.insertcollection, name='insertcollection'),
    path('insertnotification', views.insertnotification, name='insertnotification'),

    path('showhospital',views.showhospital,name='showhospital'),
    path('showstock',views.showstock,name='showstock'),
    path('showworker',views.showworker,name='showworker'),
    path('showassignedarea',views.showassignedarea,name='showassignedarea'),
    path('showcitizen',views.showcitizen,name='showcitizen'),
    path('showvaccinationrequest',views.showvaccinationrequest,name='showvaccinationrequest'),
    path('showchildInfo',views.showchildInfo,name='showchildInfo'),
    path('showvaccinationdetail',views.showvaccinationdetail,name='showvaccinationdetail'),
    path('showvaccinecollection',views.showvaccinecollection,name='showvaccinecollection'),
    path('shownotification', views.shownotification, name='shownotification'),

    path('hospital_del/(?P<pk>\d+)/$', views.hospital_del, name='hospital_del'),
    path('stock_del/(?P<pk>\d+)/$', views.stock_del, name='stock_del'),
    path('worker_del/(?P<pk>\d+)/$', views.worker_del, name='worker_del'),
    path('assignedarea_del/(?P<pk>\d+)/$', views.assignedarea_del, name='assignedarea_del'),
    path('citizen_del/(?P<pk>\d+)/$', views.citizen_del, name='citizen_del'),
    path('vaccinationrequest_del/(?P<pk>\d+)/$', views.vaccinationrequest_del, name='vaccinationrequest_del'),
    path('child_del/(?P<pk>\d+)/$', views.child_del, name='child_del'),
    path('vaccinationdetail_del/(?P<pk>\d+)/$', views.vaccinationdetail_del, name='vaccinationdetail_del'),
    path('vaccinecollection_del/(?P<pk>\d+)/$', views.vaccinecollection_del, name='vaccinecollection_del'),
    path('notification_del/(?P<pk>\d+)/$', views.notification_del, name='notification_del'),
    path('stock_update/(?P<pk>\d+)/$', views.stock_update, name='stock_update'),
]
