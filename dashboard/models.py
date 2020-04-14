from django.db import models


class WorkExperience(models.Model):
    name = models.CharField(max_length=250)
    start_year = models.DateField()
    end_year = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=250)
    actual_job = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return 'Trabaje en {}'.format(self.name)


class Education(models.Model):
    name = models.CharField(max_length=250)
    school_name = models.CharField(max_length=250)
    start_year = models.DateField()
    end_year = models.DateField(blank=True, null=True)

    def __str__(self):
        # Self es la instancia que esta accediendo al método, self es una convención, puede llamarse como sea.
        return self.name


class Skills(models.Model):
    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    name = models.CharField(max_length=255)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=15, blank=True, null=True)
    icon = models.ImageField(upload_to='icons/', max_length=350)

    def __str__(self):
        return '{} - Level: {}'.format(self.name, self.get_level_display())
