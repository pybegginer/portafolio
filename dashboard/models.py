from django.db import models


class WorkExperience(models.Model):
    name = models.CharField(max_length=250)
    start_year = models.DateField()
    end_year = models.DateField()
    job_title = models.CharField(max_length=250)
    actual_job = models.BooleanField(default=False)
    description = models.TextField()
