from django.urls import path

from . import views, views2
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("hassan/", views.index, name="index"),
    path("notshow/", views2.index, name="index"),
     # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]