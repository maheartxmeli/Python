from django.db import models


class UniversityCampus(models.Model):
    campus = models.CharField(max_length=50, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)

    #creates model manager
    object = models.Manager()

    #displays the object output value of the title and instructor name. Field as a tuple to display in the browser instead of the default titles
    def __str__(self):
        display_campus = '{0.campus}, {0.state}'
        return display_campus.format(self)

    #removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"