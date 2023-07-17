from django.db import models


class UniversityClasses(models.Model):
    title = models.CharField(max_length=50, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=50, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    #creates model manager
    object = models.Manager()

    #displays the object output value of the title and instructor name. Field as a tuple to display in the browser instead of the default titles
    def __str__(self):
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    #removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Classes"