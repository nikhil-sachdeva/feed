from django.db import models

# Create your models here.

class Post(models.Model):
    topic=models.CharField(max_length=50,help_text='What is the topic of the post?')
    body=models.CharField(max_length=150,help_text='Enter body of post')

    feelings=(
    ('h','happy'),
    ('s','sad'),
    ('e','excited'),
    ('a','angry'),
    )
    feel=models.CharField(max_length=1,choices=feelings,blank=True, default='h',help_text='what are you feeling?')
    date=models.DateField(null=True,blank=True)
    class Meta:
        ordering=["date"]

    def __str__(self):
        return self.topic
