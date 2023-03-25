from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Teacher(models.Model):

    Subject_Choices = (
    ('Mathematics','Mathematics'),
    ('Computer science', 'Computer science'),
    ('Physics','Physics'),
    ('History','History'),
    ('geography','geography'),
    ('Biology','Biology'),
    ('Chemistry','Chemistry'),
    ('English','English'),
    ('Arabic','Arabic'),
    ('more then 5 subjects','more then 5 subjects')
)

    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Profilepicture = models.ImageField(upload_to='profile/', default='user_pic/no-img.jpg', blank=True, null=True)
    EmailAddress = models.EmailField(max_length=255,unique=True)
    PhoneNumber = models.CharField(max_length=100)
    RoomNumber = models.CharField(max_length=100)
    Subjectstaught =MultiSelectField(max_length=100,choices=Subject_Choices,max_choices=5,default=0)


    def __str__(self):
        return self.FirstName