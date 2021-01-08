from django.db.models import Min
from django.shortcuts import render
import faker
from .models import EmployeeData
fake=faker.Faker()
from django.http import HttpResponse

def fakedata_view(request):
    for i in range(100):
        first_name=fake.first_name()
        last_name=fake.last_name()
        email=fake.email()
        job=fake.random_element(elements=('HR','ADMIN','MANAGER','TA','SE'))
        salary=fake.random_element(elements=(10000,15000,20000,30000,35000))
        city=fake.random_element(elements=('Bang','Hyd','Delhi','lucknow','Mumbai'))
        state=fake.state()
        address=fake.address()

        data=EmployeeData(
            first_name=first_name,
            last_name=last_name,
            email=email,
            job=job,
            salary=salary,
            city=city,
            state=state,
            address=address,
        )
        data.save()
    return HttpResponse("Data Saved")

def fetching(request):
    alldata=EmployeeData.objects.all()
    employees = filterdumps=EmployeeData.objects.filter(salary__in=(10000,15000,30000))
    return render(request,'fakedatafile.html',{'employees':employees,'alldata':len(alldata),'filterdumps':len(filterdumps)})
