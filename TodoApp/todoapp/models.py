from django.db import models


class TodoApp(models.Model):
    title = models.CharField(max_length=44)
    content = models.TextField()
    ended = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
