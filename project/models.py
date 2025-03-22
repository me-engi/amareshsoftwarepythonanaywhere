from django.db import models

class projectPageSEO(models.Model):
    meta_title = models.CharField(max_length=500, blank=True, null=True)
    meta_description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.meta_title
