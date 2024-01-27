from django.db import models

# Create your models here.
class Member(models.Model):
    
    def __str__(self) -> str:
        return self.firstname
    
    firstname = models.CharField(max_length = 225)
    lastname = models.CharField (max_length = 225)
    phoneno = models.IntegerField(null=True)
    rollno= models.IntegerField(null=True)
    image= models.ImageField(default='default.jpg',upload_to='member_photo/')
    