from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages
from .models import Person

# Create your views here.
def index(request):
    all_person = Person.objects.all()
    return render(request,"index.html",{"all_person":all_person})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        s_id = request.POST["s_id"]
        status = request.POST["status"]
        course = request.POST["course"]
        teacher = request.POST["teacher"]
        performance = request.POST["performance"]
        typ_work = request.POST["typ_work"]
        jour_name_place = request.POST["jour_name_place"]

        # บันทึกข้อมูล
        person = Person.objects.create(
            name=name,
            s_id=s_id,
            status=status,
            course=course,
            teacher=teacher,
            performance=performance,
            typ_work=typ_work,
            jour_name_place=jour_name_place,
        )
        person.save()
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        # เปลี่ยนเส้นทาง
        return redirect("/")
    else :
        return render(request,"form.html")

def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.s_id = request.POST["s_id"]
        person.status = request.POST["status"]
        person.course = request.POST["course"]
        person.teacher= request.POST["teacher"]
        person.performance = request.POST["performance"]
        person.typ_work = request.POST["typ_work"]
        person.jour_name_place = request.POST["jour_name_place"]
        person.save()
        messages.success(request,"อัพเดตข้อมูลเรียบร้อย")
        return redirect("/")
    else:
        # ดึงข้อมูลประชากรที่ต้องการแก้ไข
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})

def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/")

def chart1(request):
    
    return render(request,"chart1.html")

def chart2(request):
    return render(request,"chart2.html")

def chart3(request):
    return render(request,"chart3.html")

def chart4(request):
    return render(request,"chart4.html")


