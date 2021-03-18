from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class Department(models.Model):
    name = models.CharField(verbose_name='Department Name',max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def image_upload(instance, filename):
    return  f"employees/profile_images/{instance.department.name}/{instance.name}/{filename}"
class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Employee Name',max_length=200)
    email = models.EmailField(max_length=200)
    joined = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(verbose_name='Upload Image',upload_to=image_upload)

    def __str__(self):
        return self.name
@receiver(post_delete, sender=Employee)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
