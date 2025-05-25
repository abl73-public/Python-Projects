# campusApp/models.py

from django.db import models


# Create University Campus model
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)
    # Include a model Manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.campus_name}: {0.state}'
        return display_campus.format(self)

   # Create Meta class to display the model as University Campus
    class Meta:
        verbose_name_plural = "University Campus"


