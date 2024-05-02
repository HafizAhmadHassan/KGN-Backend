from django.db import models
import datetime

from django.utils import timezone

# Create your models here.
# Question is an object has question and publication date

"""

- A Choice has two fields: the text of the 
choice and a vote tally. 
- Each Choice is associated with a Question.

- Each Choice is related to a single Question. 
- Django supports all the common database relationships: 
many-to-one, many-to-many, and one-to-one.

"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # ...
    def __str__(self):
        return self.question_text
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
# ...
    def __str__(self):
        return self.choice_text




# model contains classes contians fields and has different types
    