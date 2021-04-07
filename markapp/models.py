from django.db import models

# Create your models here.
location_choices=[
    ('Corporate Headoffice', 'Corporate Headoffice'),
    ('Operations Departments', 'Operations Departments'),
    ('Work Station', 'Work Station'),
    ('Marketing Division', 'Marketing Division'),
]

severity_choice=[
    ('Mild', 'Mild'),
    ('Moderate', 'Moderate'),
    ('Severe', 'Severe'),
    ('Fatal', 'Fatal'),
]

class Reportincident(models.Model):
    location = models.CharField(max_length = 100, choices = location_choices, default = '1')
    desc = models.CharField(max_length=300, null=True)
    date = models.DateField()
    time = models.TimeField()
    inc_location = models.CharField(max_length=100, null=True)
    severety = models.CharField(max_length = 100, choices = severity_choice, default = '1')
    cause = models.CharField(max_length=300, null=True)
    action = models.CharField(max_length=200, null=True)
    environment = models.BooleanField('environment', default=False)
    injury = models.BooleanField('injury', default=False)
    damage = models.BooleanField('damage', default=False)
    vehicle = models.BooleanField('vehicle', default=False)

    def __str__(self):
        return self.desc