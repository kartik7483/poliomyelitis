from django.db import models

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=50)


class hospital(models.Model):
    hosp_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)


class stock(models.Model):
    stock_id = models.CharField(max_length=100)
    vaccine_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    last_updated =models.CharField(max_length=50)
    hosp_id = models.CharField(max_length=100)


class worker(models.Model):
    worker_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile_no =  models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    hosp_id = models.CharField(max_length=100)


class assignedarea(models.Model):
    area_id = models.CharField(max_length=100)
    area_name = models.CharField(max_length=100)
    worker_id = models.CharField(max_length=100)
    from_date = models.CharField(max_length=50)
    till_date = models.CharField(max_length=50)


class citizen(models.Model):
    citizen_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_no =  models.IntegerField()
    city = models.CharField(max_length=50)
    mail = models.CharField(max_length=60)




class vaccinationrequest(models.Model):
    request_id = models.CharField(max_length=100)
    citizen_id= models.CharField(max_length=100)
    citizen_name = models.CharField(max_length=100)     #city
    requested_date = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


class childInfo(models.Model):
    child_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    parent_contact = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    vaccine_status = models.CharField(max_length=50)

class dosagedetails(models.Model):
    dose_id = models.CharField(max_length=100)
    citizen_id = models.CharField(max_length=100)
    vaccine_name = models.CharField(max_length=100)
    dose_num = models.CharField(max_length=50)
    vaccination_date = models.CharField(max_length=50)
    given_by = models.CharField(max_length=100)    #worker_id


class vaccinationdetail(models.Model):
    record_id = models.CharField(max_length=100)
    vaccine_name = models.CharField(max_length=100)
    dose_num = models.CharField(max_length=50)
    vaccination_date = models.CharField(max_length=50)
    given_by = models.CharField(max_length=100)    #worker_id


class vaccinecollection(models.Model):
    collection_id = models.CharField(max_length=100)
    worker_id = models.CharField(max_length=100)
    vaccine_name = models.CharField(max_length=100)
    hosp_id = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    collection_date = models.CharField(max_length=50)


class notification(models.Model):
    vaccination = models.CharField(max_length=100)
    start_end_date = models.CharField(max_length=50)
    start_end_time = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
