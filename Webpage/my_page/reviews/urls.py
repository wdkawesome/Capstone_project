from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Reviews
urlpatterns = [
path('',
ListView.as_view(
queryset=
Reviews.objects.all(),
template_name="review.html"
)
),
path('<int:pk>/',
DetailView.as_view(
model = Reviews,
template_name="student.html"
)
),
]