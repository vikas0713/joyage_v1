from django.db import models


class JoyageModel(models.Model):

    '''
        Core Joyage Model which should be
        extended by all models henceforth
    '''

    deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True