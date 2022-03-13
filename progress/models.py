from statistics import mode
from django.db import models

# Create your models here.


class course_data(models.Model):
    title=models.CharField(max_length=255, null=False)
    no_of_videos=models.IntegerField(default=0)
    no_of_videos_completed=models.IntegerField(default=0)
    user_name=models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title+" "+self.user_name



    