# โปรเจค My Web 

##  &larr; ความรู้ที่ได้รับ

###  1. การโคลนโปรเจ็คเริ่มต้นมาใส่ใน Repository โดยการเซ็ต Remote ใหม่โดยใช้คำสั่งโค๊ดว่า **git clone** 
```shell
> git clone <url>
```

##  คำสั่งเปลี่ยนชื่อไฟล์
```shell
> rename-item Project2565 Project2566
```

### การเซ็ต remote repository ภายใต้คำสั่ง **git remote set-url origin**
```shell
> git remote set-url origin <url>
```

### การเช็คสถานะว่า remote ชี้ไปที่ repository ไหนภายใต้คำสั่งโค๊ด **git remote -v**
```shell
> git remote -v
```

การสร้างตาราง และ การใช้ prefix chouces
```shell
        > prefix_choices =(
            (1,"นาย"),
            (2,"นางสาว"),
            (3,"นาง"),
        )
        
        class Student(models.Model):
            std_id =    models.IntegerField()
            prefix = models.IntegerField(choices=prefix_choices,    default=1)
            name=       models.CharField(max_length=255)
            lastname=   models.CharField(max_length=255)
            phone =     models.CharField(max_length=255)
            address=    models.TextField()
            
        
            class Meta:
                verbose_name = 'student'
                verbose_name_plural = 'student'
        
            def __str__(self):
                return self.name + " " + self.lastname


                >**❗️ การสร้างตารางสำหรับการเก็บข้อมูลบนพื้นฐานของ db.sqlite3**

```py
from  django.db  import  models

prefix_choices  = (

(1, "นาย"),

(2, "นางสาว"),

(3, "นาง"),

)
```
>** prefix_choices จะมีการเก็บค่าข้อมูลในตารางแบบตัวเลขจาก pointer ที่ 0 แต่หลังจาก function getModelChoice มีการดึงค่าไปใช้ จะกระบวนการที่จะดึงค่าจาก pointer ที่ 1 มาใช้แทน**

## [model.py]
class  Student(models.Model):

	std_id  =  models.IntegerField()

	prefix  =  models.IntegerField(choices=prefix_choices, default=1)

	name  =  models.CharField(max_length=255)

	lastname  =  models.CharField(max_length=255)

	phone  =  models.CharField(max_length=15)

	address  =  models.TextField()


	class  Meta:

	verbose_name  =  "Student"

	verbose_name_plural  =  "Students"


	def  __str__(self):

	return  self.name


	def  get_absolute_url(self):

	return  reversed("Student_detail", kwargs={"pk": self.pk})
```
>** Clss Student เพื่อใช้เก็บข้อมูลเกี่ยวกับนักศึกษา**

```py
class Major(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Major_detail", kwargs={"pk": self.pk})
```
>** Clss Major ใช้สำหรับเก็บข้อมูลคณะของนักศึกษา**

        
## 📕8. [urls.py]

```py
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home, name='home'),
    path('about',views.About,   name='about'),
    path('contact',views.Contact,   name='contact'),
    path('details/<int:id>', views.StudentDetails, name='details'),
]
```
>**🔺 กำหนด path ของการเรียกใช้งานในแต่ละ page ซึ่งจะมีการดึงข้อมูลทั้งหมดจาก functions ใน [views.py] มาใช้งาน และแสดงออกมาทางหน้าจอ**
## 📕9. [admin.py]

```py
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("std_id", "prefix", "name", "lastname", "phone", "major")
    search_fields = list_display

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = list_display
```
>**🔺 การแสดงตารางข้อมูลใน admin โดยมีการแสดงแบบแถว และมีการค้นหา**

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

>**🔺 ใช้คำสั่ง makemigrations และ migrate เพื่อสร้างฐานข้อมูล แล้วจึงใช้คำสั่ง  createsuperuser เพื่อสร้าง admin user ในการเข้าถึงฐานข้อมูล**
>
>**❗️ หลังจากการสร้าง หรือปรับเปลี่ยนตารางสำหรับการเก็บข้อมูลใหม่ทุกครั้งๆ จำเป็นจะต้องใช้คำสั่งดังกล่าวเพื่อสร้างฐานข้อมูลใหม่ด้วยเช่นกัน**
python manage.py 