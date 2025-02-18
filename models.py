from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # Corrected to models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)  # Corrected to models.DateTimeField()

    def __str__(self):
        return self.title  # Return the title instead of a non-existing name attribute
