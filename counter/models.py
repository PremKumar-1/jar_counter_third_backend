from django.db import models

class JarCount(models.Model):
    count = models.IntegerField()
    shift = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['shift']),
        ]

    def __str__(self):
        return f"{self.count} jars at {self.timestamp} during {self.shift} shift"
