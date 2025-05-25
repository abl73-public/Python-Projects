# classApp/models.py

from django.db import models


# Create University Classes model
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10000,decimal_places=2)
    # Include a model Manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_classes = '{0.title}: {0.instructor_name}'
        return display_classes.format(self)

    # Create Meta class to display the model as University Classes
    class Meta:
        verbose_name_plural = "University Classes"


