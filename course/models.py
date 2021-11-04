from django.db import models





class skills(models.Model):
    title = models.CharField(max_length=124)


    def __str__(self):
        return self.title
