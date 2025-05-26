from django.urls import path

from .views import CompetitionResultView

urlpatterns = [
    path("results/results/get-competition-result/", CompetitionResultView.as_view()),
]
