from django.db import models


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=100)

    def __str__(self):
        return self.name
