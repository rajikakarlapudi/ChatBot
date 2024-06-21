from django.db import models

class Domain(models.Model):
    DOMAIN_CHOICES = [
        ('Education', 'Education'),
        ('Legal', 'Legal'),
        ('Finance', 'Finance'),
        ('Real Estate', 'Real Estate'),
        ('News & Media', 'News & Media'),
        ('Others', 'Others'),
    ]

    name = models.CharField(max_length=50, choices=DOMAIN_CHOICES)

    def __str__(self):
        return self.name

class Dataset(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    file = models.FileField(upload_to='datasets/')

    def __str__(self):
        return f'{self.domain.name} - {self.file.name}'
