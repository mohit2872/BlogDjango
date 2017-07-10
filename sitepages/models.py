from django.db import models

# Create your models here.
class sitepages(models.Model):
    about_title = models.CharField(max_length=250)
    about_date = models.DateTimeField()
    about_info = models.TextField()

    def __str___(self):
        return self.about_title
