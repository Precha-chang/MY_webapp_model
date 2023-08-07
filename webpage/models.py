from django.db import models

# Create your models here.
prefix_choices = (
    (1,"นาย"),
    (2,"นางสาว"),
    (3,"นาง"),
)
class Major(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"

    def __str__(self):
        return self.name

class Student (models.Model):

    std_id = models.IntegerField()
    prefix = models.IntegerField(choices=prefix_choices,default=1)
    name = models.CharField(max_length=255)
    lastname = models.CharField (max_length=255)
    phone = models.CharField (max_length=15)
    address = models.TextField ()
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default=None, null=True , blank=True) 

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Student _detail", kwargs={"pk": self.pk})