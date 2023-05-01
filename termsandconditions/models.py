from django.db import models

class Term(models.Model):
    term = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.term
