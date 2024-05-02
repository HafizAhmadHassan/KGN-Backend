# does not work because of configuration
"""
from kgnWebApp.models import Question

print(Question.objects.all())
print("Hello, kekr,hassan")

from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
q.save()

print(q.id)


# -----------

from kgnWebApp.models import Question
# Run this in the Django shell
from datetime import datetime

# Sample questions and pub_dates
questions_data = [
    {"question_text": "What is the capital of France?", "pub_date": datetime.now()},
    {"question_text": "How many planets are there in the solar system?", "pub_date": datetime.now()},
    {"question_text": "Who wrote the novel 'To Kill a Mockingbird'?", "pub_date": datetime.now()},
    {"question_text": "What is the boiling point of water in Celsius?", "pub_date": datetime.now()},
    {"question_text": "Who painted the Mona Lisa?", "pub_date": datetime.now()},
    {"question_text": "What year did World War II end?", "pub_date": datetime.now()},
    {"question_text": "What is the chemical symbol for gold?", "pub_date": datetime.now()},
    {"question_text": "Who was the first person to step on the moon?", "pub_date": datetime.now()},
    {"question_text": "What is the largest mammal on Earth?", "pub_date": datetime.now()},
    {"question_text": "What is the tallest mountain in the world?", "pub_date": datetime.now()}
]

# Create and save questions
for data in questions_data:
    question = Question(**data)
    question.save()
    print(question.id)


"""




