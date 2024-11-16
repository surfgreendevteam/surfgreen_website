from django.db import models

# Create your models here.
class CO2Data(models.Model):
    session_id = models.CharField(max_length=255, blank=True, null=True)
    emissions = models.FloatField()
    path = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session_id} - {self.emissions}g CO2"